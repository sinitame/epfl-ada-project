import numpy as np
import pandas as pd
from data_loading import YearLoader
import matplotlib.pyplot as plt

######################################################################################
#                     Number of accidents per years
######################################################################################

def get_number_accidents_per_years(min_year, max_year):
    """
    Function that get the number of accidents per year from
    min_year to max_year.
    
    Parameters
    ----------
    min_year : int
        First year to consider
    max_year : int
        Last year to consider
    
    Returns
    -------
    DataFrame
        DataFrame containing the result
    
    """
    accidents_per_years = {}
    for year in range(min_year, max_year+1):
        data_year = YearLoader(year)
        df_year_caracteristics = data_year.get_dataframe("characteristics")
        all_accident_ids = df_year_caracteristics["Num_Acc"].unique()
        num_accidents = len(all_accident_ids)
        accidents_per_years[str(year)] = num_accidents
        
    df_accidents_per_years = pd.Series(accidents_per_years)
    return df_accidents_per_years

def plot_number_accidents_per_years(df_accidents_per_year):
    plt.figure(figsize=(20,10))
    df_accidents_per_year.plot(kind='bar')
    plt.show()

######################################################################################
#                   Number of accidents per months
######################################################################################

def get_number_accidents_per_months(data_year):
    """
    Function that get the number of accidents per months for a year
    
    Parameters
    ----------
    data_year : YearLoader
        Data from the year
    
    Returns
    -------
    DataFrame
        DataFrame containing the result
    
    """
    accidents_per_months = {}
    months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
    df_year_caracteristics = data_year.get_dataframe("characteristics")
    
    for i, month in enumerate(months):
        df_month_caracteristics = df_year_caracteristics[df_year_caracteristics["mois"] == i+1]
        all_months_accident_ids = df_month_caracteristics["Num_Acc"].unique()
        num_accidents_in_month = len(all_months_accident_ids)
        accidents_per_months[month] = num_accidents_in_month

    df_accidents_per_months = pd.Series(accidents_per_months)
    
    return df_accidents_per_months

def plot_number_accidents_per_months(df_accidents_per_months):
    plt.figure(figsize=(20,10))
    df_accidents_per_months.plot(kind='bar')
    plt.show()

######################################################################################
#               Number of accidents per months for all years
######################################################################################

def get_number_accidents_per_months_all_years(min_year, max_year):
    """
    Function that get the number of accidents per months from
    min_year to max_year.
    
    Parameters
    ----------
    min_year : int
        First year to consider
    max_year : int
        Last year to consider
    
    Returns
    -------
    DataFrame
        DataFrame containing the result
    
    """
    all_years_accidents_per_months = {}
    for year in range(min_year, max_year+1):
        data_year = YearLoader(year)
        accidents_per_months = get_number_accidents_per_months(data_year)
        all_years_accidents_per_months[str(year)] = accidents_per_months
    
    df_all_years_accidents_per_months = pd.DataFrame(all_years_accidents_per_months)
    return df_all_years_accidents_per_months

def plot_all_years_accidents_per_months(all_accidents_per_months):
    width = 0.05 
    months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
    ind = np.arange(12)

    all_accidents_per_months.plot(kind='bar', figsize=(20,10))

    plt.ylabel('Number of accidents')
    plt.title('Number of accidents per months between 2008 and 2018')

    plt.xticks(ind, months)
    plt.legend(loc='best')
    plt.show()
    

######################################################################################
#                    Accidents gravity in a year
######################################################################################

def get_accidents_gravity(data_year):
    """
    Function that get the statistics of the gravity of accidents in a year.
    
    Parameters
    ----------
    data_year : YearLoader
        Data from the year
    
    Returns
    -------
    DataFrame
        DataFrame containing the result
    
    """
    gravity_mapping = ["Unscathed", "Dead", "Injured", "Slight injured" ]

    df_year_caracteristics = data_year.get_dataframe("passengers")
    df_accidents_gravity = df_year_caracteristics.groupby("grav")["grav"].count()
    
    return df_accidents_gravity

def plot_accidents_gravity(df_accidents_gravity):
    gravity_mapping = ["Unscathed", "Dead", "Injured", "Slight injured" ]
    ind = [i for i in range(4)]
    
    df_accidents_gravity.plot(kind='bar', figsize=(20,10))
    plt.xticks(ind, gravity_mapping, rotation=45)
    plt.show()
    
######################################################################################
#                    Accidents gravity over years
######################################################################################

def get_accidents_gravity_all_years(min_year, max_year):
    """
    Function that get the statistics of the gravity of accidents
    between min_year and max_year.
    
    Parameters
    ----------
    min_year : int
        First year to consider
    max_year : int
        Last year to consider
    
    Returns
    -------
    DataFrame
        DataFrame containing the result
    
    """
    all_years_accidents_gravity = {}
    for year in range(min_year, max_year+1):
        data_year = YearLoader(year)
        df_accidents_gravity = get_accidents_gravity(data_year)
        all_years_accidents_gravity[str(year)] = df_accidents_gravity
    
    df_all_years_accidents_gravity = pd.DataFrame(all_years_accidents_gravity)
    return df_all_years_accidents_gravity

def plot_all_years_accidents_gravity(all_years_accidents_gravity):
    width = 0.05 
    gravity_mapping = ["Unscathed", "Dead", "Injured", "Slightly injured" ]
    ind = np.arange(4)

    all_years_accidents_gravity.plot(kind='bar', figsize=(20,10))

    plt.ylabel('Number of accidents')
    plt.xlabel('Gravity of accidents')
    plt.title('Gravity of accidents between 2008 and 2018')

    plt.xticks(ind, gravity_mapping, rotation=45)
    plt.legend(loc='best')
    plt.show()

######################################################################################
#                   Number of people per accidents in a year
######################################################################################
    
def get_number_people_per_accidents(data_year):
    """
    Function that get the of the number of people
    involved per accidents in a year.
    
    Parameters
    ----------
    data_year : YearLoader
        Data from the year
    
    Returns
    -------
    DataFrame
        DataFrame containing the result
    
    """
    
    df_year_caracteristics = data_year.get_dataframe("passengers")
    df_people_per_accidents = df_year_caracteristics.groupby("Num_Acc")["Num_Acc"].count()
    
    return df_people_per_accidents

def plot_number_people_per_accidents(people_per_accidents, multiple_years=False, year=2018):
    
    people_per_accidents.hist(bins=200, figsize=(20,10))
    
    plt.ylabel('Number of people per accidents')
    plt.xlabel('Frequency')
    
    if multiple_years:
        plt.title('Histogram of the number of people per accidents between 2008 and 2018')
    else:
        plt.title('Histogram of the number of people per accidents in {}'.format(year))
    
    plt.show()

######################################################################################
#             Number of people per accidents in all dataset
######################################################################################

def get_number_people_per_accidents_all_years(min_year, max_year):
    """
    Function that get the number of people involved per accidents 
    between min_year and max_year.
    
    Parameters
    ----------
    min_year : int
        First year to consider
    max_year : int
        Last year to consider
    
    Returns
    -------
    DataFrame
        DataFrame containing the result
    
    """
    data_year = YearLoader(min_year)
    df_people_per_accidents_all = get_number_people_per_accidents(data_year)
    
    for year in range(min_year+1, max_year+1):
        data_year = YearLoader(year)
        df_people_per_accidents_year = get_number_people_per_accidents(data_year)
        pd.concat([df_people_per_accidents_all, df_people_per_accidents_year], ignore_index=True)
    
    return df_people_per_accidents_all

