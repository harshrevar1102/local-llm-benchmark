from dataclasses import dataclass
@dataclass
class BenchmarkResult:
    session_id: str
    timestamp: str

    model_name: str
    prompt_category: str
    prompt: str

    temperature: float
    run_number: int

    execution_time: float
    ttft: float

    output_tokens: int
    generation_time: float
    tokens_per_second: float

    generated_output: str

@dataclass
class MetricStats:
    average: float
    median: float
    minimum: float
    maximum: float
    std_dev: float


@dataclass
class BenchmarkSummary:
    model_name: str
    runs: int

    execution_time: MetricStats
    ttft: MetricStats
    output_tokens: MetricStats
    generation_time: MetricStats
    tokens_per_second: MetricStats