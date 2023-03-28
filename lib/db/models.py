from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer, Date, ForeignKey)
from sqlalchemy.orm import relationship, backref, sessionmaker

# Choose from list of options  - user input

# Traveler —--<Vacation> —--- Domicile
Base = declarative_base()

class Traveler(Base):
    
    __tablename__ = 'Travelers'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer(), primary_key = True)
    first_name = Column(String())
    last_name = Column(String())
    location = Column(String())

    def __init__(self, user_fn, user_ln, user_city):
        self.first_name = user_fn
        self.last_name = user_ln
        self.location = user_city

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
    
    def __init__(self, dest_location, sleep_capacity, local_amenities, property_type):
        self.dest_location = dest_location
        self.sleep_capacity = sleep_capacity
        self.local_amenities = local_amenities
        self.property_type = property_type

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
    start_date = Column(Date())
    end_date = Column(Date())
    Traveler_id = Column(Integer(),ForeignKey('Travelers.id', name = "t-id_constraint"))
    Domicile_id = Column(Integer(),ForeignKey('Domiciles.id', name = "d-id constraint"))

    traveler = relationship('Traveler', backref=backref("traveler"))
    lodging = relationship('Domicile', backref=backref("lodging"))

    def __init__(self, start_date, end_date, Traveler_id, Domicile_id):
        self.start_date = start_date
        self.end_date = end_date
        self.Traveler_id = Traveler_id
        self.Domicile_id = Domicile_id


    def __repr__(self):
        return f"id = {self.id}," \
            + f"start_date = {self.start_date}" \
            + f"end_date = {self.end_date}" \
            + f"Traveler_id = {self.Traveler_id}" \
            + f"Domicile_id = {self.Domicile_id}"
    
if __name__ == "__main__":
    Engine = create_engine("sqlite:///lib/db/project.db")
    Base.metadata.create_all(Engine)
