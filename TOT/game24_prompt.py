from random import choice

from openai import OpenAI
from torchvision import message

import config


def deepseek(prompt, model='deepseek-chat', n=1):
    messages = [{'role': 'user', 'content': prompt}]
    output = []
    while n>0:
        cnt = min(n, 20)
        n -= cnt
        res = client.chat.completions.create(model=model, messages=messages, n=cnt)
        print('res:', res)
        output.extend([choice.message['content'] for choice in res.choices])
        print('output:', output)
    return output

def first_think(input):
    proposal = deepseek(input)

# for backward compatibility, you can still use `https://api.deepseek.com/v1` as `base_url`.
client = OpenAI(api_key=config.api_key, base_url=config.base_url)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    max_tokens=1024,
    temperature=0.7,
    stream=False
)

print(response.choices[0].message.content)
