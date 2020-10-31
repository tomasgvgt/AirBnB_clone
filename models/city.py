#!/usr/bin/python3
"""new class inherit from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Empty name public attribute
    """
    state_id = ""
    name = ""
