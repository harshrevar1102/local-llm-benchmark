import ollama
import time

from benchmark.metrics import calculate_metrics
from benchmark.config import MODELS, NUM_RUNS, TEMPERATURES
from benchmark.prompts import PROMPTS
from benchmark.aggregator import aggregate_results
from benchmark.report import print_report
from benchmark.exporter import save_csv


def benchmark_model(
        model_name: str,
        prompt: str,
        temperature: float,
        show_output: bool = True
):

    start_time = time.perf_counter()

    response = ollama.chat(
        model=model_name,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        options={
            "temperature": temperature,
        },
        stream=True,
    )


    # print(response['message']['content'])

    # print(response.message.content)

    first_chunk = True
    last_chunk = None
    generated_response = ""

    for chunk in response:

        if first_chunk:
            ttft = time.perf_counter() - start_time
            first_chunk = False

        last_chunk = chunk

        text = chunk["message"]["content"]
        generated_response += text

        if show_output:
            print(text, end="", flush=True)

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


def warmup_model(
        model_name: str,
        prompt: str,
        temperature: float
):

    response = ollama.chat(
        model=model_name,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        options={
            "temperature": temperature,
        },
        stream=True,
    )

    for _ in response:
        pass


def run_benchmark(
    model_name: str,
    prompt: str,
    temperature: float,
    runs: int = NUM_RUNS,
):

    print("Warming up model...")

    warmup_model(
        model_name=model_name,
        prompt=prompt,
        temperature=temperature,
    )

    print("Warm-up complete.\n")

    results = []

    for run in range(1, runs + 1):

        print(f"\nRun {run}/{runs}")

        result = benchmark_model(
            model_name=model_name,
            prompt=prompt,
            temperature=temperature,
            show_output=(run == 1),
        )

        results.append(result)

        if run != 1:
            print("✓")

        print("-" * 50)

    return results


def run_benchmark_suite():

    for model in MODELS:

        for prompt in PROMPTS:

            prompt_text = prompt["text"]
            category = prompt["category"]

            for temperature in TEMPERATURES:

                print("\n" + "=" * 70)
                print(f"Model       : {model}")
                print(f"Category    : {category}")
                print(f"Temperature : {temperature}")
                print("=" * 70)

                results = run_benchmark(
                    model_name=model,
                    prompt=prompt_text,
                    temperature=temperature,
                    runs=NUM_RUNS,
                )

                summary = aggregate_results(results)

                print_report(summary)

                for result in results:
                    save_csv(result)