import pprint
import openai

openai.api_key = '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'

def update(messages, role, content):
    messages.append({"role":role, "content":content})
    return messages

def get_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response['choices'][0]['message']['content']

messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Меня зовут Александр. Я инженер-энергетик. Я работаю на коксохимическом заводе. Я учусь программированию на JavaScript."},
        {"role": "assistant", "content": "Привет, Александр. Что бы ты хотел знать?"},
    ]

while True:
    pprint.pprint(messages[-1])
    user_input = input("write=> ")
    messages = update(messages, "user", user_input)
    model_response = get_response(messages)
    messages = update(messages, "assistant", model_response)