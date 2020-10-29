#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
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

    def __str__(self):
        return ("[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        copy_dict = self.__dict__.copy()
        copy_dict["__class__"] = self.__class__.__name__
        copy_dict["created_at"] = self.created_at.isoformat()
        copy_dict["updated_at"] = self.updated_at.isoformat()
        return copy_dict
