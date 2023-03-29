#!/usr/bin/env python3

import ipdb
from db.models import Vacation, Traveler, Domicile
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime

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
        self.traveler() 
        self.start()

    def traveler(self):
        for t in CLI.travelers:
            if t.first_name == self.first_name and t.last_name == self.last_name and t.location == self.city:
                self.trav_obj= t
                return None
            
        new_traveler = Traveler(self.first_name, self.last_name, self.city)
        session.add(new_traveler)
        session.commit()
        self.trav_obj = new_traveler
    
    def start(self):
        print('')
        print(f'WELCOME TO FLATS AFTER FLATIRON, {self.trav_obj.first_name}!')
        print('')

        exit = False

        while exit == False:
            choice = input("What would you like to do? Type 'B' to book a vacation, Type 'V' to view/update your Vacations, or Type 'N' to browse all properties: ")
            print('')

            if choice.lower() == 'b':
                self.book()
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
        
    def book(self):
# add loop functionality to continue prompting for dates
        date_format = '%Y-%m-%d'
        start_date = input("When would you like your vacation to start? ")
        try:
            startDate = datetime.datetime.strptime(start_date, date_format).date()
            print(f"Here is your start date: {startDate}")
        except ValueError:
            print('Please enter a valid date!')

        end_date = input("When would you like your vacation to end? ")

        try:
            endDate = datetime.datetime.strptime(end_date, date_format).date()
            print(f"Here is your end date: {endDate}")
        except ValueError:
            print('Please enter a valid date!')

        filtered_domiciles = []
        for d in CLI.domiciles:
            vcount = 0
            for v in d.vacations:
                if (startDate < v.start_date):
                    if (endDate < v.start_date):
                        vcount += 1
                elif (endDate > v.end_date):
                    if(startDate > v.end_date):
                        vcount += 1
            if vcount == len(d.vacations):
                filtered_domiciles.append(d)

        print('Here are the available domiciles: ')
        for i, d in enumerate(filtered_domiciles):
            print(f'{i + 1}. {d.property_type}')

        propID = input('Would you like to see the details of a property to book? Please enter one of the numbers above: ')

        if int(propID) in range(1, len(filtered_domiciles)+1):
            dp = filtered_domiciles[int(propID) - 1]
            print('** Property Details **')
            print(f"Property Type: {dp.property_type}")
            print(f"Location: {dp.dest_location}")
            print(f"Sleeping Capacity: {dp.sleep_capacity}")
            print(f"Local Amenities: {dp.local_amenities}")

            book_prop = input('Would you like to book this property(y/n)? ')
# Add functionality if user says no (return to domicile list)
# Add functionality to kick user back to main menu
            if book_prop == 'y' or book_prop == 'Y':
                session.add(Vacation(startDate, endDate, self.trav_obj.id, dp.id))
                session.commit()
                print('Congrats! Your vacation is booked!')


if __name__ == '__main__':
    
    user_fn = input("Enter Your First Name: ")
    user_ln = input("Enter Your Last Name: ")
    user_city = input("Enter Your City Name: ")
    CLI(user_fn, user_ln, user_city)


ipdb.set_trace()