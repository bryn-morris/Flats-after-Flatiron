import sys
from db.models import Base, Vacation, Domicile
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from main_menu.function_screen_data import (
    print_profile_screen,
    clear_screen,
    print_no_vacations,
    print_edit_choice,
    print_profile_selection_error,
    print_vacation_editing,
    print_edit_options,
    print_other_reservations,
    print_new_date,
    print_profile_date_error,
    )
import os, time, datetime

engine = create_engine("sqlite:///lib/db/project.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def view_update(self):
        all_dom = session.query(Domicile).all()
        
        my_vacations = [v for v in session.query(Vacation).filter(Vacation.Traveler_id == self.trav_obj.id)]
        # my_vacations = [v for v in self.trav_obj.vacations]
        if len(my_vacations) > 0:
            while True:
                clear_screen()
                print_profile_screen(self.trav_obj, my_vacations)
                try:
                    if len(my_vacations) > 1:
                        chosen_vaca = print_edit_choice()
                        try:
                            if int(chosen_vaca) in range(1, len(my_vacations) + 1):
                                cv = my_vacations[int(chosen_vaca) - 1]
                            elif chosen_vaca.lower() == 'x':
                                return
                            else:
                                raise ValueError
                        except:
                            print_profile_selection_error()
                            time.sleep(2)
                            clear_screen()
                            continue

                    elif len(my_vacations) == 1:
                        
                        cv = my_vacations[0]
                        time.sleep(2)
                        
                    clear_screen()  
                    update_action = print_vacation_editing(cv)
                    
                    if update_action.lower() == 'u':
                        while True:
                            try:
                                edit_prop = print_edit_options()
                                date_format = '%Y-%m-%d'
                                vac_by_cvd = session.query(Vacation).filter(Vacation.Domicile_id == cv.Domicile_id).order_by(Vacation.end_date)

                                if edit_prop == '1':
                                    while True:
                                        clear_screen()
                                        try:  
                                            new_start_date = print_other_reservations(vac_by_cvd, cv, edit_prop)
                                            if new_start_date.lower() == "x":
                                                break
                                            newStartDate = datetime.datetime.strptime(new_start_date, date_format).date()

                                            difference_dict = {date: (date-cv.start_date).days for date in [v.end_date for v in vac_by_cvd] if (date-cv.start_date) >=0}
                                            closest_end_date = max(difference_dict, key = lambda val: difference_dict[val])

                                            if (len(difference_dict) > 0 and closest_end_date < newStartDate < cv.end_date) or (len(difference_dict) == 0 and newStartDate < cv.end_date):
                                                print_new_date(newStartDate, edit_prop)
                                                cv.start_date = newStartDate
                                                session.commit()
                                                time.sleep(1)
                                            else:
                                                raise ValueError
                                        except:
                                            print_profile_date_error()
                                            time.sleep(2)
                                            continue
                                        break
                                elif edit_prop == '2':
                                    while True:
                                        try:
                                            clear_screen()
                                            new_end_date = print_other_reservations(vac_by_cvd, cv, edit_prop)
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
                                            
                                            closest_start_date = min(difference_dict, key = lambda val: difference_dict[val])

                                            if (len(difference_dict) > 0 and closest_start_date > newEndDate > cv.start_date) or (len(difference_dict) == 0 and newEndDate > cv.start_date):
                                                print_new_date(newEndDate, edit_prop)
                                                cv.end_date = newEndDate
                                                session.commit()
                                                time.sleep(1)
                                            else:
                                                raise ValueError
                                        except:
                                            print_profile_date_error()
                                            time.sleep(2)
                                            continue
                                        break
                                elif edit_prop == '3':
                                    available_domiciles = []
                                    for d in all_dom:
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
                                    while True:
                                        try:
                                            clear_screen()
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
                                            dom_pre_change = tuple([d for d in all_dom if d.id == cv.Domicile_id])

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
                                else:
                                    raise ValueError
                            except:
                                print_profile_selection_error()
                                time.sleep(2)
                                num_lines = 12
                                sys.stdout.write(f"\033[{num_lines}A")
                                sys.stdout.write(f"\033[{num_lines}M")
                                continue
                            break

                    elif update_action.lower() == 'd': 
                        session.delete(cv)
                        session.commit()
                        print('')
                        print('                                Vacation deleted successfully!')
                        time.sleep(3)
                        clear_screen()
                        print('''                                
                                                                Your vacations:
                                                ><><><><><><><><><><><><><><><><><><><><><><
                        ''')
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
                            time.sleep(3)
                    elif update_action.lower() == 'x':
                        break
                    else:
                        raise ValueError
                    break
                except:
                    print('Is this broken?')
                    continue
        else:
            print_no_vacations()