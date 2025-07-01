import os 
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

genai.api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(
    api_key=genai.api_key,
)

"""
# This module provides functions 
# to validate user input for various fields."""

def validate_abcd(input):
    if input.lower() not in {"a", "b", "c", "d"}:
        return False
    return True
 
def validate_number(input):
    try:
        int(input)
        return True
    except ValueError:
        return False
    
def validate_alphabetical(input):
    return input.strip().isalpha()

def validate_option(input, valid_options):
    return input.strip().lower() in {opt.lower() for opt in valid_options}

def refactor_option(input, valid_options):

    if not validate_option(input, valid_options):
        response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
        system_instruction="You take in an array of the valid answer choices and refactor the answer to match" \
        "one of the options if it is close enough. If it doesn't match any of the choices close enough, just return \"other\". " \
        "So you should ALWAYS return either one of the options from the array or \"other\""
        ),
        contents=f"Options: {valid_options}\nUser Answer:{input}",
        )
        return response.text
    else:
        return input
        