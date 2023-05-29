import os
from db.models import Base, Vacation, Domicile
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os, time, datetime 
import ipdb

engine = create_engine("sqlite:///lib/db/project.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def view_update(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        all_dom = session.query(Domicile).all()
        
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
        #Do I need to query within this session context? - self.trav_obj.id filter 
        # Check line 82, querying using session may be causing the problem as trav obj was queried
        # within a different session context in CLI
        my_vacations = [v for v in session.query(Vacation).filter(Vacation.Traveler_id == self.trav_obj.id)]
        # my_vacations = [v for v in self.trav_obj.vacations]
        if len(my_vacations) > 0:
            for i, v in enumerate(my_vacations):
                print(f"                                        {i + 1}. {v.domicile.name}, in {v.domicile.dest_location} from {v.start_date} - {v.end_date}" )
            print('')
            edit = input('                                                      Would you like to edit a vacation(y/n)? ')
            print('')
            if edit.lower() == 'y':
                while True:
                    try:
                        if len(my_vacations) > 1:
                            chosen_vaca = input("                                        Type the number of the vacation you'd like to edit/delete ")
                            print('')

                            if int(chosen_vaca) in range(1, len(my_vacations) + 1):
                                cv = my_vacations[int(chosen_vaca) - 1]
                                
                        elif len(my_vacations) == 1:
                            
                            cv = my_vacations[0]
                        os.system('cls' if os.name == 'nt' else 'clear')    
                        print(f'''                     
                                                        ><><><><><><><><><><><><><><><><><

                                    Currently Editing Vacation: {cv.domicile.name}, in {cv.domicile.dest_location} from {cv.start_date} - {cv.end_date}
                                                            
                                                            ''')

                        update_action = input("                                             To update this vacation, type 'U', to delete this vacation, type 'D': ")

                        print('')
                        if update_action.lower() == 'u':
                            print("")
                            edit_prop = input("                                     Enter 1 to edit the start date, 2 to edit the end date, or 3 to edit the property: ")
                            date_format = '%Y-%m-%d'
                            if edit_prop == '1':
                                while True:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    try:
                                        vac_by_cvd = session.query(Vacation).filter(Vacation.Domicile_id == cv.Domicile_id).order_by(Vacation.start_date)
                                        print("")
                                        print("                                             This location currently has other reservations during: ")
                                        print("")
                                        for v in vac_by_cvd:
                                            if v.id == cv.id:
                                                print(f'''
                                                    ><><><><><><><><><><><><><><><><><                               
                                                        {v.start_date} to {v.end_date}   ⟸ Current Vacation''')
                                            else:
                                                print(f'''
                                                    ><><><><><><><><><><><><><><><><><
                                                        {v.start_date} to {v.end_date}''')
                                        print('')
                                        new_start_date = input("                                            Please enter your new start date or x to exit: ")
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
                                        print('                                                     PLEASE ENTER A VALID DATE!')
                                        print("")
                                        time.sleep(2)
                                        continue
                                    break
                            elif edit_prop == '2':
                                while True:
                                    try:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        vac_by_cvd = session.query(Vacation).filter(Vacation.Domicile_id == cv.Domicile_id).order_by(Vacation.end_date)
                                        print("")
                                        print("                                             This location currently has other reservations during: ")
                                        print("")
                                        for v in vac_by_cvd:
                                            if v.id == cv.id:
                                                print(f'''                                                  ><><><><><><><><><><><><><><><><><
                                                        {v.start_date} to {v.end_date} ⟸  Current Vacation 
                                                ''')
                                            else:
                                                print(f'''                                                  ><><><><><><><><><><><><><><><><><
                                                        {v.start_date} to {v.end_date}
                                                ''')
                                        print("")    
                                        new_end_date = input("                                                  Please enter your new end date or x to exit: ")
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
                                        print('                                                         PLEASE ENTER A VALID DATE!')
                                        print("")
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
                                time.sleep(3)
                            else:
                                print('''
                                                    No vacations booked yet!
                                ''')
                                time.sleep(3)
                        else:
                            raise ValueError
                        break
                    except:
                        continue
        else:
            print(''')

                                                        ><><><><><><><><><><><><><><><><><
                                                             No vacations booked yet!
                                                        ><><><><><><><><><><><><><><><><><


        ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
        ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>                                

        
            ''')