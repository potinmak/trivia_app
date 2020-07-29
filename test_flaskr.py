import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "postgres"
        self.database_path = "postgresql://{}@{}/{}".format('postgres:Liszt762!','localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_question = {
            "question": "What is the Weeked's hottest single currently in 2020?",
            "category": 5,
            "answer": "Blinding Lights",
            "difficulty": 5
            }
        self.second_question = {
            "question": "What is Obama's favoruite Prince song?",
            "category": 5,
            "answer": "Purple Rain",
            "difficulty": 5
            }
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    
    #Write at least one test for each test for successful operation and for expected errors.


  
    #1 testing number of questions we have in the table.
    def test_get_questions_error(self):
        category_id = 100
        response = self.client().get('/categories/{}/questions?page=10000'.format(category_id))
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Resource Not Found")


    #2  testing the number of categories set in the table.
    def test_get_categories(self): 
        res = self.client().get('api/categories?=42')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'],False)
        #self.assertEqual(len(data['categories']))


        

    #3 testing posting a new page and making sure it gets posted.
    def test_create_questions(self):
        res = self.client().post('/questions', json=self.new_question)
        data = json.loads(res.data)
        new_id = data['create_id']
        question_num = Question.query.all()
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['create_id'],new_id)

    #4 testing search engine of the page and make sure it can handle non-valid search.
    def test_search_questions(self):
        res = self.client().post('/search_questions', json={'searchTerm': 'Elly'})
        search_term = 'Elly'
        
        data = json.loads(res.data)
        questions_num = Question.query.all()
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'], 'Bad Request')

    #5 testing search questions by categories and make sure it can handle nonexistent questions.
    def test_search_questions_by_categories(self):
        res = self.client().get('/categories/800/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'],False)

    #6 testing when an invalid question id is received.
    def test_nonexistent_page(self):

        res = self.client().get('/questions?page=5000')
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['message'], "Resource Not Found")

    #7 testing when an non-existent page gets deleted.
    def test_delete_question_error(self):

        res = self.client().delete('/questions/5000')
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'],'Unprocessable')
        self.assertEqual(res.status_code, 422)

    #8 testing when a quiz is being played but the quiz is failed to load itself with empty jsons.

    def test_fail_playing_quiz(self):

        response = self.client().post('api/quizzes', json={})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Resource Not Found")

    #9 testing playing a quiz when previous questions are not available.
    def test_play_quiz_no_previous(self):
       
        res = self.client().post('/api/quizzes', json={"previous_questions": [56], "quiz_category": {"type": "History"}})
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)                 
        self.assertEqual(data['error'], 404)        

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
