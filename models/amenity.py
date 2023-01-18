#!/usr/bin/python3
""" Amenty Module for HBNB project """
from models.base_model import BaseModel, Base
from os import environ
from sqlalchemy import Column, String, DateTime

storage = "HBNB_TYPE_STORAGE"
if storage in environ.keys() and environ["HBNB_TYPE_STORAGE"] == "db":
    class Amenity(BaseModel, Base):
        """classs for amenty model"""
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        def __init__(self, **kwargs):
            setattr(self, "id", str(uuid4()))
            for k, v in kwargs.items():
                setattr(self, k, v)
else:
    class Amenity(BaseModel):
        """class fro amenty model"""
        name = ""
