#!/usr/bin/python3
"""This is going to be my class for review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """This is the Review class"""
    place_id = ""
    user_id = ""
    text = ""
