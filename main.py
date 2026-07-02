import ollama

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

for chunk in response:
  print(chunk['message']['content'], end='', flush=True)
