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
    while i <=7:
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
                         },{"sc": random.randint(2,5),
                         "p_type": "Cottage", 
                         },{"sc": random.randint(1,2),
                         "p_type": "Yurt", 
                         },{"sc": random.randint(5,9),
                         "p_type": "Mansion", 
                         },{"sc": random.randint(3,5),
                         "p_type": "Farmhouse", 
                         } 
                        ]
    
    amenities_list= (
                    "There is a kitchen somewhere around here...",
                    "Waterpark but it's filled with snakes",
                    "A duck pond but all of the ducks have a taste for human flesh",
                    "Greg",
                    "Sometimes at night you can hear whispers on the wind...",
                    "The nearby town only appears every 100 years!",
                    "A dark, cozy hole to sleep in",
                    "Electric Jello",
                    "A musty old library nobody ever comes out of",
                    "Shrek's Swamp",

                    )

    n = 0
    sample_domiciles = []

    while n <=7:

        random_property = random.choice(sample_properties)

        sample_domiciles.append({"dest_location": faker.city(),
                         "sleep_capacity": random_property["sc"], 
                         "local_amenities": random.choice(amenities_list),
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

    reason_table = [
        "Running from the spider in my room : (",
        "I'm not sure, I just woke up here!",
        "I'm just here for the bug convention",
        "Ghosts",
        "My in-laws were in town, had to get away",
        "In search of the biggest macaroon",
        "Fleeing the Balrog", 
        "Weekend at Bernie's", 
        "Visiting my cousin's ex-hair stylist's uncle's hamster",
        "To collect as many hotel toiletries as possible",
        "Blind date with @Bigfoot"
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