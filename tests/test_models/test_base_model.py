#!/usr/bin/python3
"""Unittest for base_model.py"""
import unittest
import uuid
import datetime

from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Tests Base Model class."""
    def test_save(self):
        """Test save()"""
        my_model = BaseModel()
        my_model.save()
        self.assertNotEqual(my_model.created_at, my_model.updated_at)

    def test_to_dict(self):
        """Test to_dict()"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        self.assertEqual(my_model_json["id"], my_model.id)
        self.assertEqual(my_model_json["created_at"], my_model.created_at.isoformat())
        
    def test__str__(self):
        """Test __str__()"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        self.assertEqual(str(my_model), "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__))

    def test_init(self):
        """Test __init__()"""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime.datetime)
        self.assertIsInstance(my_model.updated_at, datetime.datetime)
        self.assertEqual(my_model.created_at, my_model.updated_at)

if __name__ == "__main__":
    unittest.main()