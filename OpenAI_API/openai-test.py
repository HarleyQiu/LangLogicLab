from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "你是助人为乐的AI"},
    {"role": "user", "content": "你会干什么"}
  ]
)

print(completion.choices[0].message)