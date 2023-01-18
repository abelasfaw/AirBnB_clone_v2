#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from os import environ

st = "HBNB_TYPE_STORAGE"
if st in environ.keys() and environ["HBNB_TYPE_STORAGE"] == "db":
    class User(BaseModel, Base):
        """class for user model"""
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
        def __init__(self, **kwargs):
            setattr(self, "id", str(uuid4()))
            for i, j in kwargs.items():
                setattr(self, i, j)

else:
    class User(BaseModel):
        """class for user model"""
        email = ""
        password = ""
        first_name = ""
        last_name = ""
