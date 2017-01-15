from peewee import *

database = SqliteDatabase('/opt/pythonenv/quizbuzz-env/quizbuzz/app/quizbuzz.db')

class BaseModel(Model):
    class Meta:
        database = database

class Quizzes(BaseModel):
    name = CharField(unique=True)
    description = TextField()
    create_date = DateTimeField()
    start_date = DateTimeField()
    status = BooleanField()

    class Meta:
        table = 'quizzes'

class Users(BaseModel):
    username = CharField(unique=True)
    password = CharField()
    create_date = DateTimeField()
    status = BooleanField()

    class Meta:
        table = 'users'

class Hosts(BaseModel):
    quiz_id = ForeignKeyField(Quizzes)
    user_id = ForeignKeyField(Users)
    create_date = DateTimeField()
    status = BooleanField()

    class Meta:
        table = 'hosts'

class Contestants(BaseModel):
    quiz_id = ForeignKeyField(Quizzes)
    user_id = ForeignKeyField(Users)
    create_date = DateTimeField()
    status = BooleanField()

    class Meta:
        table = 'contestants'

class Questions(BaseModel):
    quiz_id = ForeignKeyField(Quizzes)
    text = CharField()
    points_right = IntegerField()
    points_wrong = IntegerField()

    class Meta:
        table = 'questions'

class Choices(BaseModel):
    question_id = ForeignKeyField(Questions)
    text = CharField()
    order = CharField()
    correct = BooleanField()

    class Meta:
        table = 'choices'

class Answers(BaseModel):
    choice_id = ForeignKeyField(Choices)
    contestant_id = ForeignKeyField(Contestants)
    points = CharField()

    class Meta:
        table = 'answers'

if __name__ == "__main__":
   
    tables = [
        Quizzes,
        Users,
        Hosts,
        Contestants,
        Questions,
        Choices,
        Answers
    ]

    for table in tables:
        try:
            table.create_table()
        except OperationalError:
            print str(table) , " table already exists!"
            continue
