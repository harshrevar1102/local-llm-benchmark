from benchmark.result import (
    BenchmarkResult,
    BenchmarkSummary,
    MetricStats,
)

import statistics


def calculate_stats(values):

    return MetricStats(
        average=statistics.mean(values),
        median=statistics.median(values),
        minimum=min(values),
        maximum=max(values),
        std_dev=statistics.stdev(values) if len(values) > 1 else 0,
    )


def aggregate_results(results: list[BenchmarkResult]):

    if not results:
        raise ValueError("No benchmark results to aggregate.")

    runs = len(results)

    execution_times = [r.execution_time for r in results]

    ttfts = [r.ttft for r in results]

    output_tokens = [r.output_tokens for r in results]

    generation_times = [r.generation_time for r in results]

    tokens_per_second = [r.tokens_per_second for r in results]

    successful_runs = sum(
        result.json_valid
        for result in results
    )

    failed_runs = runs - successful_runs

    total_retries = sum(
        result.retry_count
        for result in results
    )

    json_validity_rate = (
        successful_runs / runs
    ) * 100

    retry_rate = (
        total_retries / runs
    ) * 100

    return BenchmarkSummary(
        model_name=results[0].model_name,
        runs=runs,

        execution_time=calculate_stats(execution_times),
        ttft=calculate_stats(ttfts),
        output_tokens=calculate_stats(output_tokens),
        generation_time=calculate_stats(generation_times),
        tokens_per_second=calculate_stats(tokens_per_second),

        json_validity_rate=json_validity_rate,
        retry_rate=retry_rate,
        successful_runs=successful_runs,
        failed_runs=failed_runs,
        total_retries=total_retries,
    )