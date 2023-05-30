#!/usr/bin/env python3
from db.models import Vacation, Traveler, Domicile
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import time
from main_menu.ascii_art import *
from main_menu.browse_func import browse
from main_menu.book_func import book
from main_menu.color_class import color
from main_menu.view_update_func import view_update
from CLI_screen_data import (
    print_main_menu,
    print_greeting, 
    print_navigation_menu, 
    clear_screen, 
    print_opening_screen,
    print_user_data_request,
    print_goodbye_screen,
    tell_the_user_off,)

engine = create_engine("sqlite:///lib/db/project.db")
Session = sessionmaker(bind=engine)
session = Session()

class CLI():

    travelers = [traveler for traveler in session.query(Traveler)]

    def __init__(self, user_fn, user_ln, user_city):
        self.first_name = user_fn
        self.last_name = user_ln
        self.city = user_city
        self.verify_traveler()

        print_greeting(self)

        time.sleep(3)
        clear_screen()
        self.start()

    def comparison_func(self):
        return any(trav.first_name == self.first_name and trav.last_name == self.last_name for trav in CLI.travelers)
        
    def verify_traveler(self):
        for t in CLI.travelers:
            if t.first_name == self.first_name and t.last_name == self.last_name and t.location == self.city:
                self.trav_obj= t
                return None
            
        new_traveler = Traveler(
            first_name = self.first_name,
            last_name = self.last_name,
            location = self.city,
        )
        session.add(new_traveler)
        session.commit()
        self.trav_obj = new_traveler
    
    def start(self):
        exit = False
        while exit == False:

            clear_screen()
            choice = print_main_menu()
            
            if choice.lower() == 'b':
                book(self)
            elif choice.lower() == 'v':
                view_update(self)
            elif choice.lower() == 'n':
                browse(self)

            user_input = print_navigation_menu()
            time.sleep(1)
            
            if user_input.lower() == 't':
                clear_screen()
                
                exit = True
      
if __name__ == '__main__':
    login_counter = 0
    while True:
        clear_screen()
        print_opening_screen()
        time.sleep(1)
        
        user_input = input()
        if user_input == "":
            clear_screen()            
            time.sleep(1)
            user_fn, user_ln, user_city = print_user_data_request()
            CLI(user_fn, user_ln, user_city)
        elif(user_input.lower() == "c"):
            clear_screen()
            print_goodbye_screen()
            break
        else:
            clear_screen()
            tell_the_user_off(login_counter)
            time.sleep(4)
            login_counter += 1
            continue

