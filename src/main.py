import printing as pf
import queries
from problem import Problem
from input_validation import get_abcd_single, get_abcd_multi, get_number
from ai_feedback import give_feedback

DATABASE_PATH = 'testing.db'
TABLE_NAME = 'test_table'
letter_to_idx = {'a':0, 'b':1, 'c':2, 'd':3}


def main():
    # Greeting
    pf.print_general("""Welcome to TechKnow!
TechKnow is an interview prepper that helps you identify different styles of Leetcode problem based on the approach.
It also helps you learn the best data structures to use for each problem through quizzes with dynamic feedback.
                     
When prompted you will enter either integers or letters to select problems or answers. If you want to return to 
the start menu simply type 'back' and it will return you to the problem screen. If you want to exit the program type
exit and it will close the program. Have fun practicing!""", footer=False)
    

    while True:
        # Show problem menu
        problems = ['Longest Palindromic Substring', 'Container with most water', '3sum'] # query problems
        pf.print_problem_menu(problems, header=False)
        
        # Select problem (w/ input validation)
        user_input = get_number(1, len(problems))
        if user_input == 'back':
            continue
        elif user_input == 'exit':
            break

        problem_idx = int(user_input) - 1
        problem_name = problems[problem_idx]
        problem_title, problem_text, problem_answers1, problem_answers2, correct_answer1, correct_answer2  = queries.query_problem(problem_name, TABLE_NAME, DATABASE_PATH)
        

        problem = Problem(problem_title, problem_text, problem_answers1, problem_answers2, correct_answer1, correct_answer2)

        # Run quiz
        # Question 1
        pf.print_problem(problem.title, problem.text, footer=False)
        pf.print_approach_question(problem.answers1, header=False)

        user_input = get_abcd_single()
        if user_input == 'back':
            continue
        elif user_input == 'exit':
            break

        answer1 = problem.answers1[letter_to_idx[user_input]]
        

        # Question 2
        pf.print_data_structures_question(problem.answers2)
        
        user_input = get_abcd_single()
        if user_input == 'back':
            continue
        elif user_input == 'exit':
            break
        answer2 = problem.answers2[letter_to_idx[user_input]]
        

        # Give feedback
        pf.print_feedback(answer1, answer2, problem.correct_answer1, problem.correct_answer2)

    pf.print_general("Thank you for practicing with TechKnow!")



if __name__ == '__main__':
    main()