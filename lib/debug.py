from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import (Base, Vacation, Traveler, Domicile)

if __name__ == '__main__':

    engine = create_engine("sqlite:///lib/db/project.db")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()


    

    import ipdb; ipdb.set_trace()
