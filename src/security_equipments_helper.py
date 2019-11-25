# Imports

import sys
import warnings

sys.path.append('../src')
warnings.filterwarnings('ignore')

from data_loading import YearLoader


def gravity_code_to_string(grav_code):
    """
    Function that convert an accident code of gravity into its string value
    
    Parameters
    ----------
    atm_code : int
        The code of the gravity
    
    Returns
    -------
    String
        The string value
    """
    
    dict_gravity_code = {
        1 : "Unharmed",
        2 : "Killed",
        3 : "Injured and hospitalized",
        4 : "Slightly injured",
    }
    
    return dict_gravity_code[grav_code]

def get_gravity(secu_codes, year):
    """
    Function that returns a Dataframe containing for
    the given security items, the gravity and the number 
    of accidents
    
    Parameters
    ----------
    secu_codes : int
        The code(s) of the security equipment
    year : int
        The year
    
    Returns
    -------
    DataFrame
        The dataframe containing the number of accidents
    """
    
    # Load dataset
    loader = YearLoader(year)
    passengers = loader.get_dataframe("passengers")
    passengers = passengers.dropna(subset=['secu'])
    passengers['secu'] = passengers['secu'].astype(int)
    
    # Count the accidents
    pass_given_secu = passengers[passengers['secu'].apply(lambda x : x in secu_codes)]
    df_grav = pass_given_secu["grav"].value_counts().sort_index().rename_axis('grav').reset_index(name='counts')
    df_grav["grav"] = df_grav["grav"].apply(lambda x : gravity_code_to_string(x))
    
    # Adding percentage
    count = df_grav["counts"].sum()
    df_grav["perc"] = df_grav["counts"] / count * 100
    
    return df_grav.set_index('grav')
    


def get_gravity_over_years(secu_codes, years):
    df_full_grav = get_gravity(secu_codes, years[0])
    
    for year in years[1:]:
        df_grav_year = get_gravity(secu_codes, year)
        df_full_grav += df_grav_year
        
    # Fixing percentage
    count = df_full_grav["counts"].sum()
    df_full_grav["perc"] = df_full_grav["counts"]/count * 100
        
    return df_full_grav
