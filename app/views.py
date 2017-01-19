from app import app
from flask import render_template, jsonify, request, g
from models import *
from schemas import *

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

quizzes_schema = QuizzesSchema(many=True)
quiz_schema = QuizzesSchema()

@app.route('/quizzes/', methods=['GET'])
def get_quizzes():
    quiz_list = Quizzes.select()
    result = quizzes_schema.dump(list(quiz_list))
    return jsonify(result.data)

@app.route('/quizzes/', methods=['POST'])
def new_quiz():
    json_input = request.get_json()
    print json_input
    quiz, errors = quiz_schema.load(json_input)
    if errors:
        return jsonify({'errors': errors}), 422

    quiz = Quizzes.create(
        name = quiz['name'],
        description = quiz['description'],
        status = quiz['status']
    )

    result = quiz_schema.dump(quiz)
    return jsonify(json_input)