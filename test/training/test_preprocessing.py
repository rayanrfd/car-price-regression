import pandas as pd
from training.custom_transformer.clean_title_imputer import *


def test_clean_title():
        
        data = {
                    "clean_title": ["Yes", None, None, "Yes"],
                    "price": [20000, 29000, 10000, 10000],
                    "accident": ["None reported", None, "None reported", None]
                }

        df = pd.DataFrame(data)
                
        new_df = handle_clean_title(df)
        assert new_df["clean_title"][1] == "Yes"
        assert new_df["clean_title"][2] == "No"

def test_accident_reported():
        
        data = {
                    "clean_title": ["Yes", "No", "No", "Yes"],
                    "price": [20000, 29000, 10000, 10000],
                    "accident": ["None reported", None, "None reported", None]
                }

        df = pd.DataFrame(data)
        new_df = handle_accident_report(df)
        assert new_df["accident"][1] == "At least 1 accident or damage reported"
        assert new_df["accident"][3] == "None reported"

def test_fuel_type():
        
        data = {
                    "engine": ["Plug-In Hybrid Engine", "Hybrid engine", "Gasoline engine", "Super dupper Electric", "Gasoline engine"],
                    "fuel_type": [None, None, "Gasoline", "not supported", "–"],
                }

        df = pd.DataFrame(data)
                
        new_df = handle_fuel_type(df)
        print(new_df.head())
        assert new_df["fuel_type"][0] == "Plug-In Hybrid"
        assert new_df["fuel_type"][1] == "Hybrid"
        assert new_df["fuel_type"][2] == "Gasoline"
        assert new_df["fuel_type"][3] == "Electric"
        assert new_df["fuel_type"][4] == "Gasoline"

