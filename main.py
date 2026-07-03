from benchmark.runner import benchmark_model
from benchmark.report import print_report
from benchmark.exporter import save_csv

model = "phi3:mini"

prompt = "Explain recursion in exactly 100 words."

result = benchmark_model(model_name=model, prompt=prompt)
print_report(result=result)
save_csv(result)