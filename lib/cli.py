#!/usr/bin/env python3
from db.models import Vacation, Traveler, Domicile
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime, os, time, random, ipdb, sys
from main_menu.ascii_art import *
from main_menu.browse_func import browse
from main_menu.book_func import book
from main_menu.color_class import color
from main_menu.view_update_func import view_update


engine = create_engine("sqlite:///lib/db/project.db")
Session = sessionmaker(bind=engine)
session = Session()

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
                book(self)
            elif choice.lower() == 'v':
                view_update(self)
            elif choice.lower() == 'n':
                browse(self)

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

