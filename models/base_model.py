#!/usr/bin/python3
"""
class BaseModel
defines all common attributes/methods for other classes
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    defines all common attributes/methods
    """
    def __init__(self, *args, **kwargs):
        """
        *args, **kwargs arguments for the constructor of a BaseModel.

        if kwargs is not empty:
        - each key of this dictionary is an attribute name
        otherwise:
        id and create_at make new instance

        """
        if len(kwargs) > 0:
            for key in kwargs:
                if key == "__class__":
                    continue
                if key == "created_at":
                    kwargs[key] = datetime.strptime(
                        kwargs[key], '%Y-%m-%dT%H:%M:%S.%f')
                if key == "updated_at":
                    kwargs[key] = datetime.strptime(
                        kwargs[key], '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)  # REVISAR QUE SUCEDE

    def __str__(self):
        """
        (magic method)
        Returns:
            [dict]: return dictionary format to print
        """
        return ("[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        update the current time in 'update_at'
        """
        self.updated_at = datetime.now()
        models.storage.save()  # REVISAR METODO

    def to_dict(self):
        """
        make a copy and add new data to the dictionary
        ('create_at', 'update_at')

        Returns:
            [dict]: return the new dictionary.
        """
        copy_dict = self.__dict__.copy()
        copy_dict["__class__"] = self.__class__.__name__
        copy_dict["created_at"] = self.created_at.isoformat()
        copy_dict["updated_at"] = self.updated_at.isoformat()
        return copy_dict
