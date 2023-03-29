from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from datetime import datetime,date, timedelta
import random

from db.models import (Base, Vacation, Traveler, Domicile)

if __name__ == '__main__':

    engine = create_engine("sqlite:///lib/db/project.db")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    faker = Faker()
    

    import ipdb; ipdb.set_trace()

