#!/usr/bin/python3
from models import base_model
"""City file"""


class City(base_model.BaseModel):
    """
    City class implementing base model
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialize method for city"""
        super().__init__(*args, **kwargs)
