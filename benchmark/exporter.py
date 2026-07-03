from dataclasses import asdict
import csv
from pathlib import Path

from benchmark.result import BenchmarkResult


def save_csv(result: BenchmarkResult):

    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)

    csv_file = results_dir / "benchmark_results.csv"

    with open(csv_file, "a", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=BenchmarkResult.__dataclass_fields__.keys(),
        )

        if file.tell() == 0:
            writer.writeheader()

        writer.writerow(asdict(result))