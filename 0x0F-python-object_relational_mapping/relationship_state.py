#!/usr/bin/python3
"""state model"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    """
    State class sup calss from Base
    ORM first try :D

    Attributes:
        id: id that will be asigned from the sql
        name: name of the state
    """

    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade='all, delete')
