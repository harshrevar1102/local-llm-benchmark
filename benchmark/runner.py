import ollama
import time
from benchmark.metrics import calculate_metrics
from benchmark.report import print_report

def benchmark_model(model_name, prompt):

    start_time = time.perf_counter()

    response = ollama.chat(
        model=model_name,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        stream = True,
    )


    # print(response['message']['content'])

    # print(response.message.content)

    first_chunk = True
    last_chunk = None

    for chunk in response:

        if first_chunk:
            ttft = time.perf_counter() - start_time
            first_chunk = False
    
        last_chunk = chunk  
        print(chunk['message']['content'], end='', flush=True)

    end_time = time.perf_counter()

    output_tokens = last_chunk.eval_count
    generation_time = last_chunk.eval_duration

    metrics = calculate_metrics(
    start_time=start_time,
    end_time=end_time,
    ttft=ttft,
    output_tokens=output_tokens,
    generation_time_ns=generation_time,
    )

    print_report(model_name, metrics)