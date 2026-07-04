from benchmark.runner import run_benchmark
from benchmark.report import print_report
from benchmark.exporter import save_csv
from benchmark.aggregator import aggregate_results


model = "phi3:mini"

prompt = "Tell me a joke."

results = run_benchmark(
    model_name=model, 
    prompt=prompt, 
    runs=5
)
summary = aggregate_results(results)

print_report(summary)

for result in results:
    save_csv(result)