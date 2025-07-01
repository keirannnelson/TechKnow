

def print_general(text):
    print('='*30)
    print()
    print(text)
    print()
    print('='*30)


def print_problem(question_title, question_text):
    print('='*30)
    print()
    print(question_title, ':', sep='')
    print(question_text)
    print()
    print('='*30)


def print_approach_question(answers):
    assert len(answers) == 4, 'Problem does not have the correct number of answers'
    letters = ['a', 'b' ,'c', 'd']
    
    print('='*30)
    print()
    print('Identify: what kind of problem is this?')

    for letter, answer in zip(letters, answers):
        print(f'\t{letter}. {answer}')

    print()
    print('='*30)

def print_data_structures_question(answers):
    assert len(answers) == 4, 'Problem does not have the correct number of answers'
    letters = ['a', 'b' ,'c', 'd']
    
    print('='*30)
    print()
    print('Consider: what kind of data structures should be used?')

    for letter, answer in zip(letters, answers):
        print(f'\t{letter}. {answer}')

    print()
    print('='*30)

