#!/usr/bin/python3
"""Defines unittests for BaseModel."""
import os
import models
import unittest
import datetime
import uuid
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittests for testing the BaseModel class."""

    def test_name_class(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_instance_type(self):
        self.assertIsInstance(BaseModel(), BaseModel)

    def test_datetime(self):
        new_instance = BaseModel()
        new_instance.save()
        self.assertIsInstance(new_instance.created_at, datetime.datetime)
        self.assertNotEqual(new_instance.updated_at,
                            new_instance.created_at)

    def test_id(self):
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_to_dict(self):
        instance3 = BaseModel()
        with self.assertRaises(TypeError):
            instance3.to_dict(None)


if __name__ == "__main__":
    unittest.main()
