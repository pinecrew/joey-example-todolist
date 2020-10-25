from joey import Application
from settings import settings
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from middleware import AuthenticationMiddleware, SessionMiddleware
from starlette.middleware import Middleware


app = Application(settings)

from todolist.models import User

app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])
app.add_middleware(AuthenticationMiddleware, user_model=User)
app.add_middleware(SessionMiddleware)

app.mount('/static', StaticFiles(directory='frontend/static'), name='static')
