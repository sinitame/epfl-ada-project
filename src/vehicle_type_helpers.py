import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def get_vehicles_type_df(data, top_k):
    """Create a DataFrame (catv).

    Count number of vehicles per category

    Parameters
    ----------
    data : YearLoader
        Dataset loading class.
    top_k : int
        get top_k value.

    Returns
    -------
    pandas.DataFrame
        Vehicles categories count DataFrame.

    """
    types = {
        1 : 'Bicyclette',
        2 : 'Cyclomoteur <50cm3',
        3 : 'Voiturette (Quadricycle à moteur carrossé) (anciennement "voiturette ou tricycle à moteur")',
        4 : 'Référence plus utilisée depuis 2006 (scooter immatriculé)',
        5 : 'Référence plus utilisée depuis 2006 (motocyclette)',
        6 : 'Référence plus utilisée depuis 2006 (side-car)',
        7 : 'VL seul',
        8 : 'Catégorie plus utilisée (VL + caravane)',
        9 : 'Catégorie plus utilisée (VL + remorque)',
        10 : 'VU seul 1,5T <= PTAC <= 3,5T avec ou sans remorque (anciennement VU seul 1,5T <= PTAC <= 3,5T)',
        11 : 'Référence plus utilisée depuis 2006 (VU (10) + caravane)',
        12 : 'Référence plus utilisée depuis 2006 (VU (10) + remorque)',
        13 : 'PL seul 3,5T <PTCA <= 7,5T',
        14 : 'PL seul > 7,5T',
        15 : 'PL > 3,5T + remorque',
        16 : 'Tracteur routier seul',
        17 : 'Tracteur routier + semi-remorque',
        18 : 'Référence plus utilisée depuis 2006 (transport en commun)',
        19 : 'Référence plus utilisée depuis 2006 (tramway)',
        20 : 'Engin spécial',
        21 : 'Tracteur agricole',
        30 : 'Scooter < 50 cm3',
        31 : 'Motocyclette > 50 cm3 et <= 125 cm3',
        32 : 'Scooter >50cm3 et<=125cm3',
        33 : 'Motocyclette > 125 cm3',
        34 : 'Scooter > 125 cm3',
        35 : 'Quad léger <= 50 cm3 (Quadricycle à moteur non carrossé)',
        36 : 'Quad lourd > 50 cm3 (Quadricycle à moteur non carrossé)',
        37 : 'Autobus',
        38 : 'Autocar',
        39 : 'Train',
        40 : 'Tramway',
        99 : 'Autre véhicule'
    }

    # Get vehicles DataFrame
    vehicles = data.get_dataframe("vehicles")

    # Count vehicles per category
    vehicles_cat = pd.DataFrame(vehicles['catv'].value_counts())
    vehicles_cat.index = vehicles_cat.apply(lambda x: types.get(x.name), axis =1)
    # Get top k
    top_k_name = vehicles_cat.nlargest(top_k, 'catv', keep='first').index.values
    # If in top k => keep name, else name=>'other'
    vehicles_cat.index = vehicles_cat.apply(lambda x: x.name if x.name in top_k_name else 'other', axis=1)
    vehicles_cat = vehicles_cat.groupby(vehicles_cat.index).sum(axis=1)

    return vehicles_cat


def plot_vehicles_cat(df, figsize=(10,10)):
    """Bar plot number of vehicle per category.


    Parameters
    ----------
    df : pandas.DataFrame
         vehicle per category count DataFrame (get_vehicles_type_df() function).

    """
    df.plot.pie(y='catv', figsize=figsize)
    plt.show()
