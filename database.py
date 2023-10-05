from peewee import *
from playhouse.sqliteq import SqliteQueueDatabase

db = SqliteQueueDatabase("by002.db")

class Games(Model):
    name = TextField(default="")
    publisher = TextField(default="")
    year = TextField(default="")

    class Meta:
        db_table = "Games"
        database = db


def connect():
    db.connect()
    Games.create_table()