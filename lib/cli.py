#!/usr/bin/env python3


from db.models import Vacation, Traveler, Domicile
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class CLI():
    engine = create_engine("sqlite:///lib/db/project.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    domiciles = session.query(Domicile).all()
    # what does this return?

    travelers = [traveler for traveler in session.query(Traveler)]
    # what does this format return?

    vacations = session.query(Vacation).all()

    def __init__(self, user_fn, user_ln, user_city):
        self.first_name = user_fn
        self.last_name = user_ln
        self.city = user_city
        self.start()

    @property
    def traveler(self):
        for t in CLI.travelers:
            if t.first_name == self.first_name and t.last_name == self.last_name:
                return t
            
        new_traveler = Traveler(self.first_name, self.last_name, self.city)
        session.add(new_traveler)
        session.commit()
        return new_traveler
    
    def start(self, book, view, browse):
        print('')
        print('WELCOME TO FLATS AFTER FLATIRON!')
        print('')

        exit = False

        while exit == False:
            choice = input("What would you like to do? Type 'B' to book a vacation, Type 'V' to view your Vacations, or Type 'N' to browse ")
            print('')

            if choice.lower() == 'b':
                pass
            elif choice.lower() == 'v':
                pass
            elif choice.lower() == 'n':
                browse()


    def browse(self):
        user_action = input("Type D to see a list of Domiciles, V to see a list of vacations booked: ")
        print(' ')

        if user_action == 'D' or user_action == 'd':
            print(f"Property Type:{d.property_type}, Location: {d.dest_location}" for d in CLI.domiciles)
        elif user_action == 'V' or user_action == 'v':
            pass



if __name__ == '__main__':
    
    user_fn = input("Enter Your First Name: ")
    user_ln = input("Enter Your Last Name: ")
    user_city = input("Enter Your City Name: ")
    CLI(user_fn, user_ln, user_city)
