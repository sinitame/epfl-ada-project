# Exploring French National Traffic injuries data

# Abstract
The demand for road transportation and the rate of motorization have continued to increase in all cities around the world. However, this increase demand and the preference for private transport are at the root of many problems, among which road accidents. In fact, the number of accidents has continued to increase, with disastrous consequences. 
With this project, we aim to analyze the causes and effects of this phenomenon. We would like to investigate the correlation between the gravity level of a road accident and the components of the traffic system composed of the road, the driver and the vehicule. These components can be described by variables illustrating the drivers behavior, the attributes of the vehicle operated, the quality of the road and the climatic conditions. 

The dataset we are going to use is extracted from an official [French open source database platform](https://www.data.gouv.fr/fr/). The dataset is provided by the [French road safety observatory (ONISR)](https://www.onisr.securite-routiere.interieur.gouv.fr/en) and is composed of more than 474,000 accidents from 2005 to 2018. It can be found [here](https://www.data.gouv.fr/en/datasets/base-de-donnees-accidents-corporels-de-la-circulation/) 

# Research questions

- Are there trends in the number of accidents over time?
- Is there a link between driver (age, gender, ..) and accidents ?
- Are there roads which are more dangerous than others ?
- How much weather conditions influence accident rates ?
- Are there some conditions (weather, location, ..) that can affect the dangerousness of accidents ?

# Dataset

The main dataset that we will use for this study is : [French road safety observatory (ONISR) dataset](https://www.data.gouv.fr/en/datasets/base-de-donnees-accidents-corporels-de-la-circulation/).

It includes, for each personal injury accident (i.e. an accident on a road open to public traffic) involving at least one vehicle and causing at least one victim requiring treatment, the following informations:

#### Characteristics:
- Accident ID
- Date and time
- Localization (Department, town, type of road)
- Weather condition
- Collision type 
- Geographical coordinates

#### Location:
- Accident ID
- Road type (Highway, National road, Departmental road, ..)
- Road number
- Road traffic direction and number of lanes
- Road informations (elevation, curve, road surface,
- Type of infrastructure (tunnel, bridge, crossroads, ..)

#### Vehicles:
- Accident ID
- Vehicle ID
- Traffic direction
- Vehicle category (motorcycle, car, bus, scooter, ...)
- Fixed obstacle hit (tree, metal slide, wall, ...
- Mobil obstacle hit (pedestrian, vehicle, animal, ..)
- Initial shock point (front, back, ..)
- Last driving maneuver before accident
- Number of occupant

#### Users:
- Accident ID
- Vehicle ID
- User category (driver, passenger)
- Accident gravity (dead, injured patient, light injured, ..)
- Gender
- Year of birth
- Reason of traveling (Home - work, Home - school, ..)
- Existence of a safety equipment (belt, helmet, ..)
- Use of a safety equipment (yes, no)
- Pedestrian informations (localization, if moving or not, ..)

Our results are visually presented as cards and time charts.

We wanted to couple this dataset with the radar annual flash recordings, weather conditions and road maintenance dates in order to testify some common sense assumptions. However, after a deeper look on the dataset, we noticed that we had enough data to explore for our data story.

Possible databases we could have explored:

* [Radar informations database](https://www.data.gouv.fr/en/datasets/radars-automatiques-bilans-annuels-du-nombre-de-flashs/)

# A list of internal milestones until milestone 2

- [x] Explore the quality of the data and check its consistency over years (2018 seems to have more informations than previous years -> Same informations, just a different way to categorize accidents gravity between 2018 and previous years)
- [x] Plot the evolution of specific features over time (Number of accidents years/months)
- [x] Get hands on map visualization tools to plot some insights on a map of France. (D3.js tutorials under test)
- [x] Develop helper functions to help use aggregate our different data sources (we decided to use only one dataset so no more needed)
- [x] Develop functions to generate relevant data for each part of the data story (introduction, part 1, part 2, part 3, part 4)

# Detailed plan of the Data Story

The goal of our data story will be to explore some key insights of the dataset by making a story about how to reduce your chance of dying in a road accident. By reading the story, the reader will be able to see what are the main factors of road accidents regarding different aspects about drivers (age, sexe, ..), places where accidents occurs (type of roads, departements, ..), moments when accidents occurs (during the year, month, day or with specific weather conditions) and security equipements (if the driver had its belt, the impact of security equipment on the gravity of the accident, ..).

At the end, the story will depict the "perfect" ride to avoid an accident by looking at the best possible case for each insight (the one having the less fatal accidents rate).

### Introduction

- Number of accidents (see if there is any trend) 
- Evolution over the years
- Gravity, number of injuries, ...

### 1. Be the right person ..

- Population Pyramids (passengers and drivers): (Men, woman, age)

- Types of vehicles

### 2. At the right place ..

- Accidents per regions/departments (map of France)

- Injuries visualization in the car (Heat-map from the car top)

### 3. At the right moment ..

- Trends histograms

- Weather conditions

- Road conditions

### 4. Security

- Security equipment usage

- Impact on the gravity of accidents

#### Conclusion

All the data we will use for the data story is available in [Milestone 3 Notebook](notebooks/milestone-3.ipynb)  
The script that we will use to generate and plot all the data [Data generation script](src/)  

The link to our Data Story is [Data Story](https://epfl-ada-project.github.io/)  

# Contributions

#### Ambroise
- Development of helpers to visualize and generate CSV to extract insights
- Design of the data story timeline
- Development of the website
- Verification of milestone 2
- Plot interactive map

#### Emrick
- Development of helpers to visualize and generate CSV to extract insights
- Generation of plots for the website
- Design of the website figures
- Design of the data story timeline
- Readme

#### Gautier
- Design of the data story timeline
- Development of helpers to load the data and extract insights
- Verification of milestone 3
- Text redaction of the data story
- Clean the code for final project rendering

#### Linah
- Compute some stats insights
- Completion of milestone 3
- Design of the data story timeline
- Text redaction of the data story
- Abstract and verification of the readme



