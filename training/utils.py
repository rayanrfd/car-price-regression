import pandas as pd
import numpy as np


def convert_to_num(dataset, columns):
        """
        Convert the price values form "$10000" format to float
        """
        dataset[columns] = dataset[columns].as_type

        return dataset

def handle_clean_title(dataset):
    """
    Impute missing values of the clean title column based on the EDA
    """
    #Filters initialization
    clean_title_na = dataset["clean_title"].isna()
    price_higher_15k = dataset["price"] > 15000
    accident_not_reported = dataset["accident"] != "None reported"

    conditions = clean_title_na & price_higher_15k & accident_not_reported
    other_conditions = (~(price_higher_15k | accident_not_reported)) & clean_title_na

    #Data Imputation
    dataset.loc[conditions, "clean_title"] = "Yes"
    dataset.loc[other_conditions, "clean_title"] = "No"

    return dataset

def handle_accident_report(dataset):
      """
      Impute missing accident report
      """
      clean_title = dataset["clean_title"] == "Yes"
      accident_na = dataset["accident"].isna()

      conditions = clean_title & accident_na
      other_conditions = ~clean_title & accident_na

      dataset.loc[conditions, "accident"] = "None reported"
      dataset.loc[other_conditions, "accident"] = "At least 1 accident or damage reported"

      return dataset

fuel_types = ["Gasoline", "Hybrid", "E85 Flex Fuel", "Diesel", "Plug-In Hybrid", "Electric"]

def handle_fuel_type(dataset):
      """
      Impute missing fuel type
      """

      #Filter initialization
      fuel_type_na = dataset["fuel_type"].isna()
      not_supported_type = dataset["fuel_type"] == "not reported"
      blank_fuel_type = dataset["fuel_type"] == "–"

      condition = fuel_type_na | not_supported_type | blank_fuel_type

      for fuel_type in fuel_types:
            filt = dataset["engine"].str.contains(fuel_type, case=False, na=False) & condition
            dataset.loc[filt, "fuel_type"] = fuel_type
      
      #dataset.loc[fuel_type_na, "fuel_type"] = "Gasoline"
    
      return dataset
