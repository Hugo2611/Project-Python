from fastapi import FastAPI
from .api import app as api_router

app = FastAPI()

app.include_router(api_router)
