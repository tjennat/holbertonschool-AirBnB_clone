#!/usr/bin/python3
"""This is going to be my class for USER"""

from models.base_model import BaseModel


class User(BaseModel):
    """This is the User class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
