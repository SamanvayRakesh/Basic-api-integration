import openai


 openai.api_key = "Your-Openai-api-key"

# Define the assistant's role and the user's request
conversation = [
    {"role": "system", "content": "Act as a Python expert who provides precise and functional code."},
    {"role": "user", "content": "Can you write a Python script for a simple calculator?"}
]


result = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=conversation
0)


print(result['choices'][0]['message']['content'])
