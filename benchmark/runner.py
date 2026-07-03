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
    generated_response = ""

    for chunk in response:

        if first_chunk:
            ttft = time.perf_counter() - start_time
            first_chunk = False
    
        last_chunk = chunk

        text = chunk["message"]["content"]
        generated_response += text
        print(text, end="", flush=True)

    end_time = time.perf_counter()

    output_tokens = last_chunk.eval_count
    generation_time_ns = last_chunk.eval_duration

    result = calculate_metrics(
        model_name=model_name,
        prompt=prompt,
        response=generated_response,
        start_time=start_time,
        end_time=end_time,
        ttft=ttft,
        output_tokens=output_tokens,
        generation_time_ns=generation_time_ns,
    )

    return result