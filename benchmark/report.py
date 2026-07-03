from benchmark.result import BenchmarkResult


def print_report(result: BenchmarkResult):

    print("\n" + "=" * 45)
    print("Benchmark Results")
    print("=" * 45)

    print(f"{'Model':<20}: {result.model_name}")
    print(f"{'Execution Time':<20}: {result.execution_time:.4f} s")
    print(f"{'TTFT':<20}: {result.ttft:.4f} s")
    print(f"{'Output Tokens':<20}: {result.output_tokens}")
    print(f"{'Generation Time':<20}: {result.generation_time:.4f} s")
    print(f"{'Tokens Per Second':<20}: {result.tokens_per_second:.2f}")

    print("=" * 45)