"""
    Router for /hello endpoint
"""

from fastapi import APIRouter


router = APIRouter()


@router.get("/hello")
def hello():
    """ Return 'hello' string.

    :returns: 'hello' string
    :rtype: str
    """
    return "hello"
