

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
    print('Question 1:')
    print()
    if user_answer1 == correct_answer1:
        print(f'Correct! The proper approach for the problem is {correct_answer1}')
    else:
        print(f'Incorrect, the proper approach for the problem was {correct_answer1}, not {user_answer1}')
    print()
    if user_answer2 == correct_answer2:
        print(f'Correct! The data structures utilized in this problem are {correct_answer2}')
    else:
        print(f'Incorrect, the data structures utilized in this problem are {correct_answer2}, not {user_answer2}')
    print()
    if footer:
        print('='*30)