from input_evaluation import check_answer


def print_general(text, header=True, footer=True):
    if header:
        print('='*30)
    print()
    print(text)
    print()
    if footer:
        print('='*30)


def print_problem(question_title, question_text, header=True, footer=True):
    if header:
        print('='*30)
    print()
    print(question_title, ':', sep='')
    print(question_text)
    print()
    if footer:
        print('='*30)


def print_approach_question(answers, header=True, footer=True):
    assert len(answers) == 4, 'Problem does not have the correct number of answers'
    letters = ['a', 'b' ,'c', 'd']
    
    if header:
        print('='*30)
    print()
    print('Identify: what kind of problem is this?')

    for letter, answer in zip(letters, answers):
        print(f'\t{letter}. {answer}')

    print('Input the correct letter')

    print()
    if footer:
        print('='*30)


def print_data_structures_question(answers, header=True, footer=True):
    assert len(answers) == 4, 'Problem does not have the correct number of answers'
    letters = ['a', 'b' ,'c', 'd']
    
    if header:
        print('='*30)
    print()
    print('Consider: what kind of data structures should be used?')

    for letter, answer in zip(letters, answers):
        print(f'\t{letter}. {answer}')
    print('Input the correct letter')

    print()
    if footer:
        print('='*30)


def print_problem_menu(problems, header=True, footer=True):
    if header:
        print('='*30)
    print()
    print('Select a problem by inputting a number:')

    for i, problem in enumerate(problems):
        print(f'\t{i+1}. {problem}')

    print()
    if footer:
        print('='*30)

def print_feedback(user_answer1, user_answer2, correct_answer1, correct_answer2, header=True, footer=True):


    if header:
        print('='*30)

    print()
    if check_answer(user_answer1, correct_answer1):
        correct_answer1 = list(correct_answer1)
        if len(correct_answer1) == 1:
            print(f'Correct! This problem is a {correct_answer1[0]} problem ', end='')
        else:
            print(f'Correct! The problem is a ')
            
            for i in correct_answer1[:-1]:
                print(f'{i}', end=', ')

            print(f'and {correct_answer1[-1]} problem')
    else:
        correct_answer1 = list(correct_answer1)
        if len(correct_answer1) == 1:
            print(f'incorrect! This problem is a {correct_answer1[0]} problem ', end='')
        else:
            print(f'incorrect! The problem is a')
            
            for i in correct_answer1[:-1]:
                print(f'{i}', end=', ')

            print(f'and {correct_answer1[-1]} problem')
        
    print()
    if check_answer(user_answer2, correct_answer2):
        correct_answer2 = list(correct_answer2)
        if len(correct_answer2) == 1:
            print(f'Correct! The data structure utilized in this problem is a {correct_answer2[0]}')
        else:
            print('Correct! The data structures utilized in this problem are ', end='')
            
            for i in correct_answer2[:-1]:
                print(f'{i}', end=', ')

            print(f'and {correct_answer2[-1]}')

            
    else:
        correct_answer2 = list(correct_answer2)
        if len(correct_answer2) == 1:
            print(f'Incorrect! the only data structure utilized in this problem is a {correct_answer2[0]}')
        else:
            print('Incorrect! The data structures utilized in this problem are ', end='')
            for i in correct_answer2[:-1]:
                print(f'{i}', end=', ')

            print(f'and {correct_answer2[-1]}')
            
    print()
    if footer:
        print('='*30)