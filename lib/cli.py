#!/usr/bin/env python3

import ipdb
from db.models import Vacation, Traveler, Domicile
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///lib/db/project.db")
Session = sessionmaker(bind=engine)
session = Session()

class CLI():
    
    domiciles = session.query(Domicile).all()
    # what does this return?

    travelers = [traveler for traveler in session.query(Traveler)]
    # what does this format return?

    vacations = session.query(Vacation).all()

    def __init__(self, user_fn, user_ln, user_city):
        self.first_name = user_fn
        self.last_name = user_ln
        self.city = user_city
        self.traveler 
        self.start()

    def traveler(self):
        for t in CLI.travelers:
            if t.first_name == self.first_name and t.last_name == self.last_name:
                self._traveler = t
            
        new_traveler = Traveler(self.first_name, self.last_name, self.city)
        session.add(new_traveler)
        print('test')
        session.commit()
        self.trav_obj = new_traveler
    
    def start(self):
        print('')
        print('WELCOME TO FLATS AFTER FLATIRON!')
        print('')

        exit = False

        while exit == False:
            choice = input("What would you like to do? Type 'B' to book a vacation, Type 'V' to view/update your Vacations, or Type 'N' to browse all properties: ")
            print('')

            if choice.lower() == 'b':
                pass
            elif choice.lower() == 'v':
                pass
            elif choice.lower() == 'n':
                self.browse()

            print(' ')
            user_input = input("Would you like to stop now? (Type Y/N): ")
            print(' ')
            if user_input == "Y" or user_input == 'y':
                exit = True

     
    def browse(self):
        print('')
        print('** Properties **')
        print('')

        for i, d in enumerate(CLI.domiciles):
            print(f'{i + 1}. Property Type: {d.property_type}, Location: {d.dest_location}')

        detailPropID = input('If you would like to see the details of a property please enter the number of the property in the list: ')

        if int(detailPropID) in range(1, len(CLI.domiciles) + 1):
            dp = CLI.domiciles[int(detailPropID) - 1]
            print('** Property Details **')
            print(f"Property Type: {dp.property_type}")
            print(f"Location: {dp.dest_location}")
            print(f"Sleeping Capacity: {dp.sleep_capacity}")
            print(f"Local Amenities: {dp.local_amenities}")

            viewPastBookings = input('Would you like to see the past bookings of this property? (y/n): ')

            if viewPastBookings == 'Y' or viewPastBookings == 'y':
                pastVacations = [v for v in CLI.vacations if v.Domicile_id  == dp.id]
                for v in pastVacations:
                    print(v)
            


if __name__ == '__main__':
    
    user_fn = input("Enter Your First Name: ")
    user_ln = input("Enter Your Last Name: ")
    user_city = input("Enter Your City Name: ")
    CLI(user_fn, user_ln, user_city)


ipdb.set_trace()