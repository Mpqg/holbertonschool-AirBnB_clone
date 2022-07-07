#!/usr/bin/python3
from models import base_model
"""User file"""


class User(base_model.BaseModel):
    """
    User class implementing base model
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ Initialize method for user"""
        super().__init__(*args, **kwargs)
