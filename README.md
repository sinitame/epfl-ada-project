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

# A list of internal milestones up until project milestone 2

- Explore the quality of the data and check its consitancy over years (2018 seems to have more informations than previous years)
- Plot the evolution of specific features over time
- Get hands on map visualization tools to plot some insights on a map of France.
- Develop helper functions to help use agregate our different data sources (link a road with radar informations, a location with weather informations)


# Questions for TAa

- Should we use only one year of data (2018) or multiple years (2005->2018) ?
- Can we use an API to gather some of our data ? If yes do you know a good one for weather data ?

