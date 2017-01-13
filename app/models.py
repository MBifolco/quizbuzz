from peewee import *

database = SqliteDatabase('quizbuzz.db')

class BaseModel(Model):
    class Meta:
        database = database

class Games(BaseModel):
    name = CharField()
    description = TextField()
    create_date = DateTimeField()
    status = BooleanField()

    class Meta:
        table = 'games'


if __name__ == "__main__":
    try:
        Games.create_table()
    except OperationalError:
        print "Games table already exists!"