#!/usr/bin/python3
"""
This module contains the class DBStorage
"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {
    'City': City,
    'State': State,
    'User': User,
    'Place': Place,
    'Review': Review,
    'Amenity': Amenity
}

class DBStorage:
    """
    new storage system that deals with MySQL database
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        will be automatically configured when
        an instance of this storage in created
        """
        USER = getenv("HBNB_MYSQL_USER")
        PWD = getenv("HBNB_MYSQL_PWD")
        HOST = getenv("HBNB_MYSQL_HOST")
        DB = getenv("HBNB_MYSQL_DB")
        ENV = getenv("HBNB_ENV")

        # set up sqlalchemy engine for connecting to mysql database
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(USER, PWD, HOST, DB), pool_pre_ping=True)

        if ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        return a dictionary of atrributes depending on arg passes
        """
        if cls is not None:
            objs = self.__session.query(classes[cls]).all()
        else:
            objs = []
            for cls in classes.values():
                objs += self.__session.query(cls).all()

        a_dict = {}
        for obj in objs:
            k = "{}.{}".format(type(obj).__name__, obj.id)
            a_dict[k] = obj
            if '_sa_instance_state' in a_dict:
                del a_dict["_sa_instance_state"]
        return a_dict


    def new(self, obj):
        """
        add an object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        commit all the changes to the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete an object from the current db session
        """
        if obj is not None:
            self.__session.delete(obj)
            self.__session.commit()


    def get(self, cls_name, id):
        """
        retreive an object from the database based on class name id
        to do the destroy in the console but not still working
        kindly ignore this method
        """
        cls_obj = getattr(models, cls_name, None)
        if cls_obj:
            obj = self.__session.query(cls_obj).get(id)
            return obj
        else:
            return None

    def reload(self):
        """
        create all tables in the database using sqlalchemy
        all classes that inherit from Base must be imported before this
        Base.metadata.create_all(engine)
        create the current database session(self.__session)
        use scoped_session to make sure that session is thread-safe
        """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()
