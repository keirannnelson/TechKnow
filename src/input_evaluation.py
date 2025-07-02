
def check_answer(user_answers, possible_answers):
    """Checks if the user correctly answer a problem. For multichoice all answers must have been correct"""
    return len(set(user_answers) - set(possible_answers)) == 0 and len(user_answers) == len(possible_answers)