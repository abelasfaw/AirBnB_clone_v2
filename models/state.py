#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models import *
from models.base_model import Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
			  cascade="all, delete, delete-orphan")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE', '') != 'db':
        @property
        def cities(self):
            all_cities = models.storage.all('city')
            temp = []
            for city_id in all_cities:
                if all_cities[city_id].state_id == self.id:
                    temp.append(all_cities[city_id])
            return temp
