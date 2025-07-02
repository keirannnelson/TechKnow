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

def get_abcd():
    """Returns a valid a, b, c, d selection from user input"""
    user_input = input('>>> ')
    while user_input.lower() not in {"a", "b", "c", "d"}:
        print('Please only enter characters A, B, C, or D')
        user_input = input('>>> ')

    return user_input
        
 
def get_number(lower_bound, upper_bound):
    """Returns a valid integer selection within the upper and lower bounds from user input"""
    valid_numbers = {f'{i}' for i in range(lower_bound, upper_bound + 1)}
    user_input = input('>>> ')

    while user_input not in valid_numbers:
        print(f'Please only enter integers within [{lower_bound}, {upper_bound}]')
        user_input = input('>>> ')

    return int(user_input)

"""
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
"""