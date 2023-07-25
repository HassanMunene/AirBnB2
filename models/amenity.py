#!/usr/bin/python3
"""
Amenity Module for HBNB project
"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """
    Will be mapped to amenities table
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity, viewonly=False, back_populates="amenities")
