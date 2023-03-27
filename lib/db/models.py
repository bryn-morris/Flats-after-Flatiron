from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer, DateTime, ForeignKey)
from sqlalchemy.orm import relationship, backref, sessionmaker

# Choose from list of options  - user input

# Traveler —--<Vacation> —--- Domicile

Base = declarative_base()
Engine = create_engine("sqlite:///project.db")

class Traveler(Base):
    
    __tablename__ = 'Travelers'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer(), primary_key = True)
    first_name = Column(String())
    last_name = Column(String())
    location = Column(String())

    def __repr__(self):
        return f"id = {self.id}," \
                + f"name = {self.first_name} {self.last_name}," \
                + f"location = {self.location}"
    
class Domicile(Base):
    
    __tablename__ = 'Domiciles'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer(), primary_key = True)
    dest_location = Column(String())
    # Ideally, use a list or some sort of other data structure
    sleep_capacity = Column(Integer())
    # Ideally, use a list or some sort of other data structure
    local_amenities = Column(String())
    # Stretch Goal
    # price = Column(Integer())
    property_type = Column(String())
    
    # Avaliabilty as a method?

    def __repr__(self):
        return f"id = {self.id}," \
            + f"dest_location = {self.dest_location}," \
            + f"sleep_capacity = {self.sleep_capacity}," \
            + f"local_amenities = {self.local_amenities}," \
            + f"property_type = {self.property_type}"

class Vacation(Base):
    
    __tablename__ = 'Vacations'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer(), primary_key = True)
    start_date = Column(DateTime())
    end_date = Column(DateTime())
    Traveler_id = Column(Integer(),ForeignKey('Travelers.id', name = "t-id_constraint"))
    Domicile_id = Column(Integer(),ForeignKey('Domiciles.id', name = "d-id constraint"))

    traveler = relationship('Travelers', backref=backref("travelers"))
    lodging = relationship('Domicile', backref=backref("lodgings"))

    def __repr__(self):
        return f"id = {self.id}," \
            + f"start_date = {self.start_date}" \
            + f"end_date = {self.end_date}" \
            + f"Traveler_id = {self.Traveler_id}" \
            + f"Domicile_id = {self.Domicile_id}"


