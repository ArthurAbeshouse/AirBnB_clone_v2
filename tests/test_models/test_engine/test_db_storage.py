#!/usr/bin/python3
"""tests database storage"""
import MySQLdb
import os
import unittest
import pep8
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage


class TestDBStorage (unittest.TestCae):
    """this will test DBStorage"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.user = User()
        cls.user.first_name = "Kev"
        cls.user.last_name = "Yo"
        cls.user.email = "1234@yahoo.com"
        cls.storage = DBStorage()

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down."""
        del cls.user

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != "db",
                     "db isn't being used")

    def test_all(self):
        """tests all in File Storage"""
        storage = DBStorage()
        storage.reload()
        len_of_dict = len(storage.all())
        state = State(name="test_all_state")
        state.save()
        storage.save()
        self.assertsIs(len(storage.all()), len_of_dict + 1)

def test_pep8_dbstorage(self):
        """Testing the pep8 linter requirments."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found pep8 style errors (Please review warnings).")
