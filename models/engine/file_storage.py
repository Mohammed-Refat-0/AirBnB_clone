#!/usr/bin/python3

from models.base_model import BaseModel
from models.user import User
import json
import os


class FileStorage:

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):

        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        instance_to_json_dict = {}
        with open(self.__file_path, 'w') as FILE:
            for i in self.__objects:
                instance_to_json_dict[i] = self.__objects[i].to_dict()
            json.dump(instance_to_json_dict, FILE)

    def reload(self):

        if os.path.exists(self.__file_path):

            with open(self.__file_path, 'r') as FILE:

                json_to_instance_dict = json.load(FILE)
                for I, J in json_to_instance_dict.items():
                    class_name = J["__class__"]
                    del J["__class__"]
                    new_obj = eval(class_name)(**J)
                    self.new(new_obj)
        else:

            pass
