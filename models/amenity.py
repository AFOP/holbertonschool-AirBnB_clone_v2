#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship
from os import getenv

class Amenity(BaseModel, Base):
    """ State Amenity """
    __tablename__ = 'amenities'
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        name = Column(String(128), nullable=False)
        # place_amenities = relationship('Place', backref='amenities', secondary='place_amenity')
    else:
        name = ""
