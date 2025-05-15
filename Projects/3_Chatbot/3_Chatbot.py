from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import json
import re

def extract_json_if_present(response):
    try:
        # Naive check
        match = re.search(r"\{.*\}", response, re.DOTALL)
        if match:
            data = json.loads(match.group())
            return data
        return None
    except json.JSONDecodeError:
        return None


load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

f=open("system_instruction_salesbot.txt","r",encoding="utf-8")
system_details=f.read()
f.close()

messages=[]

flag=True

while(flag):
    user_prompt=input("[Client]: ")
    messages.append({ "role": "user", "parts": [{ "text": user_prompt}] })
    response = client.models.generate_content(
        model='gemini-1.5-flash-001', contents=messages,config=types.GenerateContentConfig(
            system_instruction=system_details,
            temperature=.6,
            top_p=0.75,
            top_k=30,
            max_output_tokens=200
        ),
    )
    if(response.text.find("(###END###)")==-1):
        print(f"[Clion Care]: {response.text}")
        messages.append({ "role": "model", "parts": [{ "text": response.text }] })
    else:
        data=extract_json_if_present(response.text)
        flag=False

print(data)