#!/usr/bin/python3

"""
File Storage module
"""


import json


class FileStorage:
    """
    File storage class
    """
    __file_path = "objects.json"
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
        self.__object[key] = obj

    def save(self):
        """
        serializes `__objects` to the JSON file path
        """
        //

    def reload(self):
        """
        Deserializes JSON file to `__objects`
        """
