from fastapi import APIRouter
from typing import List, Optional
from pydantic import BaseModel
from .models import TodoList, Item

router = APIRouter()


class TodoListResponse(BaseModel):
    id: int
    owner: Optional[int] = None


@router.get('/lists', response_model=List[TodoListResponse])
async def lists():
    data = await TodoList.objects.all()
    return ({'id': i.id, 'owner': i.owner.id} for i in data)


class TodoListCreate(BaseModel):
    owner: Optional[int] = None


@router.post('/lists', response_model=TodoListResponse)
async def new_list(lst: TodoListCreate):
    data = dict(lst)
    if not data['owner']:
        data.pop('owner')
    l = await TodoList.objects.create(**data)
    return {'id': l.id, 'owner': l.owner.id}


@router.get('/lists/{list_id}', response_model=TodoListResponse)
async def list_(list_id: int):
    l = await TodoList.objects.get(id=list_id)
    return {'id': l.id, 'owner': l.owner.id}


class ItemResponse(BaseModel):
    id: int
    list: int
    value: str
    status: bool


@router.get('/lists/{list_id}/items', response_model=List[ItemResponse])
async def items(list_id: int):
    data = await Item.objects.filter(todolist=list_id).all()
    return ({'id': i.id, 'list': i.todolist.id, 'value': i.value, 'status': i.status} for i in data)


@router.get('/items/{item_id}', response_model=ItemResponse)
async def item(item_id: int):
    i = await Item.objects.get(id=item_id)
    return {'id': i.id, 'list': i.todolist.id, 'value': i.value, 'status': i.status}


class ItemCreate(BaseModel):
    todolist: int
    value: str
    status: Optional[bool] = False


@router.post('/items/', response_model=ItemResponse)
async def new_item(item: ItemCreate):
    data = dict(item)
    data['todolist'] = await TodoList.objects.get(id=data['todolist'])
    i = await Item.objects.create(**data)
    return {'id': i.id, 'list': i.todolist.id, 'value': i.value, 'status': i.status}
