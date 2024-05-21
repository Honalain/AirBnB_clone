#!/usr/bin/python3
"""
Module file_storage serializes and
deserializes JSON types
"""
import os
import uuid
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from datetime import datetime


class FileStorage:
    """
    Custom class for file storage
    """

    __file_path = "file.json"
    __objects = {}
    classes = {"BaseModel": BaseModel, "User": User, "Place": Place}
    def all(self):
        """
        Returns dictionary representation of all objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the object with the key
        <object class name>.id
        Args:object(obj): object to write
        """
        objnm = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(objnm, obj.id)] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        (path: file_path)
        """
        obj2dict = FileStorage.__objects
        objdict = {obj: obj2dict[obj].to_dict() for obj in obj2dict.keys()}
        objdict = {}
        for key, obj in self.__objects.items():
            obj2dict[key] = obj.to_dict()
        def convert(obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(objdict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects, if the JSON
        file exists, otherwise do nothing at all.
        """
        try:
            if os.path.exists(self.__file_path):
                with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                    objdict = json.load(f)
                    for key, value in objdict.items():
                        if 'created_at' in value:
                            value['created_at'] = datetime.fromisoformat(value['created_at'])
                        if 'updated_at' in value:
                            value['updated_at'] = datetime.fromisoformat(value['updated_at'])
                        self.__objects[key] = self.classes[value["__class__"]](**value)
                        cls = value["__class__"]
                        del value["__class__"]
                        self.new(eval(cls)(**value))
        except json.JSONDecodeError as e:
            return
