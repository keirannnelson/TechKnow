import unittest
import sqlite3

from src.problem import query_problem

class TestQueries(unittest.TestCase):

    
    def setUp(self):
        con = sqlite3.connect('testing.db')
        cur = con.cursor()
        cur.execute('''
            create table IF NOT EXISTS test_table(
                question_title TEXT,
                question_text TEXT,
                answers1 TEXT,
                answers2 TEXT
            );''')
        
        question_title = 'title'
        question_text = 'text'
        answers1 = 'a, b, c, d'
        answers2 = 'a, b, c, d'

        cur.execute(f'''INSERT INTO test_table(question_title, question_text, answers1, answers2) 
                    values ({question_title}, {question_text}, {answers1}, {answers2});''')
        
        con.commit()
        con.close()


    def test_query_problem_exists(self):
        question_title = 'title'
        question_text = 'text'
        answers1 = 'a, b, c, d'
        answers2 = 'a, b, c, d'
        
        self.assertEqual(query_problem('title', 'testing_table', 'testing.db'), (question_title, question_text, answers1, answers2))