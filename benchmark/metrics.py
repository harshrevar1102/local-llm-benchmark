from datetime import datetime

from benchmark.result import BenchmarkResult


def calculate_metrics(
    session_id,
    model_name,
    prompt_category,
    prompt,
    temperature,
    run_number,
    generated_output,
    start_time,
    end_time,
    ttft,
    output_tokens,
    generation_time_ns,
    json_valid,
    retry_count,
    validation_error,
):

    execution_time = end_time - start_time

    generation_time_seconds = generation_time_ns / 1_000_000_000

    tokens_per_second = (
        output_tokens / generation_time_seconds
        if generation_time_seconds > 0
        else 0.0
    )

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
        json_valid=json_valid,
        retry_count=retry_count,
        validation_error=validation_error,
    )