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

output_tokens = last_chunk.eval_count
generation_time = last_chunk.eval_duration
seconds = generation_time / 1_000_000_000

TPS = output_tokens / seconds

print (f"\n\nExecution time: {end_time - start_time:.4f} seconds")
print (f"\nTime to first token: {ttft:.4f} seconds")
print (f"\nTokens per second: {TPS:.2f}")