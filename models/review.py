#!/usr/bin/python3

"""
Review model that inherits from the BaseModel class
"""


import models
from models.base_model import BaseModel


class Review(BaseModel):
	"""
	Review model that inherits from Basemodel class
	"""
	place_id = ''
	user_id = ''
	text = ''
