

from settings import get_settings


client, model_name = get_settings()


completion = client.chat.completions.create(
    model=model_name,
    messages=[
        {"role": "system", "content": "You're a helpful assistant."},
        {
            "role": "user",
            "content": "Write a limerick about the Python programming language.",
        },
    ],
)

response = completion.choices[0].message.content
print(response)
