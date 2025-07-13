import pandas as pd
from training.utils import *


def test_clean_title():
        
        data = {
                    "clean_title": ["Yes", None, None, "Yes"],
                    "price": [20000, 29000, 10000, 10000],
                    "accident": ["Not reported", None, "Not reported", None]
                }

        df = pd.DataFrame(data)
                
        new_df = handle_clean_title(df)
        assert new_df["clean_title"][1] == "Yes"
        assert new_df["clean_title"][2] == "Yes"

def test_fuel_type():
        
        data = {
                    "engine": ["Plug-In Hybrid Engine", "Hybrid engine", "Gasoline engine", "Super dupper Electric", "Gasoline engine"],
                    "fuel_type": [None, None, "Gasoline", "not reported", "–"],
                }

        df = pd.DataFrame(data)
                
        new_df = handle_fuel_type(df)
        print(new_df.head())
        assert new_df["fuel_type"][1] == "Hybrid"
        assert new_df["fuel_type"][3] == "Electric"
