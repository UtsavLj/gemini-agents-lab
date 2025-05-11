from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))



temperature=float(input("Enter the temperature[0.0 - 1.0]: "))
temperature= 0.0 if temperature<0 else temperature if temperature<1 else 1.0
 
prompt=input("Enter Your Prompt: ")

response = client.models.generate_content(
    model='gemini-1.5-flash-001', contents=prompt,config=types.GenerateContentConfig(
        system_instruction='You are an AI Chatbot responding in terminal',
        temperature=temperature,
        top_p=0.95,
        top_k=80,
    ),
)
print(response.text)