#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import os
import json
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy import create_engine


class DBStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __engine = None
    __session = None

    def __init__(self):
        """Public instance methods."""

        # create engine and it must be linked to the MySQL database
        # Dialect: mysql + Driver: mysqldb
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}" .format(
                os.getenv("HBNB_MYSQL_USER"),
                os.getenv("HBNB_MYSQL_PWD"),
                os.getenv("HBNB_MYSQL_HOST"),
                os.getenv("HBNB_MYSQL_DB"),
                pool_pre_ping=True))

        # drop all tables if the environment HBNB_ENV is equal to test
        if os.getenv("HBNB_ENV") is "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session."""
        """All objects will depend on the class name (argument cls)."""
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        NewObjectDictionary = {}
        QueryObjects = [User, State, City, Amenity, Place, Review]
        if cls is None:
            for Object in QueryObjects:
                QueryValues = self.__session.query(Object).all()
                for values in QueryValues:
                    key = values.__class__.__name__ + '.' + values.id
                    NewObjectDictionary[key] = values

    def new(self, obj):
        """Add the object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """If obj is not None Delete from the current database session."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Recreate all tables in the database."""
        Base.metadata.create_all(self.__engine)
        CurrentDatabaseSession = sessionmaker(self.__engine,
                                              expire_on_commit=False)
        Session = scoped_session(CurrentDatabaseSession)
        self.__session = Session()
