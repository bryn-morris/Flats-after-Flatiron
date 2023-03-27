from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Vacation,Domicile,Traveler
from faker import Faker
from random import random

if __name__ == '__main__':
    engine = create_engine('sqlite:///project.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    faker = Faker()

    # Clearing DataBase Before Running File again

    session.query(Vacation).delete()
    session.query(Domicile).delete()
    session.query(Traveler).delete()

    # Populating Traveler List with Faker

    i = 0
    sample_travelers = []
    while i <=5:
        sample_travelers.append({"first_name": faker.first_name(),
                         "last_name": faker.last_name(), 
                         "location": faker.city()})
        i += 1

    # Creating Traveler Instances with Faker Data
    
    created_travelers = []

    for trav in sample_travelers:
    
        newTraveller = Traveler(
            first_name = trav["first_name"],
            last_name = trav["last_name"],
            location = trav["location"]
        )

        created_travelers.append(newTraveller)
        session.add(newTraveller)
        session.commit()
    
    # Populating Domicile List

    sample_properties = [{"sc": random.randint(2,6),
                         "p_type": "Beach House", 
                         },{"sc": random.randint(1,4),
                         "p_type": "Bunker", 
                         },{"sc": random.randint(1,2),
                         "p_type": "Space Shuttle", 
                         },{"sc": random.randint(4,8),
                         "p_type": "Yacht", 
                         },{"sc": random.randint(1,1),
                         "p_type": "Barrel", 
                         },{"sc": random.randint(10,30),
                         "p_type": "Castle", 
                         } 
                        ]

    n = 0
    sample_domiciles = []

    while n <=5:

        random_property = random.choice(sample_properties)

        sample_domiciles.append({"dest_location": faker.city(),
                         "sleep_capacity": random_property["sc"], 
                         "local_amenities": "SAMPLE",
                         "property_type": random_property["p_type"]})
        n += 1

    # Creating Domicile Instances

    created_domiciles = []
    
    for dom in sample_domiciles:
    
        newDomicile = Domicile(
            dest_location = dom["dest_location"],
            sleep_capacity = dom["sleep_capacity"],
            local_amenities = dom["local_amenities"],
            property_type = dom["property_type"]
        )

        created_domiciles.append(newDomicile)
        session.add(newDomicile)
        session.commit()

    # Creating Vacation Instances

    sample_vacation_dates = [{"ed": "6-7-2018",
                            "sd": "5-20-2018", 
                            },{"ed": "9-16-2022",
                            "sd": "9-14-2022", 
                            },{"ed": "2-3-2022",
                            "sd": "12-2-2022", 
                            },{"ed": "5-16-2020",
                            "sd": "5-3-2020", 
                            },{"ed": "8-19-2021",
                            "sd":"8-1-2021"},
                            {"ed": "6-12-2022",
                            "sd":"6-3-2022"},
                            ]
    
    for dateset in sample_vacation_dates:

        newVacation = Vacation(
            start_date = dateset["sd"],
            end_date = dateset["ed"],
            Traveler_id = random.choice(created_travelers).id,
            Domicile_id = random.choice(created_domiciles).id
        )

        session.add(newVacation)
        session.commit()

    session.close()