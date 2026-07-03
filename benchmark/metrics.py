from datetime import datetime
from benchmark.result import BenchmarkResult

def calculate_metrics(
    model_name,
    prompt,
    start_time,
    end_time,
    ttft,
    output_tokens,
    generation_time_ns,
):
    execution_time = end_time - start_time
    generation_time_seconds = generation_time_ns / 1_000_000_000
    tokens_per_second = output_tokens / generation_time_seconds
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return BenchmarkResult(
        timestamp=timestamp,
        model_name=model_name,
        prompt=prompt,

        execution_time=execution_time,
        ttft=ttft,
        output_tokens=output_tokens,
        generation_time=generation_time_seconds,
        tokens_per_second=tokens_per_second,
    )