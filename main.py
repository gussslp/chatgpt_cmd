import openai

openai.api_key = "api_key"

prompt = input("Enter question: ")

model = "text-davinci-003"
response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=50)

generated_text = response.choices[0].text
print(generated_text)
