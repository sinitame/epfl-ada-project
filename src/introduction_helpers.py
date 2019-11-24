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