"""
    Router for root (home) "/" endpoint
"""

from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def home():
    """ Get simple home page in HTML
    """

    return """
        <html>
            <head><title>Home</title></head>
            <body>
                <h1>Home Page</h1>
                <h2>Simple Server written in FastAPI!</h2>
            </body>
        </html>
        """