#!/usr/bin/python3

"""
User model that inherits from BaseModel class
"""


import models
from models.base_model import BaseModel


class User(BaseModel):
    """
    User model that inherits from Basemodel class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
