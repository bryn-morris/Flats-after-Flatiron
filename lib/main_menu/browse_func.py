import os, ipdb, time
from sqlalchemy import create_engine
from db.models import Base, Domicile
from sqlalchemy.orm import sessionmaker
from main_menu.color_class import color
from db.models import Vacation
from main_menu.function_screen_data import (
    clear_screen,
    print_property_page,
    print_property_details,
    print_past_residents,
    print_properties_selection_error,
    print_properties_number_error,
)

engine = create_engine("sqlite:///lib/db/project.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def browse(self):
        clear_screen()
        all_dom = session.query(Domicile).all()
        
        while True:
            try:
                clear_screen()
                detailPropID = print_property_page(all_dom)
                if detailPropID.lower() == 'x':
                        break
                if int(detailPropID) in range(1, len(all_dom) + 1):
                        while True:
                            try:
                                clear_screen()
                                dp = all_dom[int(detailPropID) - 1]
                                viewPastBookings = print_property_details(dp)

                                if (viewPastBookings.lower() == 'x'):
                                    return
                                elif viewPastBookings.lower() == 'v':
                                    break
                                elif viewPastBookings.lower() == 'b':
                                    while True:
                                        clear_screen()
                                        
                                        pastVacations = session.query(Vacation).filter_by(Domicile_id = dp.id)
                                        exitInput = print_past_residents(pastVacations, dp)
                                        
                                        if exitInput.lower() == 'x':
                                                return
                                        elif exitInput.lower() == 'v':
                                                break
                                else:
                                    raise ValueError
                            except:
                                print_properties_selection_error()
                                time.sleep(1)
                                continue
                        # This continue is here to send us back to the outer loop from the inner loop
                        continue
                else:
                    raise ValueError    
            except:
                print_properties_number_error()
                time.sleep(2)
                continue