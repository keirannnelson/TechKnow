import os
import sqlite3


class Problem():
    """
    Holds a problem and relevant information, e.g.

    description, title, answers, etc.

    """

    def __init__(self, problem_name, table_name, db_path):
        # NOTE Name of specific fields will probably change once real DB is generated
        title, text, answers1, answers2 = query_problem(problem_name, table_name, db_path)
        self.title = title
        self.text = text
        self.answers1 = answers1
        self.answers2 = answers2

# Note move to queries file later
def query_problem(problem_name, table_name, db_path):
    """
    Queries relevant information for a problem, e.g.
    
    question_title
    question_text
    answers1,
    answers2
    """
    assert os.path.exists(db_path), f'Database "{db_path}" does not exist'

    con = sqlite3.connect(db_path)
    cur = con.cursor()

    cur.execute(f'SELECT name FROM sqlite_master WHERE type="table" AND name="{table_name}";')
    res = cur.fetchall()
    assert res != None, f'Error: table "{table_name}" does not exist'

    # NOTE Name of specific fields will probably change once real DB is generated
    # Query DB and fetch a single record
    cur.execute(f'SELECT question_title, question_text, answers1, answers2 FROM {table_name} WHERE question_title = "{problem_name}";')
    res = cur.fetchone()

    assert res != None, f'Error: record "{problem_name}" does not exist in table "{table_name}"'
    con.close()

    return res