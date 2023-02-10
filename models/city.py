#!/usr/bin/python3

"""
City model that inherits from the BaseModel class
"""


import models
from models.base_model import BaseModel


class City(BaseModel):
	"""
	City model that inherits from Basemodel class
	"""
	state_id = ""
	name = ""
