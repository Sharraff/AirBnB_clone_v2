#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from datetime import datetime
import models
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from os import environ

storage_engine = environ.get("HBNB_TYPE_STORAGE")

if (storage_engine == "db"):
    Base = declarative_base()
else:
    Base = object


class BaseModel():
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if kwargs:
            for key in kwargs:
                if key == "__class__":
                    continue
                elif key in ("created_at", "updated_at"):
                    iso = "%Y-%m-%dT%H:%M:%S.%f"
                    setattr(self, key, datetime.strptime(kwargs[key], iso))
                else:
                    setattr(self, key, kwargs[key])
                self.id = str(uuid4())
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        custom = self.__dict__.copy()
        custom_dict = {}
        custom_dict.update({"__class__": self.__class__.__name__})
        for key in list(custom):
            if key in ("created_at", "updated_at"):
                custom_dict.update({key: getattr(self, key).isoformat()})
            elif key == "_sa_instance_state":
                custom.pop(key)
            else:
                custom_dict.update({key: getattr(self, key)})
        return custom_dict
    
    def delete(self):
        """
        delete the current instance from the storage
        """
        k = "{}.{}".format(type(self).__name__, self.id)
        del models.storage.__objects[k]