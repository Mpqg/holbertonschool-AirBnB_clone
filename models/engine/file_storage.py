#!/usr/bin/python3
import json
"""
File storage crud
"""


class FileStorage:
    """Class that store the files"""
    __file_path = "airbnb_database.json"
    __objects = dict()

    def all(self):
        return (self.__objects)

    def new(self, obj):
        name_model_class = obj.__class__.__name__
        self.__objects["{}.{}".format(name_model_class, obj.id)] = obj

    def save(self):
        fd = open(self.__file_path, "w")
        json.dump(self.__objects, fd)

    def reload(self):
        