# Local LLM Benchmarking Framework

A lightweight benchmarking framework for evaluating locally hosted Large Language Models (LLMs) using Ollama.

The framework measures inference performance, structured output reliability, and JSON compliance across multiple models, prompts, and temperature settings.

---

## Features

- Benchmark multiple local LLMs
- Compare multiple temperature values
- Support multiple prompt categories
- Automatic warm-up before benchmarking
- Streaming inference support
- Time to First Token (TTFT) measurement
- Total execution time measurement
- Generation speed (Tokens/Second)
- Output token counting
- Automatic CSV export
- Full model output logging
- JSON output prompting
- Pydantic schema validation
- Automatic retry on invalid JSON
- Reliability statistics
- Session tracking

---

## Metrics Collected

For every benchmark run the framework records:

- Execution Time
- Time To First Token (TTFT)
- Output Tokens
- Generation Time
- Tokens per Second
- Prompt Category
- Temperature
- Run Number
- JSON Validation Status
- Retry Count
- Validation Errors

---

## Reliability Metrics

The framework also measures structured output reliability.

For every benchmark configuration it reports:

- JSON Validity Rate
- Retry Rate
- Successful Runs
- Failed Runs
- Total Retries

---

## Project Structure

```
local-llm-benchmark/
│
├── benchmark/
│   ├── aggregator.py
│   ├── config.py
│   ├── exporter.py
│   ├── metrics.py
│   ├── prompt_builder.py
│   ├── prompts.py
│   ├── report.py
│   ├── result.py
│   ├── runner.py
│   ├── schema.py
│   └── validator.py
│
├── results/
│   ├── benchmark_results.csv
│   └── benchmark_outputs.csv
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/harshrevar1102/local-llm-benchmark.git
cd local-llm-benchmark
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download Ollama

https://ollama.com

Pull the required models.

Example:

```bash
ollama pull phi3:mini
ollama pull llama3.2:latest
ollama pull gemma3:4b
```

Verify installation

```bash
ollama list
```

---

## Configure Benchmarks

Edit

```
benchmark/config.py
```

Example

```python
MODELS = [
    "phi3:mini",
    "llama3.2:latest",
    "gemma3:4b",
]

TEMPERATURES = [
    0.0,
    0.2,
    0.4,
    0.6,
    0.8,
]

NUM_RUNS = 5

SHOW_MODEL_OUTPUT = False
```

---

## Add Prompts

Edit

```
benchmark/prompts.py
```

Example

```python
PROMPTS = [
    {
        "category": "Reasoning",
        "text": "Explain recursion using a real-life example."
    },
    {
        "category": "Coding",
        "text": "Write Python code for Binary Search."
    }
]
```

---

## Run Benchmark

```bash
python main.py
```

Example output

```
Configuration 5/36

Model       : phi3:mini
Category    : Reasoning
Temperature : 0.6

Run 1/5 ✓
Run 2/5 ✓
Run 3/5 ✓

Benchmark Summary

Execution Time
TTFT
Output Tokens
Generation Time
Tokens / Second

Reliability

JSON Validity : 100%
Retry Rate : 0%
```

---

## Output Files

### benchmark_results.csv

Contains numerical benchmark metrics.

Example columns

```
session_id
timestamp
model_name
prompt_category
temperature
run_number
execution_time
ttft
output_tokens
generation_time
tokens_per_second
json_valid
retry_count
validation_error
```

---

### benchmark_outputs.csv

Stores the complete generated output for every benchmark run.

Useful for:

- Manual inspection
- Hallucination analysis
- Prompt evaluation
- Reliability studies

---

## Current Capabilities

- Multi-model benchmarking
- Multi-temperature evaluation
- Streaming inference benchmarking
- Automatic warm-up
- Structured JSON prompting
- Pydantic validation
- Automatic retry
- Reliability measurement
- CSV logging
- Session tracking

---

## Future Improvements

- Category-specific JSON schemas
- Prompt compliance scoring
- Response similarity analysis
- Memory usage benchmarking
- CPU and RAM monitoring
- GPU utilization
- Visualization dashboard
- HTML/PDF benchmark reports
- Parallel benchmarking
- Support for additional LLM providers

---

## Author

**Harsh Revar**

B.Tech Information Technology

National Institute of Technology Karnataka (NITK)

GitHub:
https://github.com/harshrevar1102