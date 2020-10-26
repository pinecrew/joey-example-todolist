from typing import List, Optional

import aiofiles
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from .models import TodoList, Item, User
from .serializers import TodoListSerializer, TodoListCreate, ItemSerializer, ItemCreate
from .auth import login as auth_login, logout as auth_logout

router = APIRouter()


class Credentials(BaseModel):
    login: str
    password: str


@router.post('/login')
async def login(credentials: Credentials, request: Request):
    try:
        user = await User.objects.get(name=credentials.login)
        if user.password == credentials.password:
            auth_login(request.scope, user)
            return {'name': user.name}
    except Exception:
        pass
    return {}


@router.get('/logout')
async def logout(request: Request):
    auth_logout(request.scope)


@router.get('/')
async def index():
    async with aiofiles.open('frontend/index.html', mode='r') as f:
        return HTMLResponse(await f.read())


@router.get('/lists', response_model=List[TodoListSerializer], response_model_by_alias=False)
async def lists():
    return await TodoList.objects.all()


@router.post('/lists', response_model=TodoListSerializer, response_model_by_alias=False)
async def new_list(lst: TodoListCreate, request: Request):
    user = request.scope['user']
    if lst.owner is None and user:
        lst.owner = user.id
    return await lst.save()


@router.get('/lists/{list_id}', response_model=TodoListSerializer, response_model_by_alias=False)
async def list_(list_id: int):
    return await TodoList.objects.get(id=list_id)


@router.get('/lists/{list_id}/items', response_model=List[ItemSerializer], response_model_by_alias=False)
async def items(list_id: int):
    return await Item.objects.filter(todolist=list_id).all()


@router.get('/items/{item_id}', response_model=ItemSerializer, response_model_by_alias=False)
async def item(item_id: int):
    return await Item.objects.get(id=item_id)


@router.post('/items/', response_model=ItemSerializer, response_model_by_alias=False)
async def new_item(item: ItemCreate):
    return await item.save()
