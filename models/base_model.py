#!/usr/bin/python3

"""
A base model for the AirBnB models
"""


import models
import uuid
from datetime import datetime


class BaseModel:
    """
    Defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Base Model constructor method
        Default values are initialized here
        """
        if kwargs:
            for key, val in kwargs.items():
                if key in ("created_at", "updated_at"):
                    val = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
        Prints details of the class
        """
        return "[{0}] ({1}) {2}".format(
                self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """
        updates the public instance attribute updated_at with current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of instance
        """
        model = self.__dict__.copy()
        model["__class__"] = self.__class__.__name__
        model["created_at"] = self.created_at.isoformat()
        model["updated_at"] = self.updated_at.isoformat()

        return model

