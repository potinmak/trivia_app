# Full Stack API Final Project

## Full Stack Trivia

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a  webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out. 

That's where you come in! Help them finish the trivia app so they can start holding trivia and seeing who's the most knowledgeable of the bunch. The application must:

1) Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer. 
2) Delete questions.
3) Add questions and require that they include question and answer text.
4) Search for questions based on a text query string.
5) Play the quiz game, randomizing either all questions or within a specific category. 

Completing this trivia app will give you the ability to structure plan, implement, and test an API - skills essential for enabling your future applications to communicate with others. 

## Tasks

There are `TODO` comments throughout project. Start by reading the READMEs in:

1. [`./frontend/`](./frontend/README.md)

This project uses Nodejs and NPM pacakge. Therefore, you must download and install Node in order to view the app
on any browsers you want. Please follow this link for details in downloading the software.
https://nodejs.com/en/download.

After downloading the software, please insatlling the project dependencies here by typing this line on your
command line windows.

`npm start`


2. [`./backend/`](./backend/README.md)

We recommend following the instructions in those files in order. This order will look familiar from our prior work in the course.

Before getting into the virtual environment setup, please install the following dependencies in your `/backend` directory

`pip install -r requirements.txt`

This will install all of the required packages we selected within the requirements.txt file.

## Setting Up Your Server

To run the server, please execute the following: (this instruction is mainly for MacOS user)
`export FLASK_APP=app.py`
`export FLASK_ENV=development`
`flask run`

For Windows Command Line user, this would be
`set FLASK_APP=app.py`
`set FLASK_ENV=development`
`flask run`

For some Windows users, in order for the app to run, a virtual envrionment may have to be manually set
by going to your C:\Users\wongb\trivia_app\backend\flaskenv\Scripts and activate the activate.bat in the directory.

Setting `FLASK_APP` variable to `flaskr` will direct flask to the `flaskr` directory and use the `__init__.py` program
as the application program.

Setting `FLASK_ENV` variable to development will let flask detects file changes and keep the applicaion
under developer mode.


## Starting and Submitting the Project

[Fork](https://help.github.com/en/articles/fork-a-repo) the [project repository]() and [Clone](https://help.github.com/en/articles/cloning-a-repository) your forked repository to your machine. Work on the project locally and make sure to push all your changes to the remote repository before submitting the link to your repository in the Classroom. 

Before 

## About the Stack

We started the full stack application for you. It is desiged with some key functional areas:

### Backend

The `./backend` directory contains a partially completed Flask and SQLAlchemy server. You will work primarily in app.py to define your endpoints and can reference models.py for DB and SQLAlchemy setup. 

### Frontend

The `./frontend` directory contains a complete React frontend to consume the data from the Flask server. You will need to update the endpoints after you define them in the backend. Those areas are marked with TODO and can be searched for expediency. 

Pay special attention to what data the frontend is expecting from each API response to help guide how you format your API. 

[View the README.md within ./frontend for more details.](./frontend/README.md)

## Testing Your Program
To run the test in test_flaskr.py, please execute the following commands in your command window.

`dropdb trivia_test`
`createdb trivia_test`
`psql trivia_test < trivia.psql`
`python test_flaskr.py`

For Windows user, you may have to run the following command after logging into your
postgres server account

`DROP DATABASE trivia_test`
`CREATE DATABASE trivia_test`
`psql -h localhost -d trivia_test -U [your username] -f trivia.psql`
`python test_flaskr.py`

The application is set up in a way that is more favorable towards Mac OS user.
Therefore, additional research maybe necessary to edit or modify this program when running them.

## Your Task

Complete all TODO flags in backend/app.py:

1. Set up an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories.
2. Set up an ndpoint to handle GET requests for all available categories.
3. Set up an ndpoint to DELETE question using a question ID.
4. Set up an ndpoint to POST a new question, which will require the question and answer text, category, and difficulty score.
5. Create a POST endpoint to get questions based on category.
6. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question.
7. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions.

## API Reference

### Getting Started
-Base URL: As of present this application can only be run locally and is not hosted as a base URL.
 The backend app can be only hosted at  http://127.0.0.1:5000/ at this moment. More Updates will be released soon.
-Authentication: This application does not require authentication or any API keys.

### Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 422,
    "message": "Unprocessable"
}
```

This API will return three types of errors:

400 – Bad Request
404 – Resource Not Found
422 – Unprocessable

### Endpoints
* In general, it returns a list of questions.
* Results are paginated in a list and shows 10 questios per page.
* Sample: `curl http://127.0.0.1:5000/questions`

#### GET /questions:
- General:
    -returns a list of questions
    -results of the questions is presented in a list of 10.
    -total number of questions and list of their categoies, difficulties and answers will be returned as well.

```

  "questions": [
    {
      "answer": "Apollo 13", 
      "category": "5", 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": "5", 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Maya Angelou", 
      "category": "4", 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": "5", 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": "4", 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Brazil", 
      "category": "6", 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": "6", 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": "4", 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": "3", 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": "3", 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ], 
```
#### GET /categories:
* In general:
    -it returns a list of categoies, which is a totally 6 of them in there.
* Sample: curl http://127.0.0.1:5000/categories
```
 "categories": [
    {
      "id": 1, 
      "type": "Science"
    }, 
    {
      "id": 2, 
      "type": "Art"
    }, 
    {
      "id": 3, 
      "type": "Geography"
    }, 
    {
      "id": 4, 
      "type": "History"
    }, 
    {
      "id": 5, 
      "type": "Entertainment"
    }, 
    {
      "id": 6, 
      "type": "Sports"
    }
  ], 
```
#### DELETE /questions/<int:question_id>
* In general:
    - It deletes a question by its id with slash-id.
    - It returns id of the deleted question and number of questions after the deletion.

* Sample: curl http://127.0.0.1:5000/questions/10 -X DELETE
```{
        "succes":True,
        "deleted": 8,
        "total_questions": 18
        
    }
```
#### POST /questions
* In general:
    - It creates a new question using the submitted question, answer, category and difficulty.It returns
      the id of the created question, total number of questions, and question lists on current page to update the 
      frontend system.
    - The success of adding this record will also shows up in the json script.
* Sample:
    - curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question":"What is the Weeknd's hottest single of 2020?", "answer":"Blinding Lights", "difficulty":5, "category":"5"}'
```
{
  "questions": [
    {
      "question": "What is the Weeknd's hottest single of 2020?",
      "answer": Blinding Lights,
      "difficulty": 5,
      "category": "5"
    }
  ],
  "created_id": 24,
  "success": true,
  "total_questions": 20
}
```

#### POST/ search_questions/
* In general:
    -It creates a POST endpoint to get questions based on a search term. 
    -It returns unproccessable when a seach term does not exist in the database.

*   Sample:
    -curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"search_term": "The Weeknd"}'

```
 "questions": [
    {
      "answer": "Blinding Lights", 
      "category": "5", 
      "difficulty": 4, 
      "id": 24 , 
      "question": "What is the Weeknd's hottest single of 2020?"
    }

  "success": true, 
  "total_questions": 24
}
```
#### GET /categories/<int:id>/questions
* In general:
    this gets questions based upon category's id. It returns the category's type and its ids.
    It then returns a list of questiosn with the requested category id.
* Sample: curl http://127.0.0.1:5000/categories/2/questions
```
{
  "category": {
    "id": 2, 
    "type": "Art"
  }, 
  "current_category": 2, 
  "question": [
    {
      "answer": "Escher", 
      "category": "2", 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }, 
    {
      "answer": "Mona Lisa", 
      "category": "2", 
      "difficulty": 3, 
      "id": 17, 
      "question": "La Giaconda is better known as what?"
    }, 
    {
      "answer": "One", 
      "category": "2", 
      "difficulty": 4, 
      "id": 18, 
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }, 
    {
      "answer": "Jackson Pollock", 
      "category": "2", 
      "difficulty": 2, 
      "id": 19, 
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }
  ], 
  "success": true, 
  "total_questions": 24
}
```
#### POST/ quizzes
* In general:
    - This allows user to play the quiz with randomized questions.
    - This generates randomized questions based on whether the questions are used or not.
* Sample:
    curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions": [17, 18], 
```
    "quiz_category": {"type": "Art", "id": "2"}}'
    {
      "answer": "Jackson Pollock", 
      "category": "2", 
      "difficulty": 2, 
      "id": 19, 
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }
  ], 
  "success": true, 
```
#### Authors
    This README doc, API(`__init__py`) and unit test(`test_flaskr.py`) are written by Po Tin Mak
    All the other project files, except the driver programs, were written by instructors at Udacity and this project is part of the Udacity's Full Stack Web Development Nanodegree program.

