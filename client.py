completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Assistant."},
        {"role": "user", "content": "What is coding?"}
    ]
)

print(completion.choices[0].message)
