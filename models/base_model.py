#!/usr/bin/python3

import models
import datetime
import uuid


class BaseModel:

    id = None
    created_at = None
    updated_at = None

    def __init__(self, **kwargs):

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'created_at':
                    self.__dict__[key] = datetime.datetime.strptime(
                        kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'updated_at':
                    self.updated_at = datetime.datetime.strptime(
                        kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.__dict__[key] = value
        else:
            self.id = uuid.uuid4().__str__()
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):

        return '[{}] ({}) {}'.format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        object_dict = self.__dict__.copy()
        object_dict['__class__'] = self.__class__.__name__
        object_dict['created_at'] = object_dict['created_at'].isoformat()
        object_dict['updated_at'] = object_dict['updated_at'].isoformat()
        return object_dict

    # @property
    # def name(self):
    #     return self._name

    # @name.setter
    # def name(self, str_name):
    #     self._name = str_name

    # @property
    # def number(self):
    #     return self._number

    # @number.setter
    # def number(self, int_number):
    #     self._number = int_number
