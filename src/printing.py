

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