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
    random_mansion = ["Bly Manor", "Hillhouse", "Pemberly Estate", "Wuthering Heights", "Rottbrandt Residence", "Thornfield Hall", ]
    random_farmhouse = ["Tara Farmhouse", "The Ingles Family Farm", "Green Gables", "The Farm", "The Farmhouse", "The Tenant Farmhouse"]
    random_boat = ["S.S. Venture", "Jenny", "The Inferno", "The Black Pearl", "The Pequod", "The Spinacher",  "The Titanic"]
    random_barrel = ["The Cask of Amontillado", "A Plastic Drum", "The Splintery Barrel", "A High-Density Polyethylene Barrel", "A Whiskey Barrel", "The Drunken Keg"]
    random_castle = ["Dracula Castle", "Castle Black", "Castle Blanca", "The Dark Tower", "Hogwarts", "Elsa's Ice Palace"]
    random_cottage = ["Grandma's Cottage", "Thoreau's Cabin", "The Gingerbread House", "The Folly", "Pemberly Cottage", "Briar Rose Cottage" ]
    random_yurt = ["A Mongolian Ger", "A Tibetan Yurt", "A Kyrgyz Yurt", "A Kazakh Yurt"]
    random_bunker = ["10 Cloverfield Lane", "The War Room", "Area 51 Bunker", "The Burlington Bunker", "Whitehouse Bunker", "Greenbrier Bunker", "The Hive"]
    random_spaceshuttle = ["The Enterprise", "Discovery", "Atlantis", "Millenium Falcon", "Serenity", "Challenger"]
    random_beachhouse = ["Grace's Beach House", "Island Escape", "Windward Cottage", "Pelican House", "Coral Cottage", "Blue Bungalow" ]
    
    
    #if there's time, we can add sample amenities to be tied to each sample property
    # could we extrapolate these random lists into a table?

    
   
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

        sample_properties = [{"sc": random.randint(2,6),
                         "p_type": "Beach House",
                         "name": random.choice(random_beachhouse) 
                         },{"sc": random.randint(1,4),
                         "p_type": "Bunker", 
                         "name": random.choice(random_bunker)
                         },{"sc": random.randint(1,2),
                         "p_type": "Space Shuttle",
                         "name": random.choice(random_spaceshuttle) 
                         },{"sc": random.randint(4,8),
                         "p_type": "Boat",
                         "name" : random.choice(random_boat)
                         },{"sc": random.randint(1,1),
                         "p_type": "Barrel",
                         "name": random.choice(random_barrel) 
                         },{"sc": random.randint(10,30),
                         "p_type": "Castle",
                         "name": random.choice(random_castle) 
                         },{"sc": random.randint(2,5),
                         "p_type": "Cottage",
                         "name": random.choice(random_cottage) 
                         },{"sc": random.randint(1,2),
                         "p_type": "Yurt",
                         "name": random.choice(random_yurt) 
                         },{"sc": random.randint(5,9),
                         "p_type": "Mansion", 
                         "name": random.choice(random_mansion)
                         },{"sc": random.randint(3,5),
                         "p_type": "Farmhouse", 
                         "name": random.choice(random_farmhouse)
                         } 
                        ]

        random_property = random.choice(sample_properties)

        if random_property["p_type"] != "Space Shuttle":
            sample_domiciles.append({ "name": random_property["name"],
                            "dest_location": faker.city(),
                            "sleep_capacity": random_property["sc"], 
                            "local_amenities": random.choice(amenities_list),
                            "property_type": random_property["p_type"]})
            n += 1
        else:
            sample_domiciles.append({ "name": random_property["name"],
                            "dest_location": "Somewhere in Space!",
                            "sleep_capacity": random_property["sc"], 
                            "local_amenities": random.choice(amenities_list),
                            "property_type": random_property["p_type"]})

    # Creating Domicile Instances

    created_domiciles = []
    
    for dom in sample_domiciles:
    
        newDomicile = Domicile(
            name = dom["name"],
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