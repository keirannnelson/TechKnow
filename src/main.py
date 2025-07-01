import printing as pf
import queries
from problem import Problem

DATABASE_PATH = 'testing.db'
TABLE_NAME = 'test_table'


def main():
    # Greeting
    pf.print_general('Welcome to TechKnow!', footer=False)

    # Show problem menu
    problems = ['ex1', 'ex2', 'ex3'] # query problems
    pf.print_problem_menu(problems, header=False)
    
    # Select problem (w/ input validation)
    print('>>>USER INPUT')
    problem_name = 'title' # select
    problem_data = queries.query_problem(problem_name, TABLE_NAME, DATABASE_PATH)
    problem = Problem(*problem_data)

    # Run quiz
    pf.print_problem(problem.title, problem.text, footer=False)
    pf.print_approach_question(problem.answers1, header=False)

    print('>>>USER INPUT')
    answer1 = 'test answer' # get input and validate

    pf.print_data_structures_question(problem.answers2)

    print('>>>USER INPUT')
    answer2 = 'test answer' # get input and validate



    # Give feedback


    # Restart at problem menu and option to exit



if __name__ == '__main__':
    main()