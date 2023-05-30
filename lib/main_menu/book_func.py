import os, time, sys, datetime 
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db.models import Base, Vacation, Domicile
from lib.screen_data import print_booking_greeting

engine = create_engine("sqlite:///lib/db/project.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def book(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        date_format = '%Y-%m-%d'
        accepted_date_formats = ['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y', '%d-%b-%Y', '%d %B %Y']

        while True:
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
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
                                                Reason for visit: ''')
                                
                                print('''                                        ········································································
                                                                                                              
                                                ''')
                                time.sleep(1)
                    

                                session.add(Vacation(start_date = startDate,
                                                     end_date = endDate,
                                                     Traveler_id = self.trav_obj.id,
                                                     Domicile_id = dp.id,
                                                     rsn_for_visit = rsn_response))
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
                                            ╰༼=ಠਊಠ=༽╯    Please enter a valid selection!    ╰༼=ಠਊಠ=༽╯
                                        ******************************************************************
                ''')
                time.sleep(2)