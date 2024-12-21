import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.0-flash-exp")
chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Hello, how are you?"},
        {"role": "assistant", "parts": "I'm good, how can I help you today?"}
    ]
)
response = chat.send_message("I'm looking for a new book to read", stream=True)
for chunk in response:
    print(chunk.text)
    print("_" * 80)