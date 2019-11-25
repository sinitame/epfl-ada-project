# Exploring French National Trafic injuries data

# Abstract
The demand for road transportation and the rate of motorization have continued to increase in all cities around the world. However, this increase demand and the preference for private transport are at the root of many problems, among which road accidents. In fact, the number of accidents has continued to increase, with disastrous consequences. 
With this project, we aim to analyze the causes and effects of this phenomenon. We would like to investigate the correlation between the gravity level of a road accident and the components of the traffic system composed of the road, the driver and the vehicule. These components can be described by variables illustrating the drivers behavior, the attributes of the vehicle operated, the quality of the road and the climatic conditions. 

The dataset we are going to use is extracted from an official [French open source database platform](https://www.data.gouv.fr/fr/). The dataset is provided by the [French road safety observatory (ONISR)](https://www.onisr.securite-routiere.interieur.gouv.fr/en) and is composed of more than 474,000 accidents from 2005 to 2018. It can be found [here](https://www.data.gouv.fr/en/datasets/base-de-donnees-accidents-corporels-de-la-circulation/) 

# Research questions

- Are there trends in the number of accidents over time?
- Is there a link between driver (age, sexe, ..) and accidents ?
- Are there roads which are more dangerous than others ?
- What is the influence of radars on the accident rate in a given road ?
- How much weather conditions influence accident rates ?
- Are there some conditions (weather, location, ..) that can affect the dangerousness of accidents ?

# Dataset

The main dataset that we will use for this study is : [French road safety observatory (ONISR) dataset](https://www.data.gouv.fr/en/datasets/base-de-donnees-accidents-corporels-de-la-circulation/).

It includes, for each personal injury accident (i.e. an accident on a road open to public traffic) involving at least one vehicle and causing at least one victim requiring treatment, the following informations:

#### Characteristics:
- Accident ID
- Date and time
- Localisation (Departement, town, type of road)
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
- Mobil obstacle hit (pedestrien, vehicle, animal, ..)
- Initial shock point (front, back, ..)
- Last driving maneuver before accident
- Number of occupant

#### Users:
- Accident ID
- Vehicle ID
- User category (driver, passenger)
- Accident gravity (dead, injured patient, light injured, ..)
- Sexe
- Year of birth
- Reason of traveling (Home - work, Home - school, ..)
- Existence of a safety equipment (belt, helmet, ..)
- Use of a safety equipement (yes, no)
- Pedestrien informations (localisation, if moving or not, ..)

We would like to couple this dataset with the radar annual flash recordings, weather conditions and road maintenance dates in order to testify some common sense assumptions. We expect our results to be visually presented as cards and time charts.

Possible databases we could explore:

* [Radar informations database](https://www.data.gouv.fr/en/datasets/radars-automatiques-bilans-annuels-du-nombre-de-flashs/)

# A list of internal milestones until milestone 2

- [x] Explore the quality of the data and check its consitancy over years (2018 seems to have more informations than previous years -> Same informations, just a different way to categorize accidents gravity between 2018 and previous years)
- [x] Plot the evolution of specific features over time (Number of accidents years/months)
- [x] Get hands on map visualization tools to plot some insights on a map of France. (D3.js tutorials under test)
- [x] Develop helper functions to help use agregate our different data sources (we decided to use only one dataset so no more needed)
- [x] Develop functions to generate relevant data for each part of the data story (introduction, part 1, part 2, part 3, part 4)

# Detailed plan of the Data Story

The goal of our data story will be to explore some key insights of the dataset by making a story about how to reduce your chance of dying in a road accident. By reading the story, the reader will be able to see what are the main factors of road accidents regarding different aspects about drivers (age, sexe, ..), places where accidents occurs (type of roads, departements, ..), moments when accidents occurs (during the year, month, day or with specific weather conditions) and security equipements (if the driver had its belt, the impact of security equipment on the gravity of the accident, ..).

At the end, the story will depict the "perfect" ride to avoid an accident by looking at the best possible case for each insight (the one having the less fatal accidents rate).

### Introduction

- Number of accidents (see if there is any trend) 
- Evolution over the years
- Gravity, number of injuries, ...

### 1. Be the right person ..

- Population Pyramids (driver): (Men, woman, age)

- Types of vehicules

### 2. At the right place ..

- Accidents per regions/departments (map of France)

- Injuries vizualization in the car (Heatmap from the car top)

### 3. At the right moment ..

- Trends histograms

- Weather conditions

- Road conditions

### 4. Security

- Security equipement usage

- Impact on the gravity of accidents

#### Conclusion

All the data we will use for the data story is available in [Milestone 2 Notebook](notebooks/milestone-2.ipynb)

The script that we will use to generate all the data (will be available soon in) [Data generation script]()



