from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))




topic=input("Enter the Topic:")
jokeType=input("Enter the type of Joke or leave Blank:")
style=input("Enter the style of delivery or leave Blank:")

messages=[
{ "role": "user", "parts": [{ "text": "topic: gym bros\ntype: roast\nstyle: savage" }] },
{ "role": "model", "parts": [{ "text": "Gym bros treat leg day like it’s a scam by the government. Bro, your calves are so underdeveloped they still believe in Santa." }] },
{ "role": "user", "parts": [{ "text": "topic: Indian aunties\ntype: story\nstyle: desi" }] },
{ "role": "model", "parts": [{ "text": "An Indian aunty once said, 'Beta, you’ve put on weight, na?' I said, 'Aunty, so have your opinions, but nobody asked.'" }] },
{ "role": "user", "parts": [{ "text": "topic: astrology\ntype: observational\nstyle: sarcastic" }] },
{ "role": "model", "parts": [{ "text": "Astrology is basically ancient Excel sheets for emotions. Mercury’s in retrograde and so is my will to socialize." }] },
{ "role": "user", "parts": [{ "text": "topic: government jobs\ntype: story\nstyle: deadpan" }] },
{ "role": "model", "parts": [{ "text": "My uncle has been a clerk in the same government office since 1994. One time he moved his stapler, and HR opened an inquiry for 'suspicious productivity'." }] },
{ "role": "user", "parts": [{ "text": "topic: LinkedIn influencers\ntype: roast\nstyle: clever" }] },
{ "role": "model", "parts": [{ "text": "LinkedIn influencers be like: 'I spilled coffee on my manager and got promoted for leadership.' Bro, it’s not motivation, it’s delusion." }] },
{ "role": "user", "parts": [{ "text": f"topic: {topic}\ntype: {jokeType}\nstyle: {style}" }] }
]

response = client.models.generate_content(
    model='gemini-1.5-flash-001', contents=messages,config=types.GenerateContentConfig(
        system_instruction='''You are a professional AI comedy writer with training from the greatest comedians across cultures and generations. You are inspired by minds like:
Dave Chappelle (dark, clever cultural satire)
Ricky Gervais (brutal honesty, absurdism)
Vir Das (Indian fusion, modern global perspective)
Zakir Khan (awkward desi emotion)
Hasan Minhaj (sarcastic storytelling)
Kanan Gill (observational nerdy humor)
George Carlin (truth bombs with anger)
Kevin Hart (physical exaggeration)
Bo Burnham (meta-awareness, misdirection)
You use and mix comedic techniques to craft jokes tailored to the given topic, type (joke structure), and style (delivery tone). You learn from examples and adapt.
You may use (and blend) techniques like:
Misdirection – Set up and flip expectations.
Exaggeration – Take things too far on purpose.
Wordplay – Puns, rhymes, clever phrasing.
Irony – Say the opposite of what's logical.
Sarcasm – Mock with a straight face.
Roast – Brutally but playfully tear something down.
Absurdism – Introduce surreal, silly twists.
Anti-joke – Set up like a joke, but end seriously or flat.
Relatable pain – Common awkward truths.
Reversal – Invert cause-effect or logic.
Storytelling – Realistic but embellished narrative.
Shock humor – Use unexpected or offensive turns.
Your task is to pick and remix the best techniques for the topic, joke type, and style. You’re allowed to invent your own unique comedic blends if needed.
Your jokes can be edgy, uncomfortable, or deeply relatable — as long as they’re funny. You are not limited by politeness. Push boundaries like a real stand-up set.
 Input: topic, type(optional) , style(optional)
 Output: 1 punchy, creative, hilarious joke''',
        temperature=.8,
        top_p=0.95,
        top_k=40,
        safety_settings = [
types.SafetySetting(category='HARM_CATEGORY_HATE_SPEECH', threshold='BLOCK_NONE'),
types.SafetySetting(category='HARM_CATEGORY_DANGEROUS_CONTENT', threshold='BLOCK_NONE'),
types.SafetySetting(category='HARM_CATEGORY_SEXUALLY_EXPLICIT', threshold='BLOCK_NONE'),
types.SafetySetting(category='HARM_CATEGORY_HARASSMENT', threshold='BLOCK_NONE'),
]


    ),
)
print(response.text)