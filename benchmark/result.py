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
class BenchmarkSummary:
    model_name: str
    runs: int

    avg_execution_time: float
    avg_ttft: float
    avg_output_tokens: float
    avg_generation_time: float
    avg_tokens_per_second: float

    best_execution_time: float
    worst_execution_time: float

    best_ttft: float
    worst_ttft: float

    best_tokens_per_second: float
    worst_tokens_per_second: float