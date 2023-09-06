#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv
from models.base_model import BaseModel
from models.city import City
from models.review import Review
from models.state import State
from models.user import User
from models.place import Place
from models.amenity import Amenity


HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')

dummy_classes = {"BaseModel": BaseModel, "User": User,
                 "Review": Review, "City": City,
                 "State": State, "Place": Place,
                 "Amenity": Amenity}

dummy_tables = {"states": State, "cities": City,
                "users": User, "places": Place,
                "reviews": Review, "amenities": Amenity}

if HBNB_TYPE_STORAGE == 'db':
    from .engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from .engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()