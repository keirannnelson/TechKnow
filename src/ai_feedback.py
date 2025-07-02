import os 
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

genai.api_key =  os.getenv("GOOGLE_API_KEY")

client = genai.Client(
    api_key=genai.api_key,
)

def give_feedback(question_ds, incorrect_answer_ds, correct_answer_ds, question_s, incorrect_answer_s, correct_answer_s, choice):
    if choice == "both":
        print("Generating response...")

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
            system_instruction="You are an expert at leetcode and data structures and algorithms" \
            "and can let a user know why their answer to a question is incorrect given a question," \
            "correct answer, and the user's answer in a brief but very informative way. Please respond using only plain text, no Markdown."
            ),
            contents=f"Tell me why the correct answer to {question_ds} is {correct_answer_ds} and not {incorrect_answer_ds}. Also tell me why the correct answer to {question_s} is {correct_answer_s} and not {incorrect_answer_s}.  Please respond using only plain text, no Markdown.",
        )
    elif choice == "style":
        print("Generating response...")

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
            system_instruction="You are an expert at leetcode and data structures and algorithms" \
            "and can let a user know why their answer to a question is incorrect given a question," \
            "correct answer, and the user's answer in a brief but very informative way. Please respond using only plain text, no Markdown."
            ),
            contents=f"Tell me why the correct answer to {question_s} is {correct_answer_s} and not {incorrect_answer_s}. Please respond using only plain text, no Markdown.",
        )
    elif choice == "datastructure":
        print("Generating response...")

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
            system_instruction="You are an expert at leetcode and data structures and algorithms" \
            "and can let a user know why their answer to a question is incorrect given a question," \
            "correct answer, and the user's answer in a brief but very informative way. Please respond using only plain text, no Markdown."
            ),
            contents=f"Tell me why the correct answer to {question_ds} is {correct_answer_ds} and not {incorrect_answer_ds}. Please respond using only plain text, no Markdown.",
        )
    else:
        return
    
    return response.text
