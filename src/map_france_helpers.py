from data_loading import *
import numpy as np
import seaborn as sns
import math
import matplotlib.pyplot as plt


def get_dep_count_df(data):
    """Create a DataFrame (dep, count) counting number of injuries per depertment.

    Parameters
    ----------
    data : YearLoader
        Dataset loading class.

    Returns
    -------
    pandas.DataFrame
        dep_count DataFrame.

    """
    characteristics = data.get_dataframe('characteristics')

    # Format dep
    # Remove 0 at the end of dep number if the dep number is not DOM-TOM
    characteristics['dep'] = characteristics.apply(lambda x: x.dep//10 if x.dep<971 else x.dep, axis=1)
    # Add 0 in front of dep number if dep number is lower than 10
    characteristics['dep'] = characteristics.apply(lambda x: '0'+str(x.dep) if x.dep<10 else str(x.dep), axis=1)

    # Count values per dep
    dep_count = pd.DataFrame(characteristics['dep'].value_counts())
    dep_count.reset_index(level=0, inplace=True)
    dep_count.rename(columns={'index':'dep',
                              'dep':'count'},
                     inplace=True)
    return dep_count
