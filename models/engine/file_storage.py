#!/usr/bin/python3

"""
File Storage module
"""


import json
from os import path
from models.base_model import BaseModel


class FileStorage:
    """
    File storage class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in `__objects` the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        serializes `__objects` to the JSON file path
        """
        json_dict = {}
        for key, val in self.__objects.items():
            json_dict[key] = val.to_dict()
        with open(self.__file_path, mode='w', encoding="utf-8") as f:
            f.write(json.dumps(json_dict))

    def reload(self):
        """
        Deserializes JSON file to `__objects`
        """
        if path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding="utf-8") as f:
                json_dict = json.loads(f.read())
                for key, val in json_dict.items():
                    self.__objects[key] = eval(val["__class__"])(**val)
