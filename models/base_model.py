#!/usr/bin/python3
""" defines the class "BaseModel"""

import models
import datetime
import uuid


class BaseModel:
    """BaseModel, From which all other classes inherit from in this project
    Attributes:
        id (string): The id of the object
        created_at (datetime): The date and time when the object was created
        updated_at (datetime): The datetime object for when it was last updated
    """

    id = None
    created_at = None
    updated_at = None

    def __init__(self, **kwargs):
        """constructor for the class
        Args:
            **kwargs (dict, optional): contain the attributes name and values
            to initialize or update the instance
        """

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
        """defines the __str__ method (print()) of the object
        Returns:
            __str__ representation of the object
        """

        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """transform the class attributes
        to a dictionary representation of the object

        Returns:
            object_dict: dictionary representation of the object
        """
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
