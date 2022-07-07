#!/usr/bin/python3

"""
Base models controller
"""

from datetime import datetime
import uuid


class BaseModel:
    """
    BaseModel class
    """

    def __init__(self, **kwargs):
        """
        Constructor
        - id
        - created_at
        - updated_at
        """
        self.id = str(uuid.uuid4())
        self.updated_at = kwargs.get("updated_at", None)
        self.created_at = kwargs.get("created_at", None)

        current_date = datetime.isoformat(datetime.now())

        if self.updated_at is None:
            self.updated_at = current_date
        if self.created_at is None:
            self.created_at = current_date

    def save(self):
        """
        Save method
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        to_dict method
        """
        pass

    def __str__(self):
        """
        String representation of the class
        """
        print("[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__))
