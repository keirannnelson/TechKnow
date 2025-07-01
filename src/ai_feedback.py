import os 
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

genai.api_key =  os.getenv("GOOGLE_API_KEY")

client = genai.Client(
    api_key=genai.api_key,
)

def give_feedback(question, incorrect_answer, correct_answer):
    print("Generating response...")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
        system_instruction="You are an expert at leetcode and data structures and algorithms" \
        "and can let a user know why his answer to a question is incorrect given a question," \
        "correct answer, and the user's answer in a brief but very informative way. Please respond using only plain text, no Markdown."
        ),
        contents=f"Tell me why the correct answer to {question} is {correct_answer} and not {incorrect_answer}. Please respond using only plain text, no Markdown.",
    )
    return response.text
