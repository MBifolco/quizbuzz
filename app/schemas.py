import datetime as dt
from marshmallow import Schema, fields, validate, pre_load, post_dump

class QuizzesSchema(Schema):
    id = fields.Int(required=False, dump_only= True)
    name = fields.Str()
    description = fields.Str()
    status = fields.Int()

