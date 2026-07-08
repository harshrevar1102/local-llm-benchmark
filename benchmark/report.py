from benchmark.result import BenchmarkSummary


def print_metric(name: str, stats):

    print(f"\n{name}")
    print("-" * 50)

    print(f"{'Average':<20}: {stats.average:.4f}")
    print(f"{'Median':<20}: {stats.median:.4f}")
    print(f"{'Minimum':<20}: {stats.minimum:.4f}")
    print(f"{'Maximum':<20}: {stats.maximum:.4f}")
    print(f"{'Std Dev':<20}: {stats.std_dev:.4f}")


def print_report(summary: BenchmarkSummary):

    print("\n" + "=" * 50)
    print("Benchmark Summary")
    print("=" * 50)

    print(f"{'Model':<30}: {summary.model_name}")
    print(f"{'Runs':<30}: {summary.runs}")
    print()

    print_metric("Execution Time (s)", summary.execution_time)

    print_metric("TTFT (s)", summary.ttft)

    print_metric("Output Tokens", summary.output_tokens)

    print_metric("Generation Time (s)", summary.generation_time)

    print_metric("Tokens / Second", summary.tokens_per_second)

    print("\nReliability")
    print("-" * 50)

    print(f"{'JSON Validity':<20}: {summary.json_validity_rate:.2f}%")
    print(f"{'Retry Rate':<20}: {summary.retry_rate:.2f}%")
    print(f"{'Successful Runs':<20}: {summary.successful_runs}")
    print(f"{'Failed Runs':<20}: {summary.failed_runs}")
    print(f"{'Total Retries':<20}: {summary.total_retries}")

    print("=" * 50)