import printing as pf
import queries
from problem import Problem
from input_validation import get_abcd, get_number

DATABASE_PATH = 'testing.db'
TABLE_NAME = 'test_table'


def main():
    # Greeting
    pf.print_general('Welcome to TechKnow!', footer=False)

    # Show problem menu
    problems = ['title', 'title', 'title'] # query problems
    pf.print_problem_menu(problems, header=False)
    
    # Select problem (w/ input validation)
    problem_idx = get_number(1, len(problems)) - 1
    problem_name = problems[problem_idx]
    problem_data = queries.query_problem(problem_name, TABLE_NAME, DATABASE_PATH)
    problem = Problem(*problem_data)

    # Run quiz
    # Question 1
    pf.print_problem(problem.title, problem.text, footer=False)
    pf.print_approach_question(problem.answers1, header=False)

    answer1 = get_abcd()

    # Question 2
    pf.print_data_structures_question(problem.answers2)

    answer2 = get_abcd()


    # Give feedback
    pf.print_feedback

    # Restart at problem menu and option to exit



if __name__ == '__main__':
    main()