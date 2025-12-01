"""
    Simple Web Server
"""

from fastapi import FastAPI
from app.routers import home, hello

app = FastAPI()
app.include_router(home.router)
app.include_router(hello.router)
