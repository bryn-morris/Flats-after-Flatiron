# from db.models import Vacation, Traveler, Domicile
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker


# class CLI():

#     domiciles = session.query(Domicile).all()
#     # what does this return?

#     travelers = [traveler for traveler in session.query(Traveler)]
#     # what does this format return?

#     vacations = session.query(Vacation).all()

#     def __init__(self, user_fn, user_ln, user_city):
#         self.first_name = user_fn
#         self.last_name = user_ln
#         self.city = user_city

#     @property
#     def traveler(self):
#         for t in CLI.travelers:
#             if t.first_name == self.first_name and t.last_name == self.last_name:
#                 return t
            
#         new_traveler = Traveler(self.first_name, self.last_name, self.city)
#         session.add(new_traveler)
#         session.commit()
#         return new_traveler
    
#     def start(self):
#         pass
    
#     def showDomiciles(self):
#             print(f"Property Type:{d.property_type}, Location: {d.dest_location}" for d in CLI.domiciles)

#     def showData(self):
#         user_action = input("Type D to see a list of Domiciles, V to see a list of vacations booked: ")
#         print(' ')

#         if user_action == 'D' or user_action == 'd':
#             showDomiciles()
#         elif user_action == 'V' or user_action == 'v':
#             pass
