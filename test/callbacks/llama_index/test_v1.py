import unittest
import logging
import sys
import os
import json
import time
from unittest.mock import patch, Mock
from google.protobuf.json_format import MessageToJson
import pprint
import openai
from typing import Any, List, Mapping, Optional
from llama_index import GPTVectorStoreIndex, ServiceContext
from llama_index.embeddings.base import BaseEmbedding
from llama_index.readers.schema.base import Document
from llama_index.llm_predictor.structured import LLMPredictor
from langchain.llms.fake import FakeListLLM

import graphsignal
from graphsignal.uploader import Uploader
from graphsignal.callbacks.llama_index.v1 import GraphsignalCallbackHandler
from graphsignal.recorders.openai_recorder import OpenAIRecorder
from graphsignal.proto_utils import find_tag, find_data_count, find_data_sample

logger = logging.getLogger('graphsignal')

class TestEmbedding(BaseEmbedding):
    def _get_text_embedding(self, text: str) -> List[float]:
        embedding_map: Dict[str, List[float]] = {
            "one": [0.5, 0.5],
            "two": [1.0, 1.0]
        }

        return embedding_map[text]

    def _get_query_embedding(self, query: str) -> List[float]:
        embedding_map: Dict[str, List[float]] = {
            "one": [0.5, 0.5],
            "two": [1.0, 1.0]
        }

        return embedding_map[query]


class LlamaIndexCallbackHandlerTest(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        if len(logger.handlers) == 0:
            logger.addHandler(logging.StreamHandler(sys.stdout))
        graphsignal.configure(
            api_key='k1',
            deployment='d1',
            upload_on_shutdown=False,
            debug_mode=True)

    async def asyncTearDown(self):
        graphsignal.shutdown()

    @patch.object(Uploader, 'upload_span')
    async def test_callback(self, mocked_upload_span):
        os.environ['OPENAI_API_KEY'] = 'sk-kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'

        graphsignal.set_context_tag('ct1', 'v1')

        documents = [Document()]
        documents[0].text = "one"
        service_context = ServiceContext.from_defaults()
        service_context.embed_model = TestEmbedding(callback_manager=service_context.callback_manager)
        llm = FakeListLLM(responses=['three'])
        predictor = LLMPredictor(llm, callback_manager=service_context.callback_manager)
        service_context.llm_predictor = predictor

        index = GPTVectorStoreIndex.from_documents(documents, service_context=service_context)

        query_engine = index.as_query_engine()
        query_engine.query("two")

        #for call in mocked_upload_span.call_args_list:
        #    print(find_tag(call[0][0], 'operation'))

        index_root_span = find_call_by_operation(mocked_upload_span.call_args_list, 'llama_index.index_construction')
        self.assertEqual(index_root_span.labels, ['root'])
        self.assertEqual(find_tag(index_root_span, 'ct1'), 'v1')

        node_parsing_span = find_call_by_operation(mocked_upload_span.call_args_list, 'llama_index.op.node_parsing')
        self.assertEqual(find_tag(node_parsing_span, 'ct1'), 'v1')
        self.assertEqual(find_data_count(node_parsing_span, 'documents', 'element_count'), 1)
        self.assertEqual(node_parsing_span.context.parent_span_id, index_root_span.span_id)
        self.assertEqual(node_parsing_span.context.root_span_id, index_root_span.span_id)

        query_root_span = find_call_by_operation(mocked_upload_span.call_args_list, 'llama_index.query')
        self.assertEqual(query_root_span.labels, ['root'])
        self.assertEqual(find_tag(query_root_span, 'ct1'), 'v1')

        query_span = find_call_by_operation(mocked_upload_span.call_args_list, 'llama_index.op.query')
        self.assertEqual(find_tag(query_span, 'component'), 'Memory')
        self.assertEqual(find_tag(query_span, 'ct1'), 'v1')
        self.assertEqual(query_span.context.parent_span_id, query_root_span.span_id)
        self.assertEqual(query_span.context.root_span_id, query_root_span.span_id)

        retrieve_span = find_call_by_operation(mocked_upload_span.call_args_list, 'llama_index.op.retrieve')
        self.assertEqual(retrieve_span.labels, [])
        self.assertEqual(find_tag(retrieve_span, 'component'), 'Memory')
        self.assertEqual(find_tag(retrieve_span, 'ct1'), 'v1')
        self.assertEqual(retrieve_span.context.parent_span_id, query_span.span_id)
        self.assertEqual(retrieve_span.context.root_span_id, query_root_span.span_id)

        embedding_span = find_call_by_operation(mocked_upload_span.call_args_list, 'llama_index.op.embedding')
        self.assertEqual(embedding_span.labels, [])
        self.assertEqual(find_tag(embedding_span, 'component'), 'LLM')
        self.assertEqual(find_tag(embedding_span, 'ct1'), 'v1')
        self.assertEqual(retrieve_span.context.parent_span_id, query_span.span_id)
        self.assertEqual(retrieve_span.context.root_span_id, query_root_span.span_id)

        synthesize_span = find_call_by_operation(mocked_upload_span.call_args_list, 'llama_index.op.synthesize')
        self.assertEqual(synthesize_span.labels, [])
        self.assertEqual(find_tag(synthesize_span, 'component'), 'Memory')
        self.assertEqual(find_tag(synthesize_span, 'ct1'), 'v1')
        self.assertEqual(find_data_count(synthesize_span, 'response', 'char_count'), 5)
        self.assertEqual(synthesize_span.context.parent_span_id, query_span.span_id)
        self.assertEqual(synthesize_span.context.root_span_id, query_root_span.span_id)

        llm_span = find_call_by_operation(mocked_upload_span.call_args_list, 'llama_index.op.llm')
        self.assertEqual(llm_span.labels, [])
        self.assertEqual(find_tag(llm_span, 'component'), 'LLM')
        self.assertEqual(find_tag(llm_span, 'ct1'), 'v1')
        self.assertEqual(find_data_count(llm_span, 'formatted_prompt', 'char_count'), 158)
        self.assertIsNotNone(find_data_sample(llm_span, 'completion'))
        self.assertEqual(llm_span.context.parent_span_id, synthesize_span.span_id)
        self.assertEqual(llm_span.context.root_span_id, query_root_span.span_id)

        fake_llm_span = find_call_by_operation(mocked_upload_span.call_args_list, 'langchain.llms.fake.FakeListLLM')
        self.assertEqual(fake_llm_span.labels, [])
        self.assertEqual(find_tag(fake_llm_span, 'ct1'), 'v1')
        self.assertEqual(fake_llm_span.context.parent_span_id, llm_span.span_id)
        self.assertEqual(fake_llm_span.context.root_span_id, query_root_span.span_id)


def find_call_by_operation(calls, operation):
    for call in calls:
        if find_tag(call[0][0], 'operation') == operation:
            return call[0][0]