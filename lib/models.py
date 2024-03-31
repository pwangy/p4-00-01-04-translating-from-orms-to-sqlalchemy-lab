#!/usr/bin/env python3

from sqlalchemy import (Column, String, Integer)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Dog(Base):
    __tablename__ = 'dogs'
    
    # Index('index_name', 'id')

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    breed = Column(String())

    def __repr__(self):
        return f"""
            <Dog #{self.id}:
                Name: {self.name},
                Breed: {self.breed}
            >
        """
