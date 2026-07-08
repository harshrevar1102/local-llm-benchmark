from datetime import datetime

from benchmark.result import BenchmarkResult


def calculate_metrics(
    session_id: str,
    model_name: str,
    prompt_category: str,
    prompt: str,
    temperature: float,
    run_number: int,
    generated_output: str,
    start_time: float,
    end_time: float,
    ttft: float,
    output_tokens: int,
    generation_time_ns: int,
):

    execution_time = end_time - start_time

    generation_time_seconds = generation_time_ns / 1_000_000_000

    tokens_per_second = output_tokens / generation_time_seconds

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return BenchmarkResult(
        session_id=session_id,
        timestamp=timestamp,

        model_name=model_name,
        prompt_category=prompt_category,
        prompt=prompt,

        temperature=temperature,
        run_number=run_number,

        execution_time=execution_time,
        ttft=ttft,

        output_tokens=output_tokens,
        generation_time=generation_time_seconds,
        tokens_per_second=tokens_per_second,

        generated_output=generated_output,
    )