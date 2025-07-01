import os 
from google import genai
from google.genai import types

my_api_key = "AIzaSyBkaYLY8OjKdaFN4blXJ_L2R19Lp1yThNs"

genai.api_key = my_api_key


# WRITE YOUR CODE HERE

# Create an genAI client using the key from our environment variable
client = genai.Client(
    api_key=my_api_key,
)

def give_feedback(question, incorrect_answer, correct_answer):
    print("Generating response...")
    # Specify the model to use and the messages to send
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
        system_instruction="You are an expert at leetcode and data structures & algorithms" \
        "and can let a user know why his answer to a question is incorrect given a question," \
        "correct answer, and the user's answer in a brief but very informative way"
        ),
        contents=f"Tell me why the correct answer to {question} is {correct_answer} and not {incorrect_answer}",
    )
    return response.text
