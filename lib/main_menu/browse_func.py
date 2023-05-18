import os, ipdb, time
from sqlalchemy import create_engine
from db.models import Base, Domicile
from sqlalchemy.orm import sessionmaker
from main_menu.color_class import color
from db.models import Vacation

engine = create_engine("sqlite:///lib/db/project.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def browse(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        all_dom = session.query(Domicile).all()
        
        while True:
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('''
        
        ·····························································································································
        ····················································      Properties    ·····················································
        ····························································································································· 
        
        
        ''')

#Unable to pull up "Where to go from here menu" from here

                for i, d in enumerate(all_dom):
                    print(f'''
                    ········································································································
                        {i + 1}. {color.BOLD} Property Name: {color.END} {d.name}, {color.BOLD} Property Type: {color.END} {d.property_type}, {color.BOLD} Location: {color.END} {d.dest_location}
                    ········································································································
                    ''')
                
                detailPropID = input('''

                            For More Details                                                         To Exit 
                        [[Enter Property Number]]                                                 [[Type 'X']]
                                            
        ·····························································································································
        ·····························································································································                         
                                ''')
                if detailPropID.lower() == 'x':
                        break
                if int(detailPropID) in range(1, len(all_dom) + 1):
                        while True:
                            try:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    
                                    dp = all_dom[int(detailPropID) - 1]
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
                                        # pastVacations = [v for v in all_dom if v.id  == dp.id]
                                        pastVacations = session.query(Vacation).filter_by(Domicile_id = dp.id)
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
                else:
                    raise ValueError    
            except:
                print('''
                        Please make sure to enter a number associated with a property!
                ''')
                time.sleep(2)
                continue 
            break