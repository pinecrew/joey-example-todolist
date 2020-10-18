from joey import Application
from settings import settings
from fastapi.middleware.cors import CORSMiddleware

app = Application(settings)

app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])
