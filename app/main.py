"""
    Simple Web Server
"""

from fastapi import FastAPI
from app.routers import home

app = FastAPI()
app.include_router(home.router)
