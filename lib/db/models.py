from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer)

# Choose from list of options  - user input

# Traveler —--<Vacation> —--- Domicile

Base = declarative_base()
Engine = create_engine("sqlite:///project.db")

class Travelers(Base):
    
    __tablename__ = 'students'

class Domicile(Base):
    
    __tablename__ = 'Domicile'

class Vacation(Base):
    
    __tablename__ = 'Vacation'
