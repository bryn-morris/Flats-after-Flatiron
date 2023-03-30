#!/usr/bin/env python3

import ipdb
from db.models import Vacation, Traveler, Domicile
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
import os, time


engine = create_engine("sqlite:///lib/db/project.db")
Session = sessionmaker(bind=engine)
session = Session()

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class CLI():
    
    domiciles = session.query(Domicile).all()

    travelers = [traveler for traveler in session.query(Traveler)]
    
    lower_trav = []

    for traveler in travelers:
        traveler.first_name = traveler.first_name.lower()
        traveler.last_name = traveler.last_name.lower()
        lower_trav.append(traveler)

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
        
        exit = False
        while exit == False:

                # use this to clear the command line interface to make "screens"
            os.system('cls' if os.name == 'nt' else 'clear')
            print('')
            print('')
            print("            ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
            # Not working - if first name OR last name matches, it registers as user already registered, need to take a look at logic - 
            #  don't touch strings currently they line up with main menu
            print(f'                         ><><><><><><><><><><><><>    WELCOME TO FLATS AFTER FLATIRON, {self.trav_obj.first_name.upper()}!   ><><><><><><><><><><><><'
                if (self.trav_obj.first_name.lower() not in [trav.first_name for trav in CLI.lower_trav]) and (self.trav_obj.last_name.lower() not in [trav.last_name for trav in CLI.lower_trav]) 
                else f'                         ><><><><><><><><><><><><>    WELCOME BACK TO FLATS AFTER FLATIRON, {self.trav_obj.first_name.upper()}!   ><><><><><><><><><><><><')
            print("            ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")

            choice = input('''

            ><><><><><><><><><><><><><><><><><><><><><><><><><                   <><><><><><><><><><><><><><><><><><><><><><><><><><><><>
            ><><><><><><><><><><><><><><><><><><><><><><><><><      Main Menu    ><><><><><><><><><><><><><><><><><><><><><><><><><><><><
            ><><><><><><><><><><><><><><><><><><><><><><><><><                   <><><><><><><><><><><><><><><><><><><><><><><><><><><><> 


                                                         __             _,-"~^"-.
                                                       _// )      _,-"~`         `.
                                                      ." ( /`"-,-"`                 ;
                                                     / 6                             ;
                                                    /           ,             ,-"     ;
                                                   (,__.--.      \           /        ;
                                                    //'   /`-.\   |          |        `._________
                                                      _.-'_/`  )  )--...,,,___\     \-----------,)
                                                    ((("~` _.-'.-'           __`-.   )         //
                                                      jgs ((("`             (((---~"`         //
                                                                                            ((________________
                                                                                             `----""""~~~~^^^```


                                                           What would you like to do?

                                    Book a Vacation            View your Profile             Browse all Properties
                                      [[Type 'B']]                [[Type 'V']]                    [[Type 'N']]



            ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
            ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
            ''')
            

            if choice.lower() == 'b':
                self.book()
            elif choice.lower() == 'v':
                self.view_update()
            elif choice.lower() == 'n':
                self.browse()

            print(' ')
            print("Type 'T' for Title Menu or 'M' for Main Menu")
            user_input = input("Where to next?: ")
            print(' ')
            
            if user_input.lower() == 't':
                os.system('cls' if os.name == 'nt' else 'clear')
                
                exit = True

     
    def browse(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''
        
        ·····························································································································
        ··················································      Properties    ·······················································
        ····························································································································· 
        
        
        ''')

#Unable to pull up "Where to go from here menu" from here

        for i, d in enumerate(CLI.domiciles):
            try:
                print("                                      ································································")
                print(f'                                            {i + 1}. Property Type: {d.property_type}, Location: {d.dest_location}')
            except:
                pass
            finally:
                print("                                      ································································")

        print("")
        detailPropID = input('''

                                        Please enter the number of the property to see more details: 
                                
        ····························································································································· 
        ·····························································································································                         
                            ''')
        
        if int(detailPropID) in range(1, len(CLI.domiciles) + 1):
            os.system('cls' if os.name == 'nt' else 'clear')
                
            dp = CLI.domiciles[int(detailPropID) - 1]
            print(' ')

            viewPastBookings = input(f'''
        
        ····························································································································· 
        ··················································      Property Details    ·················································
        ·····························································································································     
            
        
        
                                      ································································
                                                            Property Type: 
                                                                {dp.property_type}
                                      ································································
                                                            Location: 
                                                                {dp.dest_location}
                                      ································································
                                                            Sleeping Capacity: 
                                                                {dp.sleep_capacity}
                                      ································································
                                                            Local Amenities: 
                                                        {dp.local_amenities}
                                      ································································


            
                                        See past bookings                                            More Options 
                                          [[Type 'B']]                                               [[Type 'M']]
        ····························································································································· 
        ····························································································································· 

            ''')


            
            history_count = 0
            if viewPastBookings.lower() == 'b':

                print(''' ''')
                print("><><><><><><><><><><><><><><><><><")
                print("Here are some past residents!")
                print("><><><><><><><><><><><><><><><><><")
                print(' ')

                pastVacations = [v for v in CLI.vacations if v.Domicile_id  == dp.id]
                for v in pastVacations:
                    try:
                        print("--------------------------------------------------------------")
                        print(f"{history_count}. {v.traveler.first_name} {v.traveler.last_name}")
                        print(f"   Reason for visit: {v.rsn_for_visit}")
                        history_count += 1
                    except:
                        pass
                    finally:
                        print("--------------------------------------------------------------")
        
    def book(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        date_format = '%Y-%m-%d'

        # accepted_date_formats = ['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y', '%d-%b-%Y', '%d %B %Y']

        

        while True:
            try:
            #     usersd= input("When would you like your vacation to start?")
            #     for date_format in accepted_date_formats:
            #         try:
            #             start_date = datetime.strptime(usersd, accepted_date_formats).strftime('%Y-%m-%d')
            #         except ValueError:
            #             pass
            #         else:
            #             break
            #     print(f"Here is your start date: {start_date}")
            # except:
            #     print('Please enter a valid date! (year-month-day)')
            #     continue
            # else:
            #     break

                start_date = input("When would you like your vacation to start? (year-month-day) ")
# We need to provide an example of the date input format or make it so how the
# user formats their date doesnt matter
                startDate = datetime.datetime.strptime(start_date, date_format).date()
                print('')
                print("><><><><><><><><><><><><><><><><><")
                print(f"Here is your start date: {startDate}")
                print("><><><><><><><><><><><><><><><><><")
                print('')
            except:
                print('Please enter a valid date! (year-month-day)')
                continue
            else:
                break
# Need to add logic so end date CANNOT be after start date without raising the except condition
        while True:
            try:
                end_date = input("When would you like your vacation to end? (year-month-day) ")
                endDate = datetime.datetime.strptime(end_date, date_format).date()
                print('')
                print("><><><><><><><><><><><><><><><><><")
                print(f"Here is your end date: {endDate}")
                print("><><><><><><><><><><><><><><><><><")
                print('')
            except:
                print('Please enter a valid date! (year-month-day)')
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
        print('')
        print("><><><><><><><><><><><><><><><><><")
        print('Here are the available domiciles: ')
        for i, d in enumerate(filtered_domiciles):
            print(f'{i + 1}. {d.property_type}')
        print("><><><><><><><><><><><><><><><><><")
        print('')

        propID = input('Would you like to see the details of a property to book? Please enter one of the numbers above: ')

        if int(propID) in range(1, len(filtered_domiciles)+1):
            dp = filtered_domiciles[int(propID) - 1]
            print("\033[1m" + '** Property Details **' + "\033[0m")
            print(f"Property Type: {dp.property_type}")
            print(f"Location: {dp.dest_location}")
            print(f"Sleeping Capacity: {dp.sleep_capacity}")
            print(f"Local Amenities: {dp.local_amenities}")

            book_prop = input('Would you like to book this property(y/n)? ')
# Add functionality if user says no (return to domicile list)
# Add functionality to kick user back to main menu
            if book_prop.lower() == 'y':
                print('')
                print("><><><><><><><><><><><><><><><><><")
                print('Great! We support electronic sign in.')
                print("><><><><><><><><><><><><><><><><><")
                print('')
                rsn_response = input('What is the reason for your visit? ')

                session.add(Vacation(startDate, endDate, self.trav_obj.id, dp.id, rsn_response))
                session.commit()
                print('')
                print("><><><><><><><><><><><><><><><><><")
                print('Congrats! Your vacation is booked!')
                print("><><><><><><><><><><><><><><><><><")
                print('')


    def view_update(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('')
        print("><><><><><><><><><><><><><><><><><")
        print(" **My Profile** ")
        print("><><><><><><><><><><><><><><><><><")
        print('')

        print(f'First Name: {self.trav_obj.first_name}')
        print(f'Last Name: {self.trav_obj.last_name}')
        print(f'Location: {self.trav_obj.location}')

        print('')

        my_vacations = [v for v in self.trav_obj.vacations]

        print('')
        print("><><><><><><><><><><><><><><><><><")
        print('Your vacations:')
        print("><><><><><><><><><><><><><><><><><")
        print('')

        if len(my_vacations) > 0:
            for i, v in enumerate(my_vacations):
                print(f"{i + 1}. {v.domicile.property_type}, in {v.domicile.dest_location} from {v.start_date} - {v.end_date}" )
        else:
            print('')
            print("><><><><><><><><><><><><><><><><><")
            print("No vacations booked yet!")
            print("><><><><><><><><><><><><><><><><><")
            print('')

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
                        for i, v in enumerate(new_vacations):
                            try:
                                print("--------------------------------------------------------------")
                                print(f'{i + 1}. Property Type: {d.property_type}, Location: {d.dest_location}')
                            except:
                                pass
                            finally:
                                print("--------------------------------------------------------------")
                        
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
                        try:
                            print("--------------------------------------------------------------")
                            print(f"{i + 1}. {v.domicile.property_type}, in {v.domicile.dest_location} from {v.start_date} - {v.end_date}" )
                        except:
                            pass
                        finally:
                            print("--------------------------------------------------------------")
                else:
                    print("No vacations booked yet!")

if __name__ == '__main__':
    login_counter = 0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><")
        print("><><><><><><><><>                        <><><><><><><><><><><><")
        print("><><><><><><><><>  FLATS AFTER FLATIRON  <><><><><><><><><><><><")
        print("><><><><><><><><>                        <><><><><><><><><><><><")
        print("><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><")
        print("")
        print("")
        print("")
        print("")
        print("-----------------------------------------------------------------")
        print("")
        print("                   Press Enter to get Started")
        print("                        or C to exit         ")
        print("")
        print("-----------------------------------------------------------------")
        time.sleep(1)
        
        user_input = input()
        if user_input == "":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("")
            print("")
            print("-----------------------------------------------")
            user_fn = input("Enter Your First Name: ")
            user_ln = input("Enter Your Last Name: ")
            user_city = input("Enter Your City Name: ")
            print("-----------------------------------------------")
            time.sleep(1)
            print("")
            print("")
            CLI(user_fn, user_ln, user_city)
        elif(user_input.lower() == "c"):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(''' 

            ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
            ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
                

                                                        
                                          ___                       _    _        _  _             _    
                                         / __|    ___     ___    __| |  | |__    | || |   ___     | |   
                                        | (_ |   / _ \   / _ \  / _` |  | '_ \    \_, |  / -_)    |_|   
                                         \___|   \___/   \___/  \__,_|  |_.__/   _|__/   \___|   _(_)_  
                                        _|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_| """"|_|"""""|_| """ | 
                                        "`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 


                                                                    _--"-.
                                                                .-"       "-.
                                                                |""--..      '-.
                                                                |      ""--..   '-.
                                                                |.-. .-".    ""--..".
                                                                |'./  -_'  .-.      |
                                                                |      .-. '.-'   .-'
                                                                '--..  '.'    .-  -.
                                                                     ""--..   '_'   :
                                                                            ""--..   |
                                                                                 ""-' mga

            ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
            ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
                
                ''')
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("")
            print("")
            print("                         ヽ(ಠ_ಠ)ノ"
                  if login_counter == 0 else
                   "                      ( ͠° ͟ʖ ͡° )")
            print("")
            print("")
            print("Press Enter Please! This is an exercise in following directions..."
             if login_counter == 0 else 
             "This REALLY isn't that hard...press" + color.BOLD +  " E.N.T.E.R" + color.END + "..." )
            print("")
            print("")
            print("")
            time.sleep(4)
            login_counter = 1
            continue

