#!/usr/bin/python3
"""This is the state class"""
from os import getenv
from models import storage
from models.city import City
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship(City, backref="state",
                              cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            '''
            City list for FileStorage
            '''
            cities_by_state = []
            for city in storage.all('City').values():
                if city.state_id == self.id:
                    cities_by_state.append(city)
            return cities_by_state
