from google import genai

client = genai.Client(api_key="")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="kenapa ada inflasi di Indonesia?",
)
print(response.text)