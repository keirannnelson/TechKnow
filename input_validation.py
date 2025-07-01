
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
