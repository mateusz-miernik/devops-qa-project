"""
    Router for /random endpoint
"""

import random
from string import ascii_lowercase

from fastapi import APIRouter

router = APIRouter()


@router.get("/random")
def random_string(length=len(ascii_lowercase)):
    """ Generate random string from a set of ascii lowercase letters.

    :param length: Length of string
    :type length: int
    :returns: Random string with selected length.
    :rtype: str
    """

    ascii_lowercase_list = [*ascii_lowercase]
    random.shuffle(ascii_lowercase_list)
    return "".join(letter for letter in ascii_lowercase_list)[:length]
