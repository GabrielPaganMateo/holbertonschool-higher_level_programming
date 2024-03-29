#!/usr/bin/python3
"""
Class State with instance of Base
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Class that defines a State object
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement="auto",
                unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
