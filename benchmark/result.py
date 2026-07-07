from dataclasses import dataclass

@dataclass
class BenchmarkResult:
    timestamp: str

    model_name: str
    prompt: str

    execution_time: float
    ttft: float
    output_tokens: int
    generation_time: float
    tokens_per_second: float

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