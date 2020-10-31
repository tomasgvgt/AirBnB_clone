#!/usr/bin/python3
"""new class inherit from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Empty name public attribute
    """
    place_id = ""
    user_id = ""
    text = ""
