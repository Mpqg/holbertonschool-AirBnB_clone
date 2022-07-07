#!/usr/bin/python3
from models import base_model
"""Review file"""


class Review(base_model.BaseModel):
    """
    Review class implementing base model
    """
    place_id = ""
    user_id = ""
    text = ""
