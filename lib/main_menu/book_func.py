import time, sys, datetime 
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db.models import Base, Vacation, Domicile
from main_menu.function_screen_data import (
    print_booking_greeting,
    print_user_start_date,
    print_user_date_error,
    clear_screen,
    print_user_end_date_input,
    print_bottom_booking_screen,
    print_avaliable_properties,
    print_property_details,
    print_booking_signature,
    print_bottom_of_signature,
    print_booking_verification,
    print_valid_selection_error,
    print_lenny_selection_error,
    )

engine = create_engine("sqlite:///lib/db/project.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def book(self):
        clear_screen()
        date_format = '%Y-%m-%d'
        accepted_date_formats = ['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y', '%d-%b-%Y', '%d %B %Y']

        while True:
            try:
                clear_screen()
                start_date = print_booking_greeting()
                if start_date.lower() == 'x':
                    return
                for date_format in accepted_date_formats:
                    try:
                        startDate = datetime.datetime.strptime(start_date, date_format).date()
                    except ValueError:
                        pass
                    else:
                        break
                print_user_start_date(startDate)
            except:
                print_user_date_error()
                time.sleep(2)
                clear_screen()
                continue
            else:
                break
        while True:
            try:
                end_date = print_user_end_date_input()
                if end_date.lower() == 'x':
                    return
                for date_format in accepted_date_formats:
                    try:
                        testEndDate = datetime.datetime.strptime(end_date, date_format).date()
                    except ValueError:
                        pass
                    else:
                        break
                if testEndDate < startDate:
                    raise ValueError
                else:
                    endDate = testEndDate
                print_bottom_booking_screen()
            except:
                print_user_date_error()
                time.sleep(1)
                num_lines = 10
                sys.stdout.write(f"\033[{num_lines}A")
                sys.stdout.write(f"\033[{num_lines}M")
                continue
            else:
                break

        filtered_domiciles = []
        for d in session.query(Domicile).all():
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
                clear_screen()
                propID = print_avaliable_properties(startDate, endDate, filtered_domiciles)
                if propID.lower() == "x":
                    break
                elif int(propID) in range(1, len(filtered_domiciles)+1):
                    while True:
                        try:
                            dp = filtered_domiciles[int(propID) - 1]
                            clear_screen()
                            book_prop = print_property_details(dp)
                            if book_prop.lower() == 'z':
                                break
                            elif book_prop.lower() not in ['z','b']:
                                raise NameError
                            elif book_prop.lower() == 'b':
                                rsn_response = print_booking_signature(self)
                                print_bottom_of_signature()
                                time.sleep(1)
                                
                                session.add(Vacation(start_date = startDate,
                                                     end_date = endDate,
                                                     Traveler_id = self.trav_obj.id,
                                                     Domicile_id = dp.id,
                                                     rsn_for_visit = rsn_response))
                                session.commit()
                                print_booking_verification()
                                break
                        except:
                            print_valid_selection_error()
                            time.sleep(2)
                            continue
                    if (book_prop.lower() == 'z'):
                        continue
                    else:
                        break
            except:
                print_lenny_selection_error()
                time.sleep(2)