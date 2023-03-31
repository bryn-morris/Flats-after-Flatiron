<!-- All team notes at the bottom with the README guidance from the CLI project template! -->

# Flats after Flatiron
## Collaborators: Bryn Morris, Calvin Atkeson, & Grace Nieboer


## Introduction

This is a Command Line Interface program created during Phase III of Flatiron School's Full Stack Software Engineering Program.

This program is a reservations solution for travel lovers!
The program allows a user to "log in" to Flats After FlatIron and manage their travel plans. Basic user solutions include:

1. Browsing available destinations
2. Book a travel reservation
3. Manage current reservation information
4. Update user's "profile" information


## Languages

Python
SQL

## Program Composition
=> The following section describes each program component and its functionality

### CLI 

Users can "log in" to the program  by entering their cAsE SeNsItIvE information upon entering the program

Users are given a main menu from which to execute three main actions:
Booking a new vacation, viewing/managing current vacations and profile, and exploring.


1. Booking a vacation 
User is able to enter their desired start and end dates, and are presented with all properties available during the desired dates. User can choose to view any property in greater detail before deciding to book. User can decide to book the vacation, and will sign a "log" with the reason for their stay. Vacation will persist to database, and the user can view their newly booked vacation in their personal profile. 

2. Browse/ Explore
User may choose to explore all the different properties that out service currently has available to customers! User may browse and gain inspiration for a trip prior to booking their own travel plans. User can look at previous traveler's that have stayed in a particular domicile, and their reason for their stay.

3. View / Update 
User may manage their own personal information and manage travel plans. User name and/or location may be changed at any time. They can also view all travel reservations that have been booked through Flats after Flatiron, both previous and future reservations. 

Life happens! We do allow users to reschedule or cancel plans if the need arises. However, reservations are first-come first-serve. If someone else already has a reservation for a particular domicile, those dates are unavailable. The user may instead choose a different date OR perhaps another domicile might be available. 

We also offer free cancellation. Users may need to cancel their travel plans. If the need arises, we understand. 

#### CLI FUNCTIONS

def START()


def TRAVELER


def BOOK()


def VIEW-UPDATE()


def BROWSE










### MODELS

Our models file contains the following three models which constitute the framework for our project.db tables. 

1. Domicile
2. Travler
3. Vacation 

Domiciles can have many vacations. Travelers can have many vacations. Vacation belongs to both Traveler and Domicile.

    Traveler -----< Vacation >----- Domicile


### SEED

Seed Data generated for database using Faker and Random; 
Each time seed data is re-run, old data is first cleared from the database and new data is generated and populates the database.

8 Travelers:
    - first name: randomly generated 
    - last name randomly generated 
    - location: randomly generated city 

8 Properties:
    - property type: randomly selected choice from a property list 
    - property name: randomly selected based on random choice associated with property type 
    - sleep capacity: randomly selected based on range associated with property type
    - location: randomly generated city
    - local amenities: randomly selected choice from an amenities list

16 Vacations:
    - start date: randomly selected between 2021-01-02 and 2024-12-31
    - end date: corresponds to a start date, set to be a number of days after its start date, where the number of days is randomly selected from a range of 2 - 40 days. 
    - traveler: randomly assigned to a traveler instance in the Traveler table
    - domicile: randomly assigned to a domicile instance in the domicile table
    - reason for visit: randomly selected choice from a curated reasons list


### HELPERS

welcome_images = a tuple storing ASCII art representing several different domiciles st which one might choose to stay. This tuple is used in the CLI script to display one ASCII art piece at random when a user begins the program.  

### DEBUG

This debug is a sandbox file used only for the purposes of debugging and query selection


### What Goes into a README?

This README should serve as a template for your own- go through the important
files in your project and describe what they do. Each file that you edit
(you can ignore your Alembic files) should get at least a paragraph. Each
function should get a small blurb.

You should descibe your actual CLI script first, and with a good level of
detail. The rest should be ordered by importance to the user. (Probably
functions next, then models.)

Screenshots and links to resources that you used throughout are also useful to
users and collaborators, but a little more syntactically complicated. Only add
these in if you're feeling comfortable with Markdown.

## Team Notes

- should we refactor our CLI functions out... 
- can we include our whimsicle organization?

- still need to finish:
CLI functions
helpers
debug


