from benchmark.result import BenchmarkResult, BenchmarkSummary


def aggregate_results(results: list[BenchmarkResult]):

    runs = len(results)

    return BenchmarkSummary(
        model_name=results[0].model_name,
        runs=runs,

        avg_execution_time=sum(r.execution_time for r in results) / runs,
        avg_ttft=sum(r.ttft for r in results) / runs,
        avg_output_tokens=sum(r.output_tokens for r in results) / runs,
        avg_generation_time=sum(r.generation_time for r in results) / runs,
        avg_tokens_per_second=sum(r.tokens_per_second for r in results) / runs,

        best_execution_time=min(r.execution_time for r in results),
        worst_execution_time=max(r.execution_time for r in results),

        best_ttft=min(r.ttft for r in results),
        worst_ttft=max(r.ttft for r in results),

        best_tokens_per_second=max(r.tokens_per_second for r in results),
        worst_tokens_per_second=min(r.tokens_per_second for r in results),
    )