

class Problem():
    """
    Holds a problem and relevant information, e.g.

    description, title, answers, etc.

    """

    def __init__(self, title, text, answers1, answers2):
        # NOTE Name of specific fields will probably change once real DB is generated
        
        self.title = title
        self.text = text
        self.answers1 = answers1
        self.answers2 = answers2

