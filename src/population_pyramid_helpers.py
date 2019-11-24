from data_loading import *
import numpy as np
import seaborn as sns
import math
import pandas as pd
import matplotlib.pyplot as plt

def get_dead_alive_gender_df(data):
    """Create a DataFrame (male_dead, male_alive, female_dead, female_alive) for each age group.

    If the age can't be computed or age is greater than 150 years old, age_group is '?'.

    Parameters
    ----------
    data : YearLoader
        Dataset loading class.

    Returns
    -------
    pandas.DataFrame
        Dead/Alive count for each age-group and gender

    """
    # Load passengers dataset
    passengers = data.get_dataframe("passengers")
    year = data.year
    
    
    # Compute dead/alive for female/male
    passengers['male_dead'] = passengers.apply(lambda x: 1 if x.grav==2 and x.sexe==1 else 0, axis=1)
    passengers['male_alive'] = passengers.apply(lambda x: 1 if x.grav!=2 and x.sexe==1 else 0, axis=1)
    passengers['female_dead'] = passengers.apply(lambda x: 1 if x.grav==2 and x.sexe==2 else 0, axis=1)
    passengers['female_alive'] = passengers.apply(lambda x: 1 if x.grav!=2 and x.sexe==2 else 0, axis=1)
    
    # Compute age
    passengers['age_group'] = passengers.apply(lambda x: 15 if math.isnan(x.an_nais) else int((year - x.an_nais)//10), axis=1)
    pyramid_data = passengers[['male_dead', 'male_alive', 'female_dead', 'female_alive', 'age_group']]
    
    pyramid_data = pyramid_data.groupby(['age_group']).sum(axis=1).sort_values('age_group')#.drop('sort', axis=1)
    pyramid_data.reset_index(level=0, inplace=True)
    # Age categorie to age group
    pyramid_data['age_group'] = pyramid_data.apply(lambda x : '?' if x.age_group ==15 else str(x.age_group)+'0-'+str(x.age_group+1)+'0', axis=1)
    
    return pyramid_data


def plot_pyramid_dead_alive_gender(df, female=False, male=True, figsize=(10,10), xlim = None):
    """Plot population pyramid (male_dead, male_alive, female_dead, female_alive) for each age group.

    Parameters
    ----------
    df : pandas.DataFrame
        pyramid_data (get_dead_alive_gender_df() function).
    female : bool
        show female plot.
    male : bool
        show male plot.
    figsize : tuple
        (x, y) figsize for plots.
    xlim : tuple
        (min,max) x axis limits.
    """

    if male:
        fig_male, axes_male = plt.subplots(ncols=2, sharey=True, figsize=figsize)
        axes_male[0].barh(pyramid_data['age_group'], pyramid_data['male_alive'], align='center', color='green')
        axes_male[1].barh(pyramid_data['age_group'], pyramid_data['male_dead'], align='center', color='red')
        axes_male[0].set_xlim(xlim)
        axes_male[1].set_xlim(xlim)
        axes_male[0].invert_xaxis()
        axes_male[0].legend(['male alive'])
        axes_male[1].legend(['male dead'])
        plt.show()
        
    if female:
        
        fig_female, axes_female = plt.subplots(ncols=2, sharey=True, figsize=figsize)
        axes_female[0].barh(pyramid_data['age_group'], pyramid_data['female_alive'], align='center', color='green')
        axes_female[1].barh(pyramid_data['age_group'], pyramid_data['female_dead'], align='center', color='red')
        axes_female[0].set_xlim(xlim)
        axes_female[1].set_xlim(xlim)
        axes_female[0].invert_xaxis()
        axes_female[0].legend(['female alive'])
        axes_female[1].legend(['female dead'])

        plt.show()

