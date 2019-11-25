import pandas as pd
import numpy as np

def get_car_injuries_df(data, dead_only=False):
    """Create a DataFrame (place, count) .


    Parameters
    ----------
    data : YearLoader
        Dataset loading class.
        
    dead_only : bool
        only generate DataFrame for death

    Returns
    -------
    pandas.DataFrame
        Injuries count for each sit.

    """
    passengers = data.get_dataframe("passengers")
    
    if dead_only:
        return pd.DataFrame(passengers[passengers['grav']==2]['place'].dropna().value_counts())
    else:
        return pd.DataFrame(passengers['place'].dropna().value_counts())
