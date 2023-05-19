from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy import create_engine
from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer, Date, ForeignKey)
from sqlalchemy.orm import relationship, backref

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

    def __repr__(self):
        return f"id = {self.id}," \
                + f"name = {self.first_name} {self.last_name}," \
                + f"location = {self.location}"
    
    vacations = relationship("Vacation", backref = "traveler")
    domiciles = association_proxy("vacations", "domicile",
                                  creator = lambda dm: Vacation(domicile = dm))

class Domicile(Base):
    
    __tablename__ = 'Domiciles'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer(), primary_key = True)
    name = Column(String())
    dest_location = Column(String())
    sleep_capacity = Column(Integer())
    local_amenities = Column(String())
    # Stretch Goal
    # price = Column(Integer())
    property_type = Column(String())

    def __repr__(self):
        return f"id = {self.id}," \
            + f"name = {self.name}," \
            + f"dest_location = {self.dest_location}," \
            + f"sleep_capacity = {self.sleep_capacity}," \
            + f"local_amenities = {self.local_amenities}," \
            + f"property_type = {self.property_type}"
    
    vacations = relationship("Vacation", backref = "domicile")
    travelers = association_proxy("vacations", "traveler",
                                  creator = lambda tr: Vacation(traveler = tr))


class Vacation(Base):
    
    __tablename__ = 'Vacations'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer(), primary_key = True)
    start_date = Column(Date())
    end_date = Column(Date())
    Traveler_id = Column(Integer(),ForeignKey('Travelers.id'))
    Domicile_id = Column(Integer(),ForeignKey('Domiciles.id'))
    rsn_for_visit = Column(String())

    def __repr__(self):
        return f"id = {self.id}," \
            + f"start_date = {self.start_date}" \
            + f"end_date = {self.end_date}" \
            + f"Traveler_id = {self.Traveler_id}" \
            + f"Domicile_id = {self.Domicile_id}" \
            + f"rsn_for_visit = {self.rsn_for_visit}"
    
if __name__ == "__main__":
    Engine = create_engine("sqlite:///lib/db/project.db")
    Base.metadata.create_all(Engine)
