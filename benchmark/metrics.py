def calculate_metrics(
    start_time,
    end_time,
    ttft,
    output_tokens,
    generation_time_ns,
):
    execution_time = end_time - start_time
    generation_time_seconds = generation_time_ns / 1_000_000_000
    tokens_per_second = output_tokens / generation_time_seconds

    return {
        "execution_time": execution_time,
        "ttft": ttft,
        "output_tokens": output_tokens,
        "generation_time_seconds": generation_time_seconds,
        "tokens_per_second": tokens_per_second,
    }