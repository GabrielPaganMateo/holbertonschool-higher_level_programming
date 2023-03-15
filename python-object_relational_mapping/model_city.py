#!/usr/bin/python3
"""
Contains the class definition
of a city
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import State
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """
    Class that defines a City object
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement="auto",
                unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
