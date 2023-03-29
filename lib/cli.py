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

    travelers = [traveler for traveler in session.query(Traveler)]

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
        print(f'WELCOME TO FLATS AFTER FLATIRON, {self.trav_obj.first_name.upper()}!')
        print('')

        exit = False

        while exit == False:
            choice = input("What would you like to do? Type 'B' to book a vacation, Type 'V' to view your profile, or Type 'N' to browse all properties: ")
            print('')

            if choice.lower() == 'b':
                self.book()
            elif choice.lower() == 'v':
                self.view_update()
            elif choice.lower() == 'n':
                self.browse()

            print(' ')
            user_input = input("Would you like to stop now? (Type Y/N): ")
            print(' ')
            if user_input.lower() == 'y':
                exit = True

     
    def browse(self):
        print('')
        print('** Properties **')
        print('')

        for i, d in enumerate(CLI.domiciles):
            print(f'{i + 1}. Property Type: {d.property_type}, Location: {d.dest_location}')

        print("")
        detailPropID = input('If you would like to see the details of a property please enter the number of the property in the list: ')

        if int(detailPropID) in range(1, len(CLI.domiciles) + 1):
            dp = CLI.domiciles[int(detailPropID) - 1]
            print('** Property Details **')
            print(f"Property Type: {dp.property_type}")
            print(f"Location: {dp.dest_location}")
            print(f"Sleeping Capacity: {dp.sleep_capacity}")
            print(f"Local Amenities: {dp.local_amenities}")

            viewPastBookings = input('Would you like to see the past bookings of this property? (y/n): ')

# Need to make view past booking more readable, maybe print string with name and dates

            if viewPastBookings.lower() == 'y':
                pastVacations = [v for v in CLI.vacations if v.Domicile_id  == dp.id]
                for v in pastVacations:
                    print(v)
        
    def book(self):
# add loop functionality to continue prompting for dates
        date_format = '%Y-%m-%d'

        while True:
            try:
                start_date = input("When would you like your vacation to start? ")
# We need to provide an example of the date input format or make it so how the
# user formats their date doesnt matter
                startDate = datetime.datetime.strptime(start_date, date_format).date()
                print(f"Here is your start date: {startDate}")
            except:
                print('Please enter a valid date!')
                continue
            else:
                break
        
        while True:
            try:
                end_date = input("When would you like your vacation to end? ")
                endDate = datetime.datetime.strptime(end_date, date_format).date()
                print(f"Here is your end date: {endDate}")
            except:
                print('Please enter a valid date!')
                continue
            else:
                break

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
            if book_prop.lower() == 'y':
                session.add(Vacation(startDate, endDate, self.trav_obj.id, dp.id))
                session.commit()
                print('Congrats! Your vacation is booked!')


    def view_update(self):
        print(' ')
        print(" **My Profile** ")
        print(' ')

        print(f'First Name: {self.trav_obj.first_name}')
        print(f'Last Name: {self.trav_obj.last_name}')
        print(f'Location: {self.trav_obj.location}')

        print('')

        my_vacations = [v for v in self.trav_obj.vacations]

        print('Your vacations:')

        if len(my_vacations) > 0:
            for i, v in enumerate(my_vacations):
                print(f"{i + 1}. {v.domicile.property_type}, in {v.domicile.dest_location} from {v.start_date} - {v.end_date}" )
        else:
            print("No vacations booked yet!")

        print('')

        edit = input('Would you like to edit a vacation(y/n)? ')

        
        if edit.lower() == 'y':
            if len(my_vacations) > 1:
                chosen_vaca = input("Type the number of the vacation you'd like to edit/delete ")
                print('')

                if int(chosen_vaca) in range(1, len(my_vacations) + 1):
                    cv = my_vacations[int(chosen_vaca) - 1]
                    
            elif len(my_vacations) == 1:
                cv = my_vacations[0]
                
            print(f"Currently Editing Vacation: {cv.domicile.property_type}, in {cv.domicile.dest_location} from {cv.start_date} - {cv.end_date}" )

            print('')
            update_action = input("To update this vacation, type 'U', to delete this vacation, type 'D': ")

            print('')
# add logic to make sure updated dates are in the correct range
# can't exit once in enter date screen
# add end date addition functionality
            if update_action.lower() == 'u':
                edit_prop = input("Enter 1 to edit the start date, 2 to edit the end date, or 3 to edit the property: ")
                date_format = '%Y-%m-%d'
                if edit_prop == '1':
                    while True:
                        try:
                            vac_by_cvd = session.query(Vacation).filter(Vacation.Domicile_id == cv.Domicile_id).order_by(Vacation.start_date.desc())
                            print("")
                            print("This location currently has other reservations during: ")
                            print("")
                            for v in vac_by_cvd:
                                if v == cv:
                                    print(f"***{v.start_date} to {v.end_date}***")
                                else:
                                    print(f"{v.start_date} to {v.end_date}")
                            print("")    
                            new_start_date = input("Please enter your new start date: ")
                            newStartDate = datetime.datetime.strptime(new_start_date, date_format).date()

                            difference_dict = {}
                            for date in [v.end_date for v in vac_by_cvd]:
                                difference_dict[date] = (date-newStartDate).days

                            copy_diff_dict = difference_dict.copy()

                            print(f" Here is the difference dict: {difference_dict}")
                            
                            for key, value in copy_diff_dict.items():
                                
                                if value >= 0:
                                    del difference_dict[key]
                                    print(difference_dict)
                            
                            closest_end_date = max(difference_dict, key = lambda val: difference_dict[val])

                            if closest_end_date < newStartDate < cv.end_date:
                                print(f"Here is your new start date: {newStartDate}")
                                cv.start_date = newStartDate
                                session.commit()
                            else:
                                raise ValueError
                        except:
                            print('PLEASE ENTER A VALID DATE!')
                            print("")
                            continue
                        else:
                            break
                elif edit_prop == '2':
                    while True:
                        try:
                            new_end_date = input("Please enter your new end date: ")
                            newEndDate = datetime.datetime.strptime(new_end_date, date_format).date()
                            print(f"Here is your new end date: {newEndDate}")
                            cv.end_date = newEndDate
                            session.commit()
                        except:
                            print('PLEASE ENTER A VALID DATE!')
                            continue
                        else:
                            break
                elif edit_prop == '3':
                    available_domiciles = []
                    for d in CLI.domiciles:
                        vcount = 0
                        for v in d.vacations:
                            if (cv.start_date < v.start_date):
                                if (cv.end_date < v.start_date):
                                    vcount += 1
                            elif (cv.end_date > v.end_date):
                                if(cv.start_date > v.end_date):
                                    vcount += 1
                        if vcount == len(d.vacations):
                            available_domiciles.append(d)
                    
                    print("Available Properties:")
                    for i, d in enumerate(available_domiciles):
                        print(f'{i + 1}. Property Type: {d.property_type}, Location: {d.dest_location}')
                    
                    print('')
                    new_dom = input("Please enter the number of the property you would like to switch to: ")
                    
                    dom_pre_change = tuple([d for d in CLI.domiciles if d.id == cv.Domicile_id])

                    if int(new_dom) in range(1, len(available_domiciles)+1):
                        new_property = available_domiciles[int(new_dom)-1]
                        cv.Domicile_id = new_property.id
                        session.commit()

                        print(f"Congrats! Property changed from {dom_pre_change[0].property_type} in {dom_pre_change[0].dest_location} to {new_property.property_type} in {new_property.dest_location}")
                        
            elif update_action.lower() == 'd': 
                session.delete(cv)
                session.commit()
                print('Vacation deleted successfully!')
                print('Your vacations:')
                new_vacations = [v for v in self.trav_obj.vacations]
                if len(new_vacations) > 0:
                    for i, v in enumerate(new_vacations):
                        print(f"{i + 1}. {v.domicile.property_type}, in {v.domicile.dest_location} from {v.start_date} - {v.end_date}" )
                else:
                    print("No vacations booked yet!")

if __name__ == '__main__':
    
    user_fn = input("Enter Your First Name: ")
    user_ln = input("Enter Your Last Name: ")
    user_city = input("Enter Your City Name: ")
    CLI(user_fn, user_ln, user_city)
#Ask user reason for vacation, and display in the past bookings in browse
# ie. Work Retreat, Family Vacation, Honeymoon... etc etc


ipdb.set_trace()