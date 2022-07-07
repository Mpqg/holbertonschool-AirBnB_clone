#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
"""
File storage crud
"""


class FileStorage:
    """Class that store the files"""
    __file_path = "airbnb_database.json"
    __objects = {}

    def all(self):
        return (self.__objects)

    def new(self, obj):
        name_model_class = obj.__class__.__name__
        self.__objects["{}.{}".format(name_model_class, obj.id)] = obj

    def save(self):
        print(self.__objects)
        json_data = {key: obj.to_dict() for key, obj in self.__objects.items()}
        print(json_data)
        with open(FileStorage.__file_path, "w") as f:
            json.dump(json_data, f)

    def reload(self):
        try:
            fd = open(self.__file_path)
            objects = json.load(fd)
            for obj in objects.values():
                class_obj = obj["__class__"]
                del obj["__class__"]
                self.new(eval(class_obj)(**obj))
        except FileNotFoundError:
            return
