#!/usr/bin/env python3
from db.models import Vacation, Traveler, Domicile
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime, os, time, random, ipdb, sys
from helpers import *


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
    
    # lower_trav = []

    # for traveler in travelers:
    #     traveler.first_name = traveler.first_name.lower()
    #     traveler.last_name = traveler.last_name.lower()
    #     lower_trav.append(traveler)

    vacations = session.query(Vacation).all()

    def __init__(self, user_fn, user_ln, user_city):
        self.first_name = user_fn
        self.last_name = user_ln
        self.city = user_city
        self.traveler()
        print('''            
            
            ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
            ''')
            # Not working - if first name OR last name matches, it registers as user already registered, need to take a look at logic - 
            #  don't touch strings currently they line up with main menu
        print(f'                         ><><><><><><><><><><><><>    WELCOME TO FLATS AFTER FLATIRON, {self.trav_obj.first_name.upper()}!   ><><><><><><><><><><><><'
                # if (self.trav_obj.first_name.lower() not in [trav.first_name for trav in CLI.lower_trav]) and (self.trav_obj.last_name.lower() not in [trav.last_name for trav in CLI.lower_trav]) 
                # else f'                         ><><><><><><><><><><><><>    WELCOME BACK TO FLATS AFTER FLATIRON, {self.trav_obj.first_name.upper()}!   ><><><><><><><><><><><><'
                )
        print('''
            ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

        ''')
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
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
            choice = input(f'''

            ><><><><><><><><><><><><><><><><><><><><><><><><><><>                    <><><><><><><><><><><><><><><><><><><><><><><><><><>
            ><><><><><><><><><><><><><><><><><><><><><><><><><><>      Main Menu     ><><><><><><><><><><><><><><><><><><><><><><><><><><
            ><><><><><><><><><><><><><><><><><><><><><><><><><><>                    <><><><><><><><><><><><><><><><><><><><><><><><><><> 
    

                                                                       
                                                         {random.choice(welcome_images)}
                                                       

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

            user_input = input('''
             
                                        vvvvvvvvvvvvvvvvvvvvvvvvvv  Where to Next?  vvvvvvvvvvvvvvvvvvvvvvvvvv

                                                                      （＾ω＾）                                                                   
                           
                                           Title Menu                                            Main Menu
                                          [[Type 'T']]                                          [[Type 'M']]
                                        
            ''')
            time.sleep(1)
            
            if user_input.lower() == 't':
                os.system('cls' if os.name == 'nt' else 'clear')
                
                exit = True

     
    def browse(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        
        while True:
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('''
        
        ·····························································································································
        ····················································      Properties    ·····················································
        ····························································································································· 
        
        
        ''')

#Unable to pull up "Where to go from here menu" from here

                for i, d in enumerate(CLI.domiciles):
                    print(f'''
                    ········································································································
                        {i + 1}. {color.BOLD} Property Name: {color.END} {d.name}, {color.BOLD} Property Type: {color.END} {d.property_type}, {color.BOLD} Location: {color.END} {d.dest_location}
                    ········································································································
                    ''')
                
                detailPropID = input('''

                            For More Details                                                         To Exit 
                        [[Enter Property Number]]                                                  [[Type 'X']]
                                            
        ·····························································································································
        ·····························································································································                         
                                ''')
                if detailPropID.lower() == 'x':
                        break
                if int(detailPropID) in range(-9999999999999999999, 999999999999999999999999):
                    try:
                        while True:
                            try:
                             
                                if int(detailPropID) in range(1, len(CLI.domiciles) + 1):
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    
                                    dp = CLI.domiciles[int(detailPropID) - 1]
                                    print(' ')

                                    viewPastBookings = input(f''' 
        ····························································································································· 
        ················································      Property Details    ···················································
        ·····························································································································     
            
        
        
                                    ··································································
                                    Property Name: {dp.name}
                                    ··································································
                                    Property Type: {dp.property_type}
                                    ··································································
                                    Location: {dp.dest_location}
                                    ··································································
                                    Sleeping Capacity: {dp.sleep_capacity}
                                    ··································································
                                    Local Amenities:  {dp.local_amenities}                    
                                    ··································································


            
                                      See Past Bookings        Return to Properties            To Exit 
                                        [[Type 'B']]               [[Type 'V']]             [[Type 'X']]

        ····························································································································· 
        ····························································································································· 

                        ''')
                                    if (viewPastBookings.lower() == 'x'):
                                        return
                                    elif viewPastBookings.lower() == 'v':
                                        break
                                    elif viewPastBookings.lower() == 'b':
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        pastVacations = [v for v in CLI.vacations if v.Domicile_id  == dp.id]
                                        print(f'''
        ·····························································································································
        ·····························································································································

                            ························································································
                            ·····················     Past Residents of this Property    ···························
                            ························································································ 
                                                                                                
                            ''')
                                    
                                        print(f'                                                            {color.BOLD}  {dp.name}  {color.END}')
                                        print('                            ························································································')
                                        for v in pastVacations:
                                            print(f''' 
                                  ···········································································
                                            {v.traveler.first_name.capitalize()} {v.traveler.last_name.capitalize()}
                                                Reason for visit: {v.rsn_for_visit}
                                  ···········································································
                                            ''')                                  
                                        print('''
                    
        ·····························································································································
        ·····························································································································
                            ''') 
                                        break
                                
                            except:
                                print('''
                                ··································································
                                                Please make a valid selection!
                                ··································································
                                ''')
                                time.sleep(1)
                                continue
                       
                    except:
                        print('''
                                Please make sure to enter a number associated with a property!
                        ''')
                        time.sleep(2)
                        continue            
            except:
                print('''
                                                  Please make sure to enter a number!            
                ''')
                time.sleep(2)
                continue
            break
        
    def book(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        date_format = '%Y-%m-%d'
# not able to exit out of date entry loop without terminating terminal
        # accepted_date_formats = ['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y', '%d-%b-%Y', '%d %B %Y']

        while True:
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
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
            #     print('Please enter a valid date!(YYYY-MM-DD)')
            #     continue
            # else:
            #     break

# Fancy up and refactor
                start_date = input('''
                 
        *****************************************************************************************************************************       
        **************************************************     Welcome to Booking     ***********************************************
        *****************************************************************************************************************************
                                    
                                                                    To Exit
                                                                  [[Type 'X']]

                                        ******************************************************************
                                            When would you like your vacation to start? (YYYY-MM-DD)
                                        ******************************************************************

                ''')
# We need to provide an example of the date input format or make it so how the
# user formats their date doesnt matter
                if start_date.lower() == 'x':
                    return
                startDate = datetime.datetime.strptime(start_date, date_format).date()
                print(f'''
                                        ******************************************************************
                                                        Here is your start date: {startDate}
                                        ******************************************************************
                ''')
            except:
                print('''
                                        ******************************************************************
                                        ╰༼=ಠਊಠ=༽╯    Please enter a valid date! (YYYY-MM-DD)    ╰༼=ಠਊಠ=༽╯
                                        ******************************************************************
                ''')
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
            else:
                break
        while True:
            try:
                end_date = input('''
                                        ******************************************************************
                                            When would you like your vacation to end? (YYYY-MM-DD)
                                        ******************************************************************
                ''')
                if end_date.lower() == 'x':
                    return
                testEndDate = datetime.datetime.strptime(end_date, date_format).date()
                if testEndDate < startDate:
                    raise ValueError
                else:
                    endDate = testEndDate
                print(f'''

        *****************************************************************************************************************************
        *****************************************************************************************************************************

                ''')
            except:
                print('''
                                        ******************************************************************
                                        ╰༼=ಠਊಠ=༽╯    Please enter a valid date! (YYYY-MM-DD)   ╰༼=ಠਊಠ=༽╯
                                        ******************************************************************
                ''')
                time.sleep(1)
                num_lines = 10
                sys.stdout.write(f"\033[{num_lines}A")
                sys.stdout.write(f"\033[{num_lines}M")
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
        while True:
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'''

        *****************************************************************************************************************************       
        **************************************************     Avaliable Properties     *********************************************       
        *****************************************************************************************************************************       
        
                                        ******************************************************************    
                                        
                                                Here are the available properties for those dates

                                                     Start: {startDate}        End: {endDate} 

                                        ****************************************************************** 
                     
                ''')
                for i, d in enumerate(filtered_domiciles):
                    print(f'''
                                        ****************************************************************** 
                                                {i + 1}. {d.name} in {d.dest_location}
                                        ****************************************************************** 
                    ''')
                
                propID = input('''

                                For More Details                                                        To Exit 
                            [[Enter Property Number]]                                                 [[Type 'X']]

        *****************************************************************************************************************************
        *****************************************************************************************************************************
                ''')
                if propID.lower() == "x":
                    break
                elif int(propID) in range(1, len(filtered_domiciles)+1):
                    while True:
                        try:
                            dp = filtered_domiciles[int(propID) - 1]
                            os.system('cls' if os.name == 'nt' else 'clear')
                            book_prop = input(f'''

        *****************************************************************************************************************************       
        **************************************************     Property Details     *************************************************
        *****************************************************************************************************************************

                                                                    {dp.name}
                                        
                                        
                                        ******************************************************************
                                                        Property Type: {dp.property_type}
                                        ******************************************************************

                                        ******************************************************************
                                                        Location: {dp.dest_location}
                                        ******************************************************************

                                        ******************************************************************
                                                        Sleeping Capacity: {dp.sleep_capacity}
                                        ******************************************************************

                                        ******************************************************************
                                                    Local Amenities: {dp.local_amenities}
                                        ******************************************************************                        
        
                              To Book This Property                                           To Return to Property List 
                                  [[Type 'B']]                                                       [[Type 'Z']]

        *****************************************************************************************************************************
        *****************************************************************************************************************************                
                        
                        
                            ''')
                            if book_prop.lower() == 'z':
                                break
                            elif book_prop.lower() not in ['z','b']:
                                raise NameError
                            elif book_prop.lower() == 'b':
                                rsn_response = input(f'''


                                        ************************************************************************

                                                                *****************

                                                                Great! Last step!

                                                                *****************
                                            
                                                  Sign into your vacation by signing the log book!
                                   
                                                  ************************************************
                                
                                        ········································································
                                            {self.trav_obj.first_name} {self.trav_obj.last_name}
                                                Reason for visit: 
                                        ········································································
                                                  

                                                              
                                                ''')
                    

                                session.add(Vacation(startDate, endDate, self.trav_obj.id, dp.id, rsn_response))
                                session.commit()
                                print('''

                                                        **********************************
                                                        Congrats! Your vacation is booked!
                                                        **********************************

                                        ************************************************************************
                                        ************************************************************************

                                ''')
                                break
                        except:
                            print('''
                                                        **********************************
                                                          Please make a valid selection!
                                                        **********************************
                            ''')
                            time.sleep(2)
                            continue
                    if (book_prop.lower() == 'z'):
                        continue
                    else:
                        break
            except:
                print('''
                                        ******************************************************************
                                            ╰༼=ಠਊಠ=༽╯    Please enter a valid number!    ╰༼=ಠਊಠ=༽╯
                                        ******************************************************************
                ''')
                time.sleep(2)
                

    def view_update(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        # Make past bookings visible/button option for each vacation in my profile
        # Make looks nicer and similar to previous screens
        print(f'''

        ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
        ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
                                        
        
                                                        <><><><><><><><><><><><><><><><><
                                                                     Profile 
                                                        ><><><><><><><><><><><><><><><><>
                                        
                                                     
                                                              First Name: {self.trav_obj.first_name}
                                                              Last Name: {self.trav_obj.last_name}
                                                              Location: {self.trav_obj.location}

                                                    
                                                        ><><><><><><><><><><><><><><><><><
                                                                  Your vacations:
                                                        ><><><><><><><><><><><><><><><><><

                                                                                                
        ''')

        my_vacations = [v for v in self.trav_obj.vacations]
        if len(my_vacations) > 0:
            for i, v in enumerate(my_vacations):
                print(f"                              {i + 1}. {v.domicile.name}, in {v.domicile.dest_location} from {v.start_date} - {v.end_date}" )
            print('')
            edit = input('                                      Would you like to edit a vacation(y/n)? ')
            print('')
            if edit.lower() == 'y':
                if len(my_vacations) > 1:
                    chosen_vaca = input("                                Type the number of the vacation you'd like to edit/delete ")
                    print('')

                    if int(chosen_vaca) in range(1, len(my_vacations) + 1):
                        cv = my_vacations[int(chosen_vaca) - 1]
                        
                elif len(my_vacations) == 1:
                    cv = my_vacations[0]
                    
                print(f'''                     
                                            ><><><><><><><><><><><><><><><><><

                        Currently Editing Vacation: {cv.domicile.name}, in {cv.domicile.dest_location} from {cv.start_date} - {cv.end_date}
                                                    
                                                    ''')

    # Factor this into "Buttons" like on main screen  
                update_action = input("                         To update this vacation, type 'U', to delete this vacation, type 'D': ")

                print('')
                if update_action.lower() == 'u':
                    edit_prop = input("                      Enter 1 to edit the start date, 2 to edit the end date, or 3 to edit the property: ")
                    date_format = '%Y-%m-%d'
                    if edit_prop == '1':
                        while True:
                            try:
                                vac_by_cvd = session.query(Vacation).filter(Vacation.Domicile_id == cv.Domicile_id).order_by(Vacation.start_date)
                                print("")
                                print("                         This location currently has other reservations during: ")
                                print("")
                                for v in vac_by_cvd:
                                    if v == cv:
                                        print(f'''
                                        ><><><><><><><><><><><><><><><><><                               
                                            {v.start_date} to {v.end_date}   ⟸ Current Vacation''')
                                    else:
                                        print(f'''
                                        ><><><><><><><><><><><><><><><><><
                                            {v.start_date} to {v.end_date}''')
                                print('')
                                new_start_date = input("                                   Please enter your new start date or x to exit: ")
                                if new_start_date.lower() == "x":
                                    break
                                newStartDate = datetime.datetime.strptime(new_start_date, date_format).date()

                                difference_dict = {}
                                for date in [v.end_date for v in vac_by_cvd]:
                                    difference_dict[date] = (date-cv.start_date).days
                                    
                                copy_diff_dict = difference_dict.copy()
                                
                                for key, value in copy_diff_dict.items():
                                    
                                    if value >= 0:
                                        del difference_dict[key]                                                                                                  
                                

                                if len(difference_dict) > 0:
                                    
                                    closest_end_date = max(difference_dict, key = lambda val: difference_dict[val])
                                    if closest_end_date < newStartDate < cv.end_date:
                                        print(f'''
                                                                        ><><><><><><><><><><><><><><><><><><><><><><
                                                                        Here is your new start date: {newStartDate}
                                                                        ><><><><><><><><><><><><><><><><><><><><><><
                                            ''')
                                        cv.start_date = newStartDate
                                        
                                        session.commit()
                                    else:
                                        raise ValueError
                                elif(len(difference_dict) == 0):
                                    
                                    if newStartDate < cv.end_date:
                                        print(f'''                                      
                                                                        ><><><><><><><><><><><><><><><><><><><><><><
                                                                        Here is your new start date: {newStartDate}
                                                                        ><><><><><><><><><><><><><><><><><><><><><><
                                            ''')
                                        cv.start_date = newStartDate
                                        session.commit()
                                        time.sleep(1)
                                else:
                                    raise ValueError

                            except:
                                print("")
                                print('                                         PLEASE ENTER A VALID DATE!')
                                print("")
                                continue
                            else:
                                break
                    elif edit_prop == '2':
                        while True:
                            try:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                vac_by_cvd = session.query(Vacation).filter(Vacation.Domicile_id == cv.Domicile_id).order_by(Vacation.end_date)
                                print("")
                                print("                                This location currently has other reservations during: ")
                                print("")
                                for v in vac_by_cvd:
                                    if v == cv:
                                        print(f'''                                     ><><><><><><><><><><><><><><><><><
                                            {v.start_date} to {v.end_date} ⟸  Current Vacation 
                                        ''')
                                    else:
                                        print(f'''                                     ><><><><><><><><><><><><><><><><><
                                            {v.start_date} to {v.end_date}
                                        ''')
                                print("")    
                                new_end_date = input("                           Please enter your new end date or x to exit: ")
                                if new_end_date.lower() == "x":
                                    break
                                newEndDate = datetime.datetime.strptime(new_end_date, date_format).date()

                                difference_dict = {}
                                for date in [v.start_date for v in vac_by_cvd]:
                                    difference_dict[date] = (date-cv.end_date).days

                                copy_diff_dict = difference_dict.copy()
                                
                                for key, value in copy_diff_dict.items():
                                    
                                    if value < 0:
                                        del difference_dict[key]
                                
                                if len(difference_dict) > 0:
                                    closest_start_date = min(difference_dict, key = lambda val: difference_dict[val])
                                    if closest_start_date > newEndDate > cv.start_date:
                                        print(f'''                                      
                                                        ><><><><><><><><><><><><><><><><><><><><><><
                                                        Here is your new end date: {newEndDate}
                                                        ><><><><><><><><><><><><><><><><><><><><><><
                                            ''')
                                        cv.end_date = newEndDate
                                        session.commit()
                                    else:
                                        raise ValueError
                                elif(len(difference_dict) == 0):
                                    if newEndDate > cv.start_date:
                                        print(f'''                                      
                                                        ><><><><><><><><><><><><><><><><><><><><><><
                                                        Here is your new end date: {newEndDate}
                                                        ><><><><><><><><><><><><><><><><><><><><><><
                                            ''')
                                        cv.end_date = newEndDate
                                        session.commit()
                                else:
                                    raise ValueError
                            except:
                                print("")
                                print('                                PLEASE ENTER A VALID DATE!')
                                print("")
                                time.sleep(2)
                                continue
                            else:
                                break
                        # while True:
                        #     try:
                        #         new_end_date = input("                                Please enter your new end date: ")
                        #         newEndDate = datetime.datetime.strptime(new_end_date, date_format).date()
                        #         print(f"                                Here is your new end date: {newEndDate}")
                        #         cv.end_date = newEndDate
                        #         session.commit()
                        #     except:
                        #         print('                                PLEASE ENTER A VALID DATE!')
                        #         continue
                        #     else:
                        #         break
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
                        # If you enter something other than a property number, the program crashes
                        while True:
                            try:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print('''                   


                                                                                    Available Properties:
                            
                                ''')
                                for i, d in enumerate(available_domiciles):
                                    print(f'''                                
                                                        --------------------------------------------------------------------------
                                                        {i + 1}. Property Name: {d.name}, Property Type: {d.property_type}, Location: {d.dest_location}
                                                        --------------------------------------------------------------------------
                                    ''') 
                                new_dom = input('''
                                                            Please enter the number of the property you would like to switch to: 
                                ''')
                                dom_pre_change = tuple([d for d in CLI.domiciles if d.id == cv.Domicile_id])

                                if int(new_dom) in range(1, len(available_domiciles)+1):
                                    new_property = available_domiciles[int(new_dom)-1]
                                    cv.Domicile_id = new_property.id
                                    cv.name = new_property.name
                                    session.commit()

                                    print(f"                                Congrats! Property changed from {dom_pre_change[0].name} in {dom_pre_change[0].dest_location} to {new_property.name} in {new_property.dest_location}")
                                    break
                            except:
                                print('''
                                
                                                                  Please make sure to enter one of the numbers associated with a property!
                                
                                ''')
                                time.sleep(2)
                                continue

                elif update_action.lower() == 'd': 
                    session.delete(cv)
                    session.commit()
                    print('                                Vacation deleted successfully!')
                    print('                                Your vacations:')
                    new_vacations = [v for v in self.trav_obj.vacations]
                    if len(new_vacations) > 0:
                        for i, v in enumerate(new_vacations):
                            print(f'''
                                                        --------------------------------------------------------------------------
                                                                {i + 1}. {v.domicile.name}, in {v.domicile.dest_location} from {v.start_date} - {v.end_date}
                                                        --------------------------------------------------------------------------
                            ''')
                    else:
                        print('''
                                              No vacations booked yet!
                        ''')
        else:
            print(''')

                                                        ><><><><><><><><><><><><><><><><><
                                                             No vacations booked yet!
                                                        ><><><><><><><><><><><><><><><><><


        ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
        ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>                                

            ''')
            print('')

if __name__ == '__main__':
    login_counter = 0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''

            ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
            ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
        
        
            
            
                                              ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><
                                              ><><><><><><><><><>                         <><><><><><><><><><>
                                              ><><><><><><><><><>   FLATS AFTER FLATIRON  <><><><><><><><><><>
                                              ><><><><><><><><><>                         <><><><><><><><><><>
                                              ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><

                                              -----------------------------------------------------------------
                                                                 Press Enter to get Started
                                                                        or C to exit       
                                              -----------------------------------------------------------------

                                              


            ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
            ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
            ''')
        time.sleep(1)
        
        user_input = input()
        if user_input == "":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'''

            ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
            ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

            
                                                 ><><><><><><><><><><><><><><><><><><><><><><><>

            ''')
            user_fn = input("                                                          Enter Your First Name:     ")
            print ("")
            user_ln = input("                                                          Enter Your Last Name:      ")
            print ("")
            user_city = input("                                                          Enter Your City Name:      ")
            print(f''' 

                                                 ><><><><><><><><><><><><><><><><><><><><><><><>

                                                 
            ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
            ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
                                                                           
            ''', flush = True)
            
            time.sleep(1)
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
            print(f'''

            ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
            ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

            
            
                                                         
            
                                                                      {'ヽ(ಠ_ಠ)ノ'if login_counter == 0 else '( ͠° ͟ʖ ͡° )'}


                                            {
                                            "Press Enter Please! This is an exercise in following directions..."
                                            if login_counter == 0 else 
                                            "This REALLY isn't that hard...press" + color.BOLD +  " E.N.T.E.R" + color.END + "..." 
                                            }
            
                                        
                                                

            ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
            ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
            ''')
            time.sleep(4)
            login_counter = 1
            continue

