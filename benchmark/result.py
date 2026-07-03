from dataclasses import dataclass


@dataclass
class BenchmarkResult:
    model_name: str
    prompt: str
    response: str

    execution_time: float
    ttft: float
    output_tokens: int
    generation_time: float
    tokens_per_second: float