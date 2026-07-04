from benchmark.result import BenchmarkSummary


def print_report(summary: BenchmarkSummary):

    print("\n" + "=" * 50)
    print("Benchmark Summary")
    print("=" * 50)

    print(f"{'Model':<30}: {summary.model_name}")
    print(f"{'Runs':<30}: {summary.runs}")

    print()

    print(f"{'Average Execution Time':<30}: {summary.avg_execution_time:.4f} s")
    print(f"{'Average TTFT':<30}: {summary.avg_ttft:.4f} s")
    print(f"{'Average Output Tokens':<30}: {summary.avg_output_tokens:.2f}")
    print(f"{'Average Generation Time':<30}: {summary.avg_generation_time:.4f} s")
    print(f"{'Average Tokens / Second':<30}: {summary.avg_tokens_per_second:.2f}")

    print()

    print(f"{'Best Execution Time':<30}: {summary.best_execution_time:.4f} s")
    print(f"{'Worst Execution Time':<30}: {summary.worst_execution_time:.4f} s")

    print(f"{'Best TTFT':<30}: {summary.best_ttft:.4f} s")
    print(f"{'Worst TTFT':<30}: {summary.worst_ttft:.4f} s")

    print(f"{'Best TPS':<30}: {summary.best_tokens_per_second:.2f}")
    print(f"{'Worst TPS':<30}: {summary.worst_tokens_per_second:.2f}")

    print("=" * 50)