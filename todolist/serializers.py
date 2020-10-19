from pydantic import BaseModel, Field
from pydantic.main import ModelMetaclass
from pydantic.utils import GetterDict
from typing import List, Optional, Any

from .models import TodoList, Item, User

class NestedGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = self._obj
        for s in key.split('.'):
            res = getattr(res, s, default)
        return res

class SerializerMetaclass(ModelMetaclass):
    def __call__(cls, obj):
        return cls.from_orm(obj)


class Serializer(BaseModel, metaclass=ModelMetaclass):
    class Config:
        orm_mode = True
        getter_dict = NestedGetterDict

class TodoListSerializer(Serializer):
    id: int
    owner: Optional[int] = Field(alias='owner.id')


class TodoListCreate(Serializer):
    owner: Optional[int] = None

    async def save(self):
        validated_data = self.dict()
        if self.owner:
            validated_data['owner'] = User.objects.get(id=self.owner)
        else:
            del validated_data['owner']
        return await TodoList.objects.create(**validated_data)



class ItemCreate(Serializer):
    todolist: int
    value: str
    status: Optional[bool] = False

    async def save(self):
        validated_data = self.dict()
        validated_data['todolist'] = await TodoList.objects.get(id=self.todolist)
        return await Item.objects.create(**validated_data)


class ItemSerializer(Serializer):
    id: int
    todolist: Optional[int] = Field(alias='todolist.id')
    value: str
    status: bool
