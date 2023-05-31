# Graphsignal: Observability for AI Stack

[![License](http://img.shields.io/github/license/graphsignal/graphsignal-python)](https://github.com/graphsignal/graphsignal-python/blob/main/LICENSE)
[![Version](https://img.shields.io/github/v/tag/graphsignal/graphsignal-python?label=version)](https://github.com/graphsignal/graphsignal-python)
[![Status](https://img.shields.io/uptimerobot/status/m787882560-d6b932eb0068e8e4ade7f40c?label=SaaS%20status)](https://stats.uptimerobot.com/gMBNpCqqqJ)


Graphsignal is an observability platform for AI agents and LLM-powered applications. It helps developers ensure AI applications run as expected and users have the best experience. With Graphsignal, developers can:

* Trace requests and runs with full AI context.
* See latency breakdown by operations.
* Analyze model API costs for deployments, models, or users.
* Get notified about errors and anomalies.
* Monitor API, compute, and GPU utilization.

[![Dashboards](https://graphsignal.com/external/screencast-dashboards.gif)](https://graphsignal.com/)

Learn more at [graphsignal.com](https://graphsignal.com).


## Install

Install Graphsignal library by running:

```
pip install graphsignal
```

Or clone and install the [GitHub repository](https://github.com/graphsignal/graphsignal-python):

```
git clone https://github.com/graphsignal/graphsignal-python.git
python setup.py install
```


## Configure

Configure Graphsignal tracer by specifying your API key directly or via `GRAPHSIGNAL_API_KEY` environment variable.

```python
import graphsignal

graphsignal.configure(api_key='my-api-key', deployment='my-model-prod-v1') 
```

To get an API key, sign up for a free account at [graphsignal.com](https://graphsignal.com). The key can then be found in your account's [Settings / API Keys](https://app.graphsignal.com/settings/api-keys) page.

Alternatively, you can add Graphsignal tracer at command line, when running your module or script. Environment variables `GRAPHSIGNAL_API_KEY` and `GRAPHSIGNAL_DEPLOYMENT` must be set.

```bash
python -m graphsignal <script>
```

```bash
python -m graphsignal -m <module>
```


## Integrate

Use the following examples to integrate Graphsignal tracer into your application. See integration documentation and [API reference](https://graphsignal.com/docs/reference/python-api/) for full reference. More integration examples are available in [examples](https://github.com/graphsignal/examples) repo.


### Tracing and monitoring

Graphsignal **auto-instruments** and traces libraries and frameworks, such as [OpenAI](https://graphsignal.com/docs/integrations/openai/), [LangChain](https://graphsignal.com/docs/integrations/langchain/), and many others.

To measure and monitor other operations, e.g. model inference or inference API calls, wrap the code with [`start_trace()`](https://graphsignal.com/docs/reference/python-api/#graphsignalstart_trace) method or use [`@trace_function`](https://graphsignal.com/docs/reference/python-api/#graphsignaltrace_function) decorator.

```python
with graphsignal.start_trace('predict'):
    pred = model(x)
```

```python
@graphsignal.trace_function
def predict(x):
    return model(x)
```

Enable profiling to additionally record code-level statistics. Profiling is disabled by default due to potential overhead. To enable, provide [`TraceOptions`](https://graphsignal.com/docs/reference/python-api/#graphsignaltraceoptions) object.

```python
with graphsignal.start_trace(
        operation='predict', 
        options=graphsignal.TraceOptions(enable_profiling=True)):
    pred = model(x)
```

The tracer will automatically choose a profiler depending on available modules. Currently, CProfile, PyTorch Kineto and Yappi are supported. The Kineto profiler is used if `torch` module is detected and Yappi profiler is used if `yappi` module is detected. Otherwise, CProfile is used. To properly profile `asyncio` coroutines, simply `pip install yappi`.


### Exception tracking

For auto-instrumented libraries, or when using `@trace_function` decorator, `start_trace()` method with `with` context manager or callbacks, exceptions are **automatically** recorded. For other cases, use [`Span.add_exception`](https://graphsignal.com/docs/reference/python-api/#graphsignalspanadd_exception) method.


### Data monitoring

Data, such as prompts and completions, is automatically monitored for auto-instrumented libraries. To track data metrics and record data profiles for other cases, [`Span.set_data()`](https://graphsignal.com/docs/reference/python-api/#graphsignalspanset_data) method can be used.

```python
with graphsignal.start_trace('predict') as span:
    span.set_data('input', input_data)
```

The following data types are currently supported: `list`, `dict`, `set`, `tuple`, `str`, `bytes`, `numpy.ndarray`, `tensorflow.Tensor`, `torch.Tensor`.

Raw data samples, such as prompts or completions, are recorded by default. To disable, set `record_data_samples=False` in `graphsignal.configure`. Note, that data statistics, such as size, shape or number of missing values will still be recorded.


## Observe

After everything is setup, [log in](https://app.graphsignal.com/) to Graphsignal to monitor and analyze your application and monitor for issues.


## Overhead

Graphsignal tracer is very lightweight. While all traces are monitored, Graphsignal tracer only records certain traces, automatically limiting the overhead. The overhead per trace is measured to be less than 100 microseconds.


## Security and Privacy

Graphsignal tracer can only open outbound connections to `signal-api.graphsignal.com` and send data, no inbound connections or commands are possible.

Raw data samples, e.g. prompts, are recorded by default. This feature can be disabled at tracer initialization time, if necessary.


## Troubleshooting

To enable debug logging, add `debug_mode=True` to `configure()`. If the debug log doesn't give you any hints on how to fix a problem, please report it to our support team via your account.

In case of connection issues, please make sure outgoing connections to `https://signal-api.graphsignal.com` are allowed.
