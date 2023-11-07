from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "你是一个富有诗意的助手，擅长用创造性的天赋解释复杂的编程概念。"},
    {"role": "user", "content": "写一首诗来解释编程中递归的概念。"}
  ]
)

print(completion.choices[0].message)