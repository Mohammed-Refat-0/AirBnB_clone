#!/usr/bin/python3
"""defines the class "FileStorage" """

from models.base_model import BaseModel
from models.user import User
import json
import os


class FileStorage:
    """FileStorage class implementation

    Attributes:
    __file_path (string): The path of the file to store and reload
    json representation of objects
    __objects (dict): dictionary of objects"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Return the dictionary of all saved objects"""
        return self.__objects

    def new(self, obj):
        """Add a new object to the dictionary
        Args:
        obj (object): The object to add to the dictionary"""
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """save the dictionary to file in json format"""
        instance_to_json_dict = {}
        with open(self.__file_path, 'w') as FILE:
            for i in self.__objects:
                instance_to_json_dict[i] = self.__objects[i].to_dict()
            json.dump(instance_to_json_dict, FILE)

    def reload(self):
        """reload the saved instances from json file to the namespace"""

        if os.path.exists(self.__file_path):

            with open(self.__file_path, 'r') as FILE:

                json_to_instance_dict = json.load(FILE)
                for key, J in json_to_instance_dict.items():
                    class_name = J["__class__"]
                    del J["__class__"]
                    new_obj = eval(class_name)(**J)
                    self.nsew(new_obj)
        else:

            pass
