

class Problem():
    """
    Holds a problem and relevant information, e.g.

    description, title, answers, etc.

    """

    def __init__(self, title, text, answers1, answers2):
        # NOTE Name of specific fields will probably change once real DB is generated
        
        self.title = title
        self.text = text

        if not isinstance(answers1, list):
            answers1 = answers1.replace(',','').split(' ')

        if not isinstance(answers2, list):
            answers2 = answers2.replace(',','').split(' ')

        self.answers1 = answers1
        self.answers2 = answers2

