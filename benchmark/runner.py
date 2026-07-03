import ollama
import time

from benchmark.metrics import calculate_metrics

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

        
        print(chunk["message"]["content"], end="", flush=True)

    end_time = time.perf_counter()

    output_tokens = last_chunk.eval_count
    generation_time_ns = last_chunk.eval_duration

    result = calculate_metrics(
        model_name=model_name,
        prompt=prompt,
        start_time=start_time,
        end_time=end_time,
        ttft=ttft,
        output_tokens=output_tokens,
        generation_time_ns=generation_time_ns,
    )

    return result

def warmup_model(model_name: str, prompt: str):

    response = ollama.chat(
        model=model_name,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        stream=True,
    )

    for _ in response:
        pass

def run_benchmark(model_name: str, prompt: str, runs: int = 5):

    print("Warming up model...")

    warmup_model(model_name, prompt)

    print("Warm-up complete.\n")

    results = []
    for run in range(1, runs + 1):
        print(f"\nRun {run}/{runs}")
        result = benchmark_model(model_name, prompt)
        results.append(result)
        print("\n" + "-" * 50)

    return results