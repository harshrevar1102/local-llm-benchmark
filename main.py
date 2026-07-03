from benchmark.runner import run_benchmark
from benchmark.report import print_report
from benchmark.exporter import save_csv


model = "phi3:mini"

prompt = "Tell me a joke."

results = run_benchmark(model_name=model, prompt=prompt, runs=5)
for result in results:
    print_report(result)
    save_csv(result)