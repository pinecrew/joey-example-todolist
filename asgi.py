from joey import Application
from settings import settings
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


app = Application(settings)

app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
