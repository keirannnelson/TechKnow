import os 

"""
This module provides functions to validate user input for various fields.
"""

def get_abcd_single():
    """Returns a valid a, b, c, d selection from user input"""
    user_input = input('>>> ')
    
    while user_input.lower() not in {"a", "b", "c", "d", "back", "exit"}:
        print('Please only enter characters A, B, C, or D')
        user_input = input('>>> ')
        

    return user_input

def get_abcd_multi():
    """Returns a valid a, b, c, d selection from user input"""
    valid_answers = {"a", "b", "c", "d"}
    user_input = input('>>> ')
    
    user_set = set()
    for i in user_input.split(' '):
        user_set.add(i.lower())

    while len(user_set.difference(valid_answers)) != 0 and user_input.lower() not in ['back', 'exit']:
        print('Please only enter characters A, B, C, or D, separated by a space')
        user_input = input('>>> ')
        user_set = set()
        for i in user_input.split():
            user_set.add(i.lower())


    return user_input
        
 
def get_number(lower_bound, upper_bound):
    """Returns a valid integer selection within the upper and lower bounds from user input"""
    valid_numbers = {f'{i}' for i in range(lower_bound, upper_bound + 1)}
    user_input = input('>>> ')

    while user_input not in valid_numbers and user_input not in ["back", "exit"]:
        print(f'Please only enter integers within [{lower_bound}, {upper_bound}]')
        user_input = input('>>> ')

    return user_input
    
def validate_alphabetical(input):
    return input.strip().isalpha()

def validate_option(input, valid_options):
    return input.strip().lower() in {opt.lower() for opt in valid_options}