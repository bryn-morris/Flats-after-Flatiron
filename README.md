<!-- All team notes at the bottom with the README guidance from the CLI project template! -->


# Flats after Flatiron
## Collaborators: Bryn Morris, Calvin Atkeson, & Grace Nieboer


## Introduction

This is a Command Line Interface program created during Phase III of Flatiron School's  Full Stack Software Engineering Program.

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
=> The following sections describe program components and their functionality

### CLI 

Users can "log in" to the program  by entering their cAsE SeNsItIvE information upon entering the program

#### CLI FUNCTIONS








### MODELS


### SEED

Seed Data generated for database using Faker and Random; 

Each time seed data is re-run, old data is cleared and new data is generated.

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
    - start date: 
    - end date
    - traveler: randomly assigned to a traveler instance in the Traveler table
    - domicile: randomly assigned to a domicile instance in the domicile table
    - reason for visit: randomly selected choice from a curated reasons list


### HELPERS

Welcome  Images:


### DEBUG



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
