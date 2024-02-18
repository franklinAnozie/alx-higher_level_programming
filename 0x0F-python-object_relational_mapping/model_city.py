#!/usr/bin/python3
"""city model"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


Base = declarative_base()


class City(Base):
    """
    City class from Base

    Attributes:
        id: id that will be asigned
        name: name of the city
        state: state city is located
    """

    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
