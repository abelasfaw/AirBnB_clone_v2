#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import environ
from uuid import uuid4


st = "HBNB_TYPE_STORAGE"
if st in environ.keys() and environ["HBNB_TYPE_STORAGE"] == "db":
    class Review(BaseModel, Base):
        """class for review model"""
        __tablename__ = "reviews"
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

        def __init__(self, **kwargs):
            setattr(self, "id", str(uuid4()))
            for i, j in kwargs.items():
                setattr(self, i, j)
else:
    class Review(BaseModel):
        """class for review model"""
        place_id = ""
        user_id = ""
        text = ""
