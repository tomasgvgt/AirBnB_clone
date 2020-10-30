#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = type(obj).__name__+"." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes the dictionary __objects into a JSON file
        """
        json_dict = {}
        for key, value in FileStorage.__objects.items():
            json_dict[key] = value.to_dict()  # convert each object into a dict
        with open(FileStorage.__file_path, "w") as f:
            json.dump(json_dict, f)

    def reload(self):
        class_obj = FileStorage.__objects[key]
        try:
            with open(FileStorage.__file_path, "r") as f:
                json_dict = json.load(f)
                for key, value in json_dict.items():
                    file_obj = eval(value["__class__"] + "(**value)")
        except Exception:
            pass
