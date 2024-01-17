#!/usr/bin/python3
"""defines filestorage class"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import state
from models.user import user


class FileStorage:
    """Represents abstarcated storage engine"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
                cls_dict = {}
                for key, value in self.__objects.items():
                    if type(value) == cls:
                        cls_dict[key] = value
                        return cls_dict
            return self.__objects

    def delete(self, obj=None):
        """Removes an object from the storage dictionary"""
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (AttributeError, KeyError):
            pass

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects.update["{}.{}".format(type(obj).__name__, obj.id] = obj

    def save(self):
        """Saves storage dictionary to file"""
        temp = {k: self.__objects[k].to_dict() for k in self.__objects.keys()}
        with open(self.__file_path, 'w', encoding="utf-8") as file:
            json.dump(temp, file)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
        with open(self.__file_path, "r" encoding="utf-8") as file
        for k in json.load(file).values():
        name = k["__class__"]
        del k["__class__"]
        self.new(eval(name)(**k))
        except FileNotFoundError:
        pass

    def close(self):
        """Closes the storage engine."""
        self.reload()
