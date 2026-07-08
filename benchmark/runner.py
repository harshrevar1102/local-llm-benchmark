import ollama
import time

from datetime import datetime

from benchmark.metrics import calculate_metrics
from benchmark.config import (
    MODELS,
    NUM_RUNS,
    TEMPERATURES,
    SHOW_MODEL_OUTPUT,
)
from benchmark.prompts import PROMPTS
from benchmark.aggregator import aggregate_results
from benchmark.report import print_report
from benchmark.exporter import save_csv
from benchmark.prompt_builder import build_json_prompt
from benchmark.validator import validate_output


def generate_response(
        model_name: str,
        prompt: str,
        temperature: float,
        show_output: bool,
):

    start_time = time.perf_counter()

    json_prompt = build_json_prompt(prompt)

    response = ollama.chat(
        model=model_name,
        messages=[
            {
                "role": "user",
                "content": json_prompt,
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

    return (
        generated_response,
        ttft,
        last_chunk,
        start_time,
        end_time,
    )


def benchmark_model(
        session_id: str,
        model_name: str,
        prompt_category: str,
        prompt: str,
        temperature: float,
        run_number: int,
        show_output: bool = SHOW_MODEL_OUTPUT,
):

    generated_response, ttft, last_chunk, start_time, end_time = generate_response(
        model_name=model_name,
        prompt=prompt,
        temperature=temperature,
        show_output=False,
    )

    valid, parsed, error = validate_output(generated_response)

    retry_count = 0

    if not valid:

        print("\nInvalid JSON detected.")
        print("Retrying once...")

        retry_count = 1

        generated_response, ttft, last_chunk, start_time, end_time = generate_response(
            model_name=model_name,
            prompt=prompt,
            temperature=temperature,
            show_output=show_output,
        )

        valid, parsed, error = validate_output(generated_response)

    print(f"\nJSON Valid : {valid}")

    if not valid:
        print(f"Validation Error : {error}")
        if valid:
            print("Retry successful.")
        else:
            print("Retry failed. Continuing benchmark.")

    output_tokens = last_chunk.eval_count
    generation_time_ns = last_chunk.eval_duration

    result = calculate_metrics(
        session_id=session_id,
        model_name=model_name,
        prompt_category=prompt_category,
        prompt=prompt,
        temperature=temperature,
        run_number=run_number,
        generated_output=generated_response,
        start_time=start_time,
        end_time=end_time,
        ttft=ttft,
        output_tokens=output_tokens,
        generation_time_ns=generation_time_ns,
        json_valid=valid,
        retry_count=retry_count,
        validation_error=error if not valid else None,
    )

    return result

def warmup_model(
        model_name: str,
        prompt: str,
        temperature: float,
):

    json_prompt = build_json_prompt(prompt)

    response = ollama.chat(
        model=model_name,
        messages=[
            {
                "role": "user",
                "content": json_prompt,
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
    session_id: str,
    model_name: str,
    prompt_category: str,
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

        print(f"Run {run}/{runs}...", end=" ")

        result = benchmark_model(
            session_id=session_id,
            model_name=model_name,
            prompt_category=prompt_category,
            prompt=prompt,
            temperature=temperature,
            run_number=run,
            show_output=SHOW_MODEL_OUTPUT,
        )

        results.append(result)

        print("✓")

    print("-" * 50)

    return results


def run_benchmark_suite():

    session_id = datetime.now().strftime("%Y%m%d_%H%M%S")

    total_configs = (
        len(MODELS)
        * len(PROMPTS)
        * len(TEMPERATURES)
    )

    config_number = 1

    for model in MODELS:

        for prompt in PROMPTS:

            prompt_text = prompt["text"]
            category = prompt["category"]

            for temperature in TEMPERATURES:

                print("\n" + "=" * 70)
                print(
                    f"Configuration {config_number}/{total_configs}"
                )
                print(f"Session ID  : {session_id}")
                print(f"Model       : {model}")
                print(f"Category    : {category}")
                print(f"Temperature : {temperature}")
                print("=" * 70)

                results = run_benchmark(
                    session_id=session_id,
                    model_name=model,
                    prompt_category=category,
                    prompt=prompt_text,
                    temperature=temperature,
                    runs=NUM_RUNS,
                )

                summary = aggregate_results(results)

                print_report(summary)

                for result in results:
                    save_csv(result)

                config_number += 1

    print("\n" + "=" * 80)
    print("Benchmark Suite Completed Successfully.")
    print("=" * 80)