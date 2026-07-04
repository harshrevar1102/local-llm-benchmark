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

    runs = len(results)

    execution_times = [r.execution_time for r in results]

    ttfts = [r.ttft for r in results]

    output_tokens = [r.output_tokens for r in results]

    generation_times = [r.generation_time for r in results]

    tokens_per_second = [r.tokens_per_second for r in results]

    return BenchmarkSummary(
        model_name=results[0].model_name,
        runs=len(results),

        execution_time=calculate_stats(execution_times),
        ttft=calculate_stats(ttfts),
        output_tokens=calculate_stats(output_tokens),
        generation_time=calculate_stats(generation_times),
        tokens_per_second=calculate_stats(tokens_per_second),
    )