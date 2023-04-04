"""
This module is used to test the class BaseModel
"""
import unittest
from models.base_model import BaseModel
import uuid
from datetime import datetime

class BaseModelTest(unittest.TestCase):
    """
    This is the test class that contains one or more tests methods
    It is here that we will group related tests together for easier organization
    """

    def setUp(self):
        """
        This method is used to create an instance of BaseModel that we will be using
        to test our test cases. Everytime we call a test case method we will use the instance
        """
        self.model = BaseModel()

    def test_id_type(self):
        """
        this method will be used to test the class type of id
        """
        self.assertIsInstance(self.model.id, str)

    def test_id_uniqueness(self):
        """
        use to check if indeed an id is unique
        """
        model2 = BaseModel()
        self.assertNotEqual(self.model.id, model2.id)

    def test_created_at_type(self):
        """
        Test the type of class that created_at instance attribute
        belongs to
        """
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_type(self):
        """
        will be used to test the class that updated_at instance attribute
        belongs to
        """
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_method(self):
        """
        test that indeed the __str__ method returns a string representation of
        ModelBase instance
        """
        expected_output = "[BaseModel] ({}) {}".format(self.model.id, self.model, __dict__)
        self.assertEqual(str(self.model), expected_output)

    def test_save(self):
        """
        used to test that indeed time is updated in the updated_at attribute
        when the save method is called by an instance
        """
        old_updated_at = self.model.updated_at
        self.model.save()
        new_updated_at = self.model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        """
        test that indeed the string representation of the instance is turned
        to a dictionary
        """
        expected_dict = {
                'id': self.model.id,
                'created_at': self.model.created_at.isoformat(),
                'updated_at': self.model.updated_at.isoformat(),
                '__class__': 'BaseModle'
                }
        self.assertDictEqual(self.model.to_dict(), expected_dict)



