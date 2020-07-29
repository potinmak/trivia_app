import os
from flask import Flask, request, abort, jsonify, json
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

#helper function for paginating the questions
def paginate_questions(request, selections):
  page = request.args.get('page', 1, type=int)
  start = (page - 1)* QUESTIONS_PER_PAGE
  end = start + QUESTIONS_PER_PAGE
  questions = [question.format() for question in selections]
  current_questions = questions[start:end]
  
  return current_questions

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  #Set up CORS. Allow '*' for origins. 
  CORS(app, resources={'/': {'origins': '*'}})

  #Use the after_request decorator to set Access-Control-Allow
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


  #Create an endpoint to handle GET requests for all available categories.
  @app.route('/categories', methods=['GET'])
  def retrieve_categories():
    #get all the categories and order them by their ids
    categories = Category.query.order_by(Category.id).all()
    old_categories = Category.query.all()
    current_categories_dict = {}
    #format them in a for-loop
    for c in categories:
      current_categories_dict[c.id] =c.type

    total_questions = Question.query.all()
    questions_display = paginate_questions(request, total_questions)
    
    #if there is no categories found then abort
    if len(current_categories_dict) == 0:
      abort (404)
  
    #return the json results
    return jsonify({
      #'success': True,
      "questions": questions_display,
      "total_questions": len(total_questions),
      "current_category": current_categories_dict,
      "categories": categories
    })

  #Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). 
  #This endpoint should return a list of questions, number of total questions, current category, categories. 

  #TEST: At this point, when you start the application you should see questions and categories generated,
  #ten questions per page and pagination at the bottom of the screen for three pages.
  #Clicking on the page numbers should update the questions. 

  @app.route('/questions')
  def retrieve_questions():

    #get all questions and order them by their ids
    questions = Question.query.order_by(Question.id).all()
    #paginate the questions
    questions_list = paginate_questions(request, questions)
    total_questions = len(questions)
    


    #get all the categories and add them to a dictionary
    categories = Category.query.order_by(Category.id).all()

    current_categories ={}
    for c in categories:
      current_categories[c.id] =c.type

    _questions= [(q.id) for q in questions]
    _categories_ = {c.id:c.type for c in categories}

    if _categories_ == '':
      abort(404)
    #abort if there is no questions
    if len(questions_list) == 0:
      abort(404)

    #return the json results
    return jsonify({
      "success": True,
      "questions": questions_list,
      "total_questions": total_questions,
      "categories": [category.format() for category in current_categories],
      "current_category":None,  
    })

#Create error handlers for all expected errors including 404, 422 and 500. 

  #@app.errorhandler(500)
  #def server_error(error):
  #  return jsonify({
  #    "success": False,
  #    "error": 500,
  #    "message": "Internal Server Error"
  #  }), 500

  


    
  
  #Create an endpoint to DELETE question using a question ID.
  #TEST: When you click the trash icon next to a question, the question will be removed.
  #This removal will persist in the database and when you refresh the page. 
  
  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    
    try:
      #get the question by their id
      question = Question.query.filter(id == question_id).one_or_none()
      
      #if the question does not exist, then abort 404 return resource not found
      if not question:
        abort(404)
      
      #delete the question if it exists
      
        
      question.delete()

      #refresh the question pool and paginate the lastest result
      question_selection = Question.query.order_by(question_id).all()
      current_questions = paginate_questions(request, question_selection)
      
      #return json result
      return jsonify({
        "succes":True,
        #"deleted": question_id,
        #"questions": current_questions,
        #"total_questions": len(question_selection),
        
        
        
      })
    except:
    
      abort(422)
      
  

 #Create an endpoint to POST a new question,  which will require the question and answer text, 
 # category, and difficulty score.se

 #TEST: When you submit a question on the "Add" tab, he form will clear and the question will appear at the 
 # end of the last page of the questions list in the "List" tab.  
  @app.route('/questions', methods=['POST'])
  def create_question():
    body = request.get_json()
    
    #getting new data from user' input
    new_question = body.get('question')
    new_category = body.get('category')
    new_answer = body.get('answer')
    new_difficulty = body.get('difficulty')

    #if one of the fields is missing then the request would become unprocessable
    if ((new_question is None) or (new_difficulty is None) or (new_answer is None) or (new_category is None)):
      abort(422)
    
    
    try:  #insert new records for Question
      question = Question(question=new_question, category=new_category, answer=new_answer, 
                          difficulty=new_difficulty)
      
      question.insert()
      
      #get all the questions and paginate the results
      new_selection = Question.query.order_by(Question.id).filter(Question.question.ilike('%{}%'.format(question)))
      new_ = Question.query.all()
      current_questions = paginate_questions(request, new_)

      #return json results
      return jsonify({
        "success" : True,
        "question" : current_questions,
    
        "create_id" : question.id,
        #"deleted": question.id,
        #'current_questions' : current_questions,
        "total_questions": len(new_)

      })
    except:
      abort(422)

  #Create a POST endpoint to get questions based on a search term. 
  #It should return any questions for whom the search term is a substring of the question. 

  #TEST: Search by any phrase. The questions list will update to include 
  #only question that include that string within their question. 
  #Try using the word "title" to start. 
  @app.route('/search_questions', methods=['POST'])
  def search_questions():
    body = request.get_json()
    search_term = body['searchTerm']

    #check to see if the search term is present
    if (body.get('searchTerm')):
      search_term = body['searchTerm']

    
    try:
      #query the database using search time to search the questions
      search_questions = Question.query.order_by(Question.id).filter(Question.question.ilike(f'%'+searchTerm+'%')).all()
      #paginated the search results
      current_questions = paginate_questions(request, search_questions)
      #query the categories and put them in order by id
      current_categories = Category.query.order_by(Category.id).all()
      #put questions in tuples
      questions_list = [(q.id.format(), q.type.format()) for q in search_questions]

      num = Question.query.all()

      #if there is not questions, return "resouces is not found" and abort it
      if len(questions_list)==0:
        abort(404)

      #same
      if current_categories is None:
        abort(404)
      
      #return the results
      return jsonify({
        "success": True,
        "questions": current_questions,
        "total_questions": len(current_questions),
        "current_category": "",
         
        #'categories_list': list(categories_list)
      })

    except:
      abort(400)


  #Create a GET endpoint to get questions based on category. 

  #TEST: In the "List" tab / main screen, clicking on one of the 
  #categories in the left column will cause only questions of that 
  #category to be shown. 
  @app.route('/categories/<int:id>/questions')
  def questions_search_by_category(id):
    
      #get category by their ids
    category_ = Category.query.all()
      #select questions and filter them by their category ids
      #c_id = category.id
    questions_selected = Question.query.filter_by(category=str(id)).all()
      

      #paginate the result
    questions_pool = paginate_questions(request, questions_selected)
      #if the category id is none then abort 400
    if category_ =='':
      abort(400)

      #if the questions id does not exist by search id
    if len(questions_selected)==0 :
      abort(404)

      

      #paginate the result
    return jsonify({
      #'success':True,
      #'category': Category.query.get(id).format(),
      'questions': questions_pool,
      'total_questions':len(questions_pool),
      'current_category': id
    })
      
 
 #Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters 
 # and return a random questions within the given category, if provided, and that is not one of the previous questions. 

 #TEST: In the "Play" tab, after a user selects "All" or a category,
 #one question at a time is displayed, the user is allowed to answer
 #and shown whether they were correct or not. 
  @app.route('/quizzes', methods=['POST'])
  def quizzes():
    
    #get the json data
    
    data = request.get_json() #data is like [^&(^*###@$^%&......)]
    #get data from previous questions
    previous_questions = data.get('previous_questions')
    #get the category
    quiz_catgeory = data.get('quiz_category')

    #abort if category or previous questions is none
    if ((quiz_category is None) or (previous_questions is None)):
      abort(400)

    previous_question=[]

    def check_used_q(qqqqqq):
      used = False
      for s in previous_questions:
        if (s == qqqqqq.id):
          used =True
      return used

    #format questions together
      qqq = Question.id.notin_(previous_questions)
      selected_question = Question.query.filter(Question.category == body['quiz_category']['id'], qqq)

      total_questions = len(questions)

  
    return jsonify({
      "success":True,
      "question":selected_question.format(),
      #"total_question":total_questions,
      #"previous_questions": previous_questions
    })
  
  @app.errorhandler(422)
  def unprocessable_entity(error):
    return jsonify({
      "success":False,
      "error":422,
      "message":"Unprocessable"
    }),422
  
  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      "success":False,
      "error":404,
      "message":"Resource Not Found"

    }), 404
  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      "success":False,
      "error":400,
      "message":"Bad Request"
    }), 400
    

    
  
 
  return app
