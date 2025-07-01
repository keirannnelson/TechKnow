from input_validation import validate_abcd, validate_number, validate_alphabetical, validate_option, refactor_option
from input_evaluation import check_answer
from ai_feedback import give_feedback

""" Test validate_abcd"""
# print("Question 1:")
# print("A, B, C, or D?")
# print("a.\nb.\nc.\nd.")
# input = input()

# res = validate_abcd(input)
# print(f"{res}")

""" Test validate_number"""
# print("Question 2:")
# print("Give me a number:")
# input = input()

# res = validate_number(input)
# print(f"{res}")

""" Test validate_alphabetical"""
# print("Question 3:")
# print("Give me a word:")
# input = input()

# res = validate_alphabetical(input)
# print(f"{res}")

""" Test validate_option"""
# valid = ["Sliding Window", "Two Pointer", "Sorting", "Dynamic Programming"]
# input = input("What kind of problem is this? ")
# if validate_option(input, valid):
#     print("Valid choice.")
# else:
#     print("Try again.")

""" Test check_answer"""
# answers = ["2 pointer", "two pointer"]

# input = input("What's the answer?\n")

# print(f"{input} is {check_answer(input, answers)}")

""" Test give_feedback"""
# question = "Given the leetcode problem two-sum, what is the most efficient approach to solving the problem?"
# incorrect_answer = "Sorting"
# correct_answer = "Hash Map"

# feedback = give_feedback(question, incorrect_answer, correct_answer)
# print(feedback)


""" Test refactor_option"""
answers = ["Two Pointer", "Dynamic Programming", "Breadth First Search", "Depth First Search"]
user_answer = "2 Pointer"

new_answer = refactor_option(user_answer, answers)
print(new_answer)


