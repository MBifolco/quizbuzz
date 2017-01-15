from app import app
from flask import render_template, jsonify
from models import *
from schemas import *

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

quizzes_schema = QuizzesSchema(many=True)

@app.route('/quizzes/', methods=['GET'])
def get_quiz():
    quiz_list = Quizzes.select()
    result = quizzes_schema.dump(list(quiz_list))
    return jsonify(result.data)