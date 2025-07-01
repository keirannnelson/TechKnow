import unittest
import sqlite3

from src.queries import query_problem

class TestQueries(unittest.TestCase):

    
    def setUp(self):

        # Create a testing database
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
        #f'INSERT INTO test_table  (question_title, question_text, answers1, answers2)  VALUES ({question_title}, {question_text}, {answers1}, {answers2}
        cur.execute(f'INSERT INTO test_table  (question_title, question_text, answers1, answers2)  VALUES ("{question_title}", "{question_text}", "{answers1}", "{answers2}");')
        
        con.commit()
        con.close()


    def test_query_problem_exists(self):
        question_title = 'title'
        question_text = 'text'
        answers1 = 'a, b, c, d'
        answers2 = 'a, b, c, d'
        
        self.assertEqual(query_problem('title', 'test_table', 'testing.db'), (question_title, question_text, answers1, answers2))
        

    def test_query_problem_no_record(self):
        with self.assertRaises(AssertionError):
            query_problem('fake_record', 'test_table', 'testing.db')


    def test_query_problem_no_table(self):
        with self.assertRaises(AssertionError):
            query_problem('title', 'fake', 'testing.db')

    
    def test_query_problem_no_db(self):
        with self.assertRaises(AssertionError):
            query_problem('title', 'test_table', 'fake.db')