from google import genai


client = genai.Client()
prompt = input("Enter your prompt: ")

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=prompt
)

print(response.text)