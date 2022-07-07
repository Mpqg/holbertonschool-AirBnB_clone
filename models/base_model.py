#!/usr/bin/python3
from models import storage
"""
Base models controller
"""

from datetime import datetime
import uuid


class BaseModel:
    """
    BaseModel class
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor
        - id
        - created_at
        - updated_at
        """
        current_date = datetime.isoformat(datetime.now())
        self.id = str(uuid.uuid4())
        self.updated_at = datetime.today()
        self.created_at = datetime.today()

        if len(kwargs) == 0:
            storage.new(self)

    def save(self):
        """
        Save method
        """
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """
        Dictionary with attributes and formats
        """
        my_dict = dict(self.__dict__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["__class__"] = self.__class__.__name__
        return my_dict

    def __str__(self):
        """
        String representation of the class
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
