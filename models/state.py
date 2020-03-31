#!/usr/bin/python3
"""This is the state class"""
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, City


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input nameOB
    """
    name = Column(String(128), nullable=False)
    __tablename__ = 'states'
    cities = relationship('City', cascase='delete', backref='state')

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        """returns City instances with state_id"""
        @property
        def cities(self):
            return [value for key, value in storage.all(City).items()
                    if value.state_id == self.id]
