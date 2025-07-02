

class Problem():
    """
    Holds a problem and relevant information, e.g.

    description, title, answers, etc.

    """

    def __init__(self, title, text, answers1, answers2, correct_answer1, correct_answer2):
        # NOTE Name of specific fields will probably change once real DB is generated
        
        self.title = title
        self.text = text

        if not isinstance(answers1, list):
            answers1 = answers1.split(',')
            answers1 = [i.strip() for i in answers1]

        if not isinstance(answers2, list):
            answers2 = answers2.split(',')
            answers2 = [i.strip() for i in answers2]

        self.answers1 = answers1
        self.answers2 = answers2

        if not isinstance(correct_answer1, list):
            correct_answer1 = correct_answer1.split(',')
            correct_answer1 = [i.strip() for i in correct_answer1]

        if not isinstance(correct_answer2, list):
            correct_answer2 = correct_answer2.split(',')
            correct_answer2 = [i.strip() for i in correct_answer2]

        self.correct_answer1 = correct_answer1
        self.correct_answer2 = correct_answer2

