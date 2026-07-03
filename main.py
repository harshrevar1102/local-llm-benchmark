from benchmark.runner import benchmark_model
from benchmark.report import print_report

model = "phi3:mini"

prompt = "Explain recursion in exactly 100 words."

result = benchmark_model(model_name=model, prompt=prompt)
print(result)