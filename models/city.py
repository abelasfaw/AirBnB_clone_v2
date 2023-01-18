#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from os import environ
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from uuid import uuid4

st = "HBNB_TYPE_STORAGE"
if st in environ.keys() and environ["HBNB_TYPE_STORAGE"] == "db":
    class City(BaseModel, Base):
        """class for city model"""
        __tablename__ = "cities"
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities", cascade="all,delete")
        
        def __init__(self, **kwargs):
            setattr(self, "id", str(uuid4()))
            for i, j in kwargs.items():
                setattr(self, i, j)
else:
    class City(BaseModel):
        """ The city class, contains state ID and name """
        state_id = ""
        name = ""
