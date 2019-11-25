# Imports
import sys
import pandas as pd
import warnings

sys.path.append('../src')
warnings.filterwarnings('ignore')

from data_loading import YearLoader


def atm_code_to_str(atm_code):
    """
    Function that convert an atmospheric code to its string value
    
    Parameters
    ----------
    atm_code : int
        The code of the atmospheric conditions
    
    Returns
    -------
    String
        The string value
    """
    
    dict_atm_code = {
        1 : "Normal",
        2 : "Light rainfall",
        3 : "Heavy rainfall",
        4 : "Snow - hail",
        5 : "Fog - smoke",
        6 : "Strong wind - storm",
        7 : "Dazzling weather",
        8 : "Covered weather",
        9 : "Other",
    }
    
    return dict_atm_code[atm_code]



def gravity_code_to_string(grav_code):
    """
    Function that convert a code of gravity to its string value
    
    Parameters
    ----------
    grav_code : int
        The code of the accident's gravity
    
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


def get_accident_per_weather(year):
    """
    Function that returns a Dataframe containing for each type 
    of weather the count and the percentage of accidents
    
    Parameters
    ----------
    year : int
        The year
    
    Returns
    -------
    DataFrame
        The dataframe containing the number of accidents
    """
    
    # Load the dataset
    loader = YearLoader(year)
    charac = loader.get_dataframe('characteristics')
    charac = charac.dropna(subset=['atm'])
    charac['atm'] = charac['atm'].astype(int)
    
    # Extract the count of accidents
    df_accidents = charac["atm"].value_counts().sort_index().rename_axis('weather').reset_index(name='accidents')
    df_accidents["weather"] = df_accidents["weather"].apply(lambda x : atm_code_to_str(x))
    # Adding percentage
    count = df_accidents["accidents"].sum()
    df_accidents["perc"] = df_accidents["accidents"] / count * 100
    
    return df_accidents.set_index('weather')




def get_accident_per_weather_years(years):
    """
    Function that returns a Dataframe containing for each type 
    of weather the count and the percentage of accidents given
    multiple years
    
    Parameters
    ----------
    years : list(int)
        The list of the years
    
    Returns
    -------
    DataFrame
        The dataframe containing the number of accidents
    """
    
    df_full = get_accident_per_weather(years[0])
    
    for year in years[1:]:
        df_year = get_accident_per_weather(year)
        df_full += df_year
    
    # Fixing percentages
    count = df_full["accidents"].sum()
    df_full["perc"] = df_full["accidents"]/count * 100
        
    return df_full



def grav_weather_year(year):
    """
    Function that returns a Dataframe containing 
    for a year the count of accidents and the 
    percentage given a gravity 
    
    Parameters
    ----------
    year : int
        The year
    
    Returns
    -------
    DataFrame
        The dataframe containing the number of accidents
    """
    
    # Loading datasets
    loader = YearLoader(year)
    charac = loader.get_dataframe('characteristics')
    charac = charac.dropna(subset=['atm'])
    charac['atm'] = charac['atm'].astype(int)
    
    # Empty dataset for the results
    df_full = pd.DataFrame()
    
    for atm in range(1, 10):
        # Loop for each atm condition
        
        # Keeping only the number of the accidents given the atm code
        df_atm = charac[charac["atm"] == atm]
        list_accidents = df_atm["Num_Acc"]
        
        # Keeping the passengers of the previous accidents
        passengers = loader.get_dataframe("passengers")
        passengers = passengers[passengers["Num_Acc"].isin(list_accidents)]
        
        # Counting the gravity of the accidents
        df_res = passengers["grav"].value_counts().sort_index().rename_axis('grav').reset_index(name='counts')        
        
        # Adding percentage and atm code
        sum_acc = df_res["counts"].sum()
        df_res["perc"] = df_res["counts"] / sum_acc * 100 # Adding percentage
        df_res["atm"] = atm                                 # Add atm code
        
        # Append to full dataset
        df_full = df_full.append(df_res)
    
    # Codes to strings
    df_full["atm"] = df_full["atm"].apply(lambda x : atm_code_to_str(x))
    df_full["grav"] = df_full["grav"].apply(lambda x : gravity_code_to_string(x))
    
    # Set correct indexes
    df_full = df_full.set_index(["atm", "grav"])
    
    return df_full



def grav_weather_over_years(years):
    """
    Function that returns a Dataframe containing 
    for several years the count of accidents and 
    the percentage given a gravity 
    
    Parameters
    ----------
    years : list(int)
        The years
    
    Returns
    -------
    DataFrame
        The dataframe containing the number of accidents
    """
    
    df_res = grav_weather_year(years[0])
    
    # Adding results
    for year in years[1:]:
        df_res = df_res + grav_weather_year(year)
    
    # Fixing percentages   
    # Get count of acc for each atm
    dict_count = df_res.groupby(["atm"]).sum(columns=["counts"]).to_dict()["counts"]
    # Reset index to access all fields
    df_res = df_res.reset_index()
    for i in range(len(df_res)):
        # Compute percentages
        df_res.ix[i, "perc"] = df_res.iloc[i]["counts"] * 100 / dict_count[df_res.iloc[i]["atm"]]
    
    return df_res.set_index(["atm", "grav"])


######################
#   Road conditions  #
######################


def surf_code_to_string(surf_code):
    """
    Function that convert the code of a 
    road surface into its string value
    
    Parameters
    ----------
    surf_code : int
        The code of the road's surface
    
    Returns
    -------
    String
        The string value
    """
        
    dict_surf_code = {
        0 : "Other",
        1 : "Normal",
        2 : "Wet",
        3 : "Puddles",
        4 : "Flooded",
        5 : "Snowy",
        6 : "Muddy",
        7 : "Icy",
        8 : "Greasy substance - oil",
        9 : "Other",
    }
    
    return dict_surf_code[surf_code]

def get_accident_per_road_conditions(year):
    """
    Function that returns a Dataframe containing 
    for a specific year the count of accidents and
    the percentage for each road condition
    
    Parameters
    ----------
    year : int
        The year
    
    Returns
    -------
    DataFrame
        The dataframe containing the number of accidents
    """
    
    loader = YearLoader(year)
    locations = loader.get_dataframe('locations')
    locations = locations.dropna(subset=['surf'])
    locations['surf'] = locations['surf'].astype(int)
    # 0 are considered as "Other"
    locations['surf'] = locations['surf'].apply(lambda x : 9 if x == 0 else x)
    
    df_accidents = locations["surf"].value_counts().sort_index().rename_axis('surface').reset_index(name='accidents')
    # Getting the code into string
    df_accidents["surface"] = df_accidents["surface"].apply(lambda x : surf_code_to_string(x))
    # Adding percentage
    count_accidents = df_accidents["accidents"].sum()
    df_accidents["perc"] = df_accidents["accidents"] / count_accidents * 100
    
    return df_accidents.set_index('surface')
    
    
    
    
def get_accident_per_road_conditions_years(years):
    """
    Function that returns a Dataframe containing 
    for a several years the count of accidents 
    for each road condition
    
    Parameters
    ----------
    years : list(int)
        The years
    
    Returns
    -------
    DataFrame
        The dataframe containing the number of accidents
    """
    
    df_full = get_accident_per_road_conditions(years[0])
    
    for year in years[1:]:
        df_year = get_accident_per_road_conditions(year)
        df_full += df_year
    
    # Fixing percentages
    count = df_full["accidents"].sum()
    df_full["perc"] = df_full["accidents"]/count * 100
    
    return df_full


def grav_surface_year(year):
    """
    Function that returns a Dataframe containing 
    for a specific year the count of accidents 
    for each road condition and type of gravity
    
    Parameters
    ----------
    year : int
        The year
    
    Returns
    -------
    DataFrame
        The dataframe containing the number of accidents
    """
        
    # Loading datasets
    loader = YearLoader(year)
    locations = loader.get_dataframe('locations')
    locations = locations.dropna(subset=['surf'])
    locations['surf'] = locations['surf'].astype(int)
    # 0 are considered as "Other"
    locations['surf'] = locations['surf'].apply(lambda x : 9 if x == 0 else x)
    
    # Empty dataset for the results
    df_full = pd.DataFrame()
    
    for surf in range(1, 10):
        # Loop for each road surface condition
        
        # Keeping only the number of the accidents given the surf code
        df_surf = locations[locations["surf"] == surf]
        list_accidents = df_surf["Num_Acc"]
        
        # Keeping the passengers of the previous accidents
        passengers = loader.get_dataframe("passengers")
        passengers = passengers[passengers["Num_Acc"].isin(list_accidents)]
        
        # Counting the gravity of the accidents
        df_res = passengers["grav"].value_counts().sort_index().rename_axis('grav').reset_index(name='counts')        
        
        # Adding percentage and atm code
        sum_acc = df_res["counts"].sum()
        df_res["perc"] = df_res["counts"] / sum_acc * 100 # Adding percentage
        df_res["surf"] = surf                             # Add atm code
        
        # Append to full dataset
        df_full = df_full.append(df_res)
    
    # Codes to strings
    df_full["surf"] = df_full["surf"].apply(lambda x : surf_code_to_string(x))
    df_full["grav"] = df_full["grav"].apply(lambda x : gravity_code_to_string(x))
    
    # Set correct indexes
    df_full = df_full.set_index(["surf", "grav"])
    
    return df_full


def grav_surface_over_years(years):
    """
    Function that returns a Dataframe containing 
    for a several year the count of accidents 
    for each road condition and type of gravity
    
    Parameters
    ----------
    year : int
        The year
    
    Returns
    -------
    DataFrame
        The dataframe containing the number of accidents
    """
    
    df_res = grav_surface_year(years[0])
    
    # Adding results
    for year in years[1:]:
        df_res = df_res + grav_surface_year(year)
    
    ## Fixing percentages ##
    # Get count of acc for each surface
    dict_count = df_res.groupby(["surf"]).sum(columns=["counts"]).to_dict()["counts"]
    # Reset index to access all fields
    df_res = df_res.reset_index()
    
    for i in range(len(df_res)):
        # Compute percentages
        df_res.ix[i, "perc"] = df_res.iloc[i]["counts"] * 100 / dict_count[df_res.iloc[i]["surf"]]
    
    return df_res.set_index(["surf", "grav"])
