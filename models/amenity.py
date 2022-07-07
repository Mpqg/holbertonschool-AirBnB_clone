#!/usr/bin/python3
from models import base_model
"""Amenity file"""


class Amenity(base_model.BaseModel):
    """
    Amenity class implementing base model
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialize method for amenity"""
        super().__init__(*args, **kwargs)
