import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def get_vehicles_type_df(data):
    """Create a DataFrame (catv).

    Count number of vehicles per category

    Parameters
    ----------
    data : YearLoader
        Dataset loading class.

    Returns
    -------
    pandas.DataFrame
        Vehicles categories count DataFrame.

    """

    # Get vehicles DataFrame
    vehicles = data.get_dataframe("vehicles")

    # Count vehicles per category
    vehicles_cat = pd.DataFrame(vehicles['catv'].value_counts())

    return vehicles_cat

def plot_vehicles_cat(df, figsize=(10,10)):
    """Bar plot number of vehicle per category.


    Parameters
    ----------
    df : pandas.DataFrame
         vehicle per category count DataFrame (get_vehicles_type_df() function).

    """
    df.plot(kind='bar', figsize=figsize)
    plt.show()
