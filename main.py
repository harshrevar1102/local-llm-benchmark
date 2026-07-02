import ollama
import time

start_time = time.perf_counter()

response = ollama.chat(
    model="phi3:mini",
    messages=[
        {
            "role": "user",
            "content": "Tell me two jokes"
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
execution_time = end_time - start_time

output_tokens = last_chunk.eval_count
generation_time = last_chunk.eval_duration
generation_time_seconds = generation_time / 1_000_000_000

tokens_per_second = output_tokens / generation_time_seconds

print("\n" + "=" * 45)
print("        Benchmark Results")
print("=" * 45)

print(f"{'Model':<20}: phi3:mini")
print(f"{'Execution Time':<20}: {execution_time:.4f} s")
print(f"{'TTFT':<20}: {ttft:.4f} s")
print(f"{'Output Tokens':<20}: {output_tokens}")
print(f"{'Generation Time':<20}: {generation_time_seconds:.4f} s")
print(f"{'Tokens Per Second':<20}: {tokens_per_second:.2f}")

print("=" * 45)