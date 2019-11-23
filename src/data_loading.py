import pandas as pd

class YearLoader:
    """
    This class represents data for one year.
    
    Parameters
    ----------
    year : int
        Year the data to be load
    
    Attributes
    ----------
    default_encoding : str
        Encoding used to load data in dataframe
    
    default_mapping_csv : dict
        Mapping between english csv names and french csv names
        
    dataframes: dict
        Dictionnary containing all dataFrames for a year (keys in english)
    
    """

    def __init__(self, year):
        self.default_encoding = "ISO-8859-1"
        self.default_mapping_csv = {
            "characteristics": "caracteristiques",
            "locations"      : "lieux",
            "passengers"     : "usagers",
            "vehicles"       : "vehicules"
        }

        separator = ""
        delimiter = ""

        # Handle exceptions in file paths
        if int(year) <= 2016:
            separator = "_"
        else:
            separator = "-"
        
        if int(year) == 2009:
            delimiter = "\t"
        else:
            delimiter = ","
    
        self.dataframes = {}
        for k, v in self.default_mapping_csv.items():
            self.dataframes.update({k:pd.read_csv("../data/{2}/{0}{1}{2}.csv".format(v, separator, year), encoding=self.default_encoding, delimiter=delimiter)})
    
    def get_dataframe(self, name):
        return self.dataframes[name]



