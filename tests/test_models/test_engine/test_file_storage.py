#!/usr/bin/python3
'''
unittest module for module 'file_storage'
'''

import os
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorageInstantiation(unittest.TestCase):
    """
    Test the instantiation of the FileStorage class
    """
    def test_FileStorage_instantiation_with_arg(self):
        """
        Test that FileStorage can be instantiated with an argument
        """
        self.assertEqual(type(FileStorage(), FileStorage))

    def test_FileStorage_instantiation_with_arg(self):
        """
        Test that FileStorage can be instantiated with an argument
        Should raise TypeError
        """
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_instantializes(self):
        """
        Test that storage is initialized
        """
        self.assertEqual(type(models.storage), FileStorage)

class TestFileStorage(unittest.TestCase):
    """
    Test the FileStorage class
    """
    def setUp(self):
        """
        Set up the test
        """
        self.test_file = "test_file.json"

    def tearDown(self):
        """
        Tear down the test
        """ 
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_all_returns_dict(self):
        """
        Test that all returns a dictionary
        """
        self.assertEqual(type(models.storage.all()), dict)

    def test_new_creates_instance(self):
        """
        Test that new creates an instance
        """
        obj = BaseModel()
        models.storage.new(obj)
        self.assertIn("BaseModel.{}".format(obj.id), models.storage.all())

    def test_new_with_args(self):
        """
        Test that new raises TypeError with arguments
        """
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        """
        Test creating a new object with None (should raise AttributeError).
        """
        with self.assertRaises(AttributeError):
            models.storage.new(None) 

    def test_save_and_reload(self):
        """
        Test saving objects to a file and then reloading them
        """
        obj1 = BaseModel()
        obj2 = BaseModel()
        models.storage.new(obj1)
        models.storage.new(obj2)
        models.storage.save()
        # Create new storage instance to simulate reloading
        new_storage = FileStorage()
        new_storage.reload()

        # Check if the reloaded objects match the original objects
        self.assertTrue(new_storage.all().get("BaseModel.{}".format(obj1.id)) is not None)
        self.assertTrue(new_storage.all().get("BaseModel.{}".format(obj2.id)) is not None)
    def test_save_to_file(self):
        """
        Test saving objects to a file and check if the file is created
        """
        obj = BaseModel()
        models.storage.new(obj)
        models.storage.save()
        self.assertTrue(os.path.exists(models.storage.FileStorage.file_path))

    def test_reload_empty_file(self):
        """
        Test reloading when the file is empty or does not exist
        """

        with self.assertRaises(TypeError):
            models.storage()
            models.storage.reload()



if __name__ == '__main__':
    unittest.main()