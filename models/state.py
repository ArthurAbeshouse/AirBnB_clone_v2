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
        name: input name
    """
    name = ""
