from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Vacation,Domicile,Traveler
from faker import Faker
import random
from datetime import datetime, date, timedelta

if __name__ == '__main__':
    engine = create_engine('sqlite:///lib/db/project.db')
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

# Need to update Amenties into list that is randomly generated

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

    sample_vacation_dates = []

    k=0
    while k <= 15:
        sample_vacation_dates.append(str(faker.date_between_dates(date_start=datetime(2021,1,1), date_end=datetime(2024,12,31)))) 
        k += 1

    # sample_vacation_dates = [{"ed": date.fromisoformat("2018-06-07"),
    #                         "sd": date.fromisoformat("2018-05-20"), 
    #                         },{"ed": date.fromisoformat("2022-09-16"),
    #                         "sd": date.fromisoformat("2022-09-14"), 
    #                         },{"ed": date.fromisoformat("2023-02-03"),
    #                         "sd": date.fromisoformat("2022-12-02"), 
    #                         },{"ed": date.fromisoformat("2020-05-16"),
    #                         "sd": date.fromisoformat("2020-05-03"), 
    #                         },{"ed": date.fromisoformat("2021-08-19"),
    #                         "sd":date.fromisoformat("2021-08-01")},
    #                         {"ed": date.fromisoformat("2022-06-12"),
    #                         "sd":date.fromisoformat("2022-06-03")},
    #                         ]

    reason_table = [
        "Running from the spider in my room : (",
        "Family Vacation!",
        "Business Trip, on the company's dime",
        "I'm not sure, I just woke up here!",
        "I'm just here for the bug convention",
        "Ghosts"
        ]
    
    for dateset in sample_vacation_dates:

        newVacation = Vacation(
            start_date = date.fromisoformat(dateset),
            end_date = date.fromisoformat(dateset)+timedelta(days=random.choice(range(2,40))),
            Traveler_id = random.choice(created_travelers).id,
            Domicile_id = random.choice(created_domiciles).id,
            rsn_for_visit = random.choice(reason_table)
        )
        
        session.add(newVacation)
        session.commit()

    session.close()