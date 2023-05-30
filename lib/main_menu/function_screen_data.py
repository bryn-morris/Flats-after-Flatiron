import os

'''Booking Screens'''

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_booking_greeting():
    return input('''
                 
        *****************************************************************************************************************************       
        **************************************************     Welcome to Booking     ***********************************************
        *****************************************************************************************************************************
                                    
                                                                    To Exit
                                                                  [[Type 'X']]

                                        ******************************************************************
                                            When would you like your vacation to start? 
                                        ******************************************************************

        ''')

def print_user_start_date(startDate):
    print(f'''
                                        ******************************************************************
                                                        Here is your start date: {startDate}
                                        ******************************************************************
    ''')

def print_user_end_date_input():
    return input('''
                                        ******************************************************************
                                            When would you like your vacation to end? (YYYY-MM-DD)
                                        ******************************************************************
        ''')

def print_bottom_booking_screen():
    print(f'''

        *****************************************************************************************************************************
        *****************************************************************************************************************************

    ''')

def print_avaliable_properties(startDate, endDate, filtered_domiciles):

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
                
    return input('''

                                For More Details                                                        To Exit 
                            [[Enter Property Number]]                                                 [[Type 'X']]

        *****************************************************************************************************************************
        *****************************************************************************************************************************
                ''')

def print_property_details(dp):
    return input(f'''

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

def print_booking_signature(self):
    return input(f'''
                                        ************************************************************************

                                                                    *****************

                                                                    Great! Last step!

                                                                    *****************
                                            
                                                    Sign into your vacation by signing the log book!
                                   
                                                    ************************************************
                                
                                        ········································································
                                            {self.trav_obj.first_name} {self.trav_obj.last_name}
                                                Reason for visit: ''')

def print_bottom_of_signature():
    print('''                                        ········································································
                                                                                                              
    ''')

def print_booking_verification():
    print('''

                                                            **********************************
                                                            Congrats! Your vacation is booked!
                                                            **********************************

                                        ************************************************************************
                                        ************************************************************************

    ''')

'''Error Messages'''

def print_user_date_error():
    print('''
                                        ******************************************************************
                                        ╰༼=ಠਊಠ=༽╯    Please enter a valid date! (YYYY-MM-DD)    ╰༼=ಠਊಠ=༽╯
                                        ******************************************************************
    ''')

def print_valid_selection_error():
    print('''
                                                        **********************************
                                                          Please make a valid selection!
                                                        **********************************
    ''')

def print_lenny_selection_error():
    print('''
                                        ******************************************************************
                                            ╰༼=ಠਊಠ=༽╯    Please enter a valid selection!    ╰༼=ಠਊಠ=༽╯
                                        ******************************************************************
    ''')