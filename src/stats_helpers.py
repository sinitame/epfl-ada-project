from scipy.stats import chi2
import scipy.stats as ss
import pandas as pd

from data_loading import *
from security_equipments_helper import *
from weather_road_conditions_helpers import *

import numpy as np
import seaborn as sns
import math
import matplotlib.pyplot as plt


def ChiSquare(x,y):
    
    contingency_table=pd.crosstab(x,y)
    print('contingency_table :-\n',contingency_table)

    #Observed Values
    Observed_Values = contingency_table.values 
    print("Observed Values :-\n",Observed_Values)
    b=ss.chi2_contingency(contingency_table)
    Expected_Values = b[3]
    print("Expected Values :-\n",Expected_Values)
    no_of_rows=len(contingency_table.iloc[0:2,0])
    no_of_columns=len(contingency_table.iloc[0,0:2])
    ddof=(no_of_rows-1)*(no_of_columns-1)
    print("Degree of Freedom:-",ddof)
    alpha = 0.05
    chi_square=sum([(o-e)**2./e for o,e in zip(Observed_Values,Expected_Values)])
    chi_square_statistic=chi_square[0]+chi_square[1]
    print("chi-square statistic:-",chi_square_statistic)
    critical_value=chi2.ppf(q=1-alpha,df=ddof)
    print('critical_value:',critical_value)
    #p-value
    p_value=1-chi2.cdf(x=chi_square_statistic,df=ddof)
    print('p-value:',p_value)
    print('Significance level: ',alpha)
    print('Degree of Freedom: ',ddof)
    print('chi-square statistic:',chi_square_statistic)
    print('critical_value:',critical_value)
    print('p-value:',p_value)
    if chi_square_statistic>=critical_value:
        print("Chi-square test result : Reject H0, There is a relationship between 2 categorical variables")
    else:
        print("Chi-square test result : Retain H0, There is no relationship between 2 categorical variables")

    if p_value<=alpha:
        print("Reject H0 with 95% level of confidence.")
    else:
        print("Retain H0  with 95% level of confidence.")
        

def plot_gender_vs_gravity_contingency(data) :
    
    data = data.get_dataframe("passengers")
    x = data['sexe']
    y = data['grav']
    contingency_table=pd.crosstab(x,y)

    #Assigns the frequency values
    malecount = contingency_table.iloc[0][0:4].values
    femalecount = contingency_table.iloc[1][0:4].values

    #Plots the bar chart
    fig = plt.figure(figsize=(10, 5))
    categories = ["Unscathed","Dead","Injured","Slightly injured"]
    p1 = plt.bar(categories, malecount, 0.55, color='#d62728')
    p2 = plt.bar(categories, femalecount, 0.55, bottom=malecount)
    plt.legend((p2[0], p1[0]), ('Female', 'Male'))
    plt.xlabel('Gravity of the accidents')
    plt.ylabel('Count')
    
    plt.show()
    
    #Plot the pie plot for each gender
    
    #Male
    ax1 = contingency_table.iloc[0][0:4].plot.pie(y='grav',autopct='%1.1f%%',figsize=(10, 5))
    plt.title('Male exposition to accidents')
    plt.legend(categories, title="Gravity",bbox_to_anchor=(1,0), loc="lower right",bbox_transform=plt.gcf().transFigure)
    
    plt.show()
    
    #Female
    ax2 = contingency_table.iloc[1][0:4].plot.pie(y='grav',autopct='%1.1f%%',figsize=(10, 5))
    plt.title('Female exposition to accidents')
    plt.legend(categories, title="Gravity",bbox_to_anchor=(1,0), loc="lower right",bbox_transform=plt.gcf().transFigure)
    
    plt.show()
    
def stats_df_security_gravity(secu_codes, years):
    
    """
    Function that returns a Dataframe containing for each accident that happenned over the years 2008 to 2018,
    the given security items and the gravity, to be used for a statistical analysis
    
    Parameters
    ----------
    secu_codes : int
        The code(s) of the security equipment
    year : int
        The year
    
    Returns
    -------
    DataFrame
        The dataframe containing for each accident, the gravity and corresponding security equipement used
    """
    
    # Load dataset
    loader = YearLoader(years[0])
    passengers = loader.get_dataframe("passengers")
    passengers = passengers.dropna(subset=['secu'])
    passengers['secu'] = passengers['secu'].astype(int)
    
    pass_given_secu = passengers[passengers['secu'].apply(lambda x : x in secu_codes)]
    df_full_grav = pd.DataFrame(data=pass_given_secu,columns=['grav','secu'])
    
    for year in years[1:]:
        df_grav_year = pass_given_secu
        df_full_grav.append(df_grav_year) 
        

    return df_full_grav
    
def plot_seatbelt_vs_gravity_contingency() : 
    
    #Get the contingency
    
    years = list(range(2008, 2019))
    codes_seatbelt = [11]
    codes_no_seatbelt = [12]
    
    belt_vs_gravity = pd.DataFrame(columns = ['Seatbelt','No Seatbelt'])
    df_belt = get_gravity_over_years(codes_seatbelt, years)
    df_no_belt = get_gravity_over_years(codes_no_seatbelt, years)

    belt_vs_gravity['Seatbelt'] = df_belt['counts']
    belt_vs_gravity['No Seatbelt'] = df_no_belt['counts']

    #Separate between Killed and Alive (sum of Injured, Slightly injured and Unharmed)
    belt_vs_gravity = belt_vs_gravity.append(pd.Series([df_belt['counts'][0]+df_belt['counts'][2]+df_belt['counts'][3],df_no_belt['counts'][0]+df_no_belt['counts'][2]+df_no_belt['counts'][3]],index = belt_vs_gravity.columns),ignore_index=True)
    belt_vs_gravity.drop(belt_vs_gravity.index[[0,2,3]],inplace = True)
    belt_vs_gravity.rename(index={1: "Killed", 4: "Alive"}, inplace = True)

    belt_vs_gravity['Seatbelt'] = belt_vs_gravity['Seatbelt'] / belt_vs_gravity['Seatbelt'].sum() * 100
    belt_vs_gravity['No Seatbelt'] = belt_vs_gravity['No Seatbelt'] / belt_vs_gravity['No Seatbelt'].sum() * 100

    contingency_table = belt_vs_gravity.T
    
    #Plot the contingency

    ax1 = contingency_table.iloc[0][:].plot.pie(figsize=(10,5),autopct='%1.1f%%')
    plt.show()
    ax2 = contingency_table.iloc[1][:].plot.pie(figsize=(10,5),autopct='%1.1f%%')
    plt.show()
    
def stats_df_weather_gravity(years):
    """
    Function that returns a Dataframe containing for each passenger, the gravity of injuries and weather conditions

    Parameters
    ----------
    year : int
        The year

    Returns
    -------
    DataFrame
        The dataframe containing the gravity and weather condition of each passenger
    """

    df_full = pd.DataFrame()
    
    for year in years:
        
        # Load the dataset
        loader = YearLoader(year)
        charac = loader.get_dataframe('characteristics')
        charac = charac.dropna(subset=['atm'])
        charac['atm'] = charac['atm'].astype(int)
        
        # Empty dataset for the results
        df_year = pd.DataFrame(columns = ['grav','atm'])

        # Merging the weather and passenger dataframes on the Accident IDs
        passengers = loader.get_dataframe("passengers")
        df_merge = pd.merge(charac, passengers, on='Num_Acc')

        df_year['grav'] = df_merge['grav']
        df_year['atm'] = df_merge['atm']

        df_full = df_full.append(df_year, ignore_index=True)
    
    return df_full

def plot_weather_vs_gravity_contingency() :
    
    years = list(range(2008, 2019))
    data = stats_df_weather_gravity(years)
    contingency_table=pd.crosstab(data['atm'],data['grav'])

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


    contingency_table['Alive'] = contingency_table[1] + contingency_table[3] + contingency_table[4] 
    contingency_table.drop(columns = [1,3,4],inplace = True)
    contingency_table.rename(columns={2: "Killed"}, inplace = True)
    contingency_table.rename(index=dict_atm_code, inplace = True)

    contingency_table['Perc_Killed'] = (contingency_table['Killed'] /(contingency_table['Alive'] + contingency_table['Killed']) )*100
    
    #Plot the bar plot : 
    
    #Assigns the frequency values
    killed_perc = contingency_table['Perc_Killed']

    #Plots the bar chart
    fig = plt.figure(figsize=(10, 5))
    categories = dict_atm_code.values()

    p = plt.bar(categories, killed_perc, 0.55, color='#d62728')
    plt.xticks(rotation=50)
    plt.xlabel('Weather conditions')
    plt.ylabel('% Killed / Weather')

    plt.show()

