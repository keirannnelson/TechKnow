
def check_answer(user_answer, possible_answers):
    return user_answer.strip().lower() in {ans.lower() for ans in possible_answers}
