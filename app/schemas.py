import datetime as dt
from marshmallow import Schema, fields, validate, pre_load, post_dump

class QuizzesSchema(Schema):
    name = fields.Str()
    description = fields.Str()
    create_date = fields.DateTime()
    start_date = fields.DateTime()
    status = fields.Int()

    @pre_load
    def process_input(self, data):
        return data

    # We add a post_dump hook to add an envelope to responses
    @post_dump(pass_many=True)
    def wrap(self, data, many):
        key = 'quizzes' if many else 'quiz'
        return {
            key: data
        }
