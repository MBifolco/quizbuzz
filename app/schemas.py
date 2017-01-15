import datetime as dt
from marshmallow import Schema, fields, validate, pre_load, post_dump

class QuizzesSchema(Schema):
    name = fields.Str()
    description = fields.Str()
    status = fields.Int()

    # We add a post_dump hook to add an envelope to responses
    @post_dump(pass_many=True)
    def wrap(self, data, many):
        key = 'quizzes' if many else 'quiz'
        return {
            key: data
        }
