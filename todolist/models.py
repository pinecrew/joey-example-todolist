from joey.db import Model
from pydantic import BaseModel
import orm

class User(Model):
    id = orm.Integer(primary_key=True)
    name = orm.String(max_length=100)
    password = orm.String(max_length=60)

class TodoList(Model):
    id = orm.Integer(primary_key=True)
    title = orm.String(max_length=100, default='')
    owner = orm.ForeignKey(User, allow_null=True)

class Item(Model):
    id = orm.Integer(primary_key=True)
    todolist = orm.ForeignKey(TodoList)
    value = orm.String(max_length=100)
    status = orm.Boolean(default=False)
