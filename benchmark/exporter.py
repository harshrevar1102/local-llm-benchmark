import csv
from dataclasses import asdict
from pathlib import Path

from benchmark.result import BenchmarkResult


def save_csv(result: BenchmarkResult):

    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)

    metrics_file = results_dir / "benchmark_results.csv"
    outputs_file = results_dir / "benchmark_outputs.csv"

    result_dict = asdict(result)

    # ----------------------------------------------------
    # Metrics CSV (Numeric Data)
    # ----------------------------------------------------

    metrics_data = result_dict.copy()
    metrics_data.pop("generated_output")

    with open(metrics_file, "a", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=metrics_data.keys(),
        )

        if file.tell() == 0:
            writer.writeheader()

        writer.writerow(metrics_data)

    # ----------------------------------------------------
    # Outputs CSV (Model Responses)
    # ----------------------------------------------------

    output_data = {
        "session_id": result.session_id,
        "timestamp": result.timestamp,
        "model_name": result.model_name,
        "prompt_category": result.prompt_category,
        "temperature": result.temperature,
        "run_number": result.run_number,
        "prompt": result.prompt,
        "generated_output": result.generated_output,
    }

    with open(outputs_file, "a", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=output_data.keys(),
        )

        if file.tell() == 0:
            writer.writeheader()

        writer.writerow(output_data)