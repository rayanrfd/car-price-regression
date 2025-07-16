import re
import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline

class CleanTitleImputer(BaseEstimator, TransformerMixin):
      
      def fit(self, X, y=None):
            return self
      
      def transform(self, X, y=None):

            #Filters initialization
            is_na = X["clean_title"].isna()
            accident_reported = X["accident"] == "At least 1 accident or damage reported"

            conditions = is_na & (~accident_reported)
            other_conditions = is_na & accident_reported

            #Data Imputation
            X.loc[conditions, "clean_title"] = "Yes"
            X.loc[other_conditions, "clean_title"] = "No"

            return X
      
class AccidentReportImputer(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
          return self

    def transform(self, X, y=None):
        """
        Impute missing accident report
        """
        X = X.copy()

        is_clean_title = X["clean_title"] == "Yes"
        accident_na = X["accident"].isna()

        conditions = is_clean_title & accident_na
        other_conditions = ~is_clean_title & accident_na

        X.loc[conditions, "accident"] = "None reported"
        X.loc[other_conditions, "accident"] = "At least 1 accident or damage reported"

        return X
    

class FuelTypeImputer(BaseEstimator, TransformerMixin):

    def __init__(self):
        self.fuel_types = ["Gasoline", "Hybrid", "E85 Flex Fuel", "Diesel", "Plug-In Hybrid", "Electric"]

    def _handle_fuel_type(self, X):
        """
        Impute missing fuel type
        """
        X = X.copy()

        #Filter initialization
        fuel_type_na = X["fuel_type"].isna()
        not_supported_type = X["fuel_type"] == "not supported"
        blank_fuel_type = X["fuel_type"] == "–"

        missing_condition = fuel_type_na | not_supported_type | blank_fuel_type

        pattern = "(" + "|".join(self.fuel_types) + ")"
        matches = X["engine"].str.extract(pattern, flags=re.IGNORECASE, expand=False)
        X.loc[missing_condition, "fuel_type"] = matches[missing_condition].fillna("Gasoline")
      
        return X

    def _replace_by_gasoline(self, X):
        #Filter initialization
        fuel_type_na = X["fuel_type"].isna()
        not_supported_type = X["fuel_type"] == "not supported"
        blank_fuel_type = X["fuel_type"] == "–"

        condition = fuel_type_na | not_supported_type | blank_fuel_type

        X.loc[condition, "fuel_type"] = "Gasoline"

        return X
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):

        X = self._handle_fuel_type(X)
        X = self._replace_by_gasoline(X)

        return X
    
class MultipleTransmissionHandler(BaseEstimator, TransformerMixin):

    def __init__(self):
        self.automatic_transmission_names = ["A/T", "Automatic", "AT", "At", "CVT", "DSG", "Powershift", "i-Shift", "Matic", "Easy-R", "Dualogic", "X-Tronic", "Multitronic", "Tiptronic"]

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):

        regex = "|".join(self.automatic_transmission_names)
        is_automatic = X["transmission"].str.contains(regex, case=False, regex=True)

        X.loc[is_automatic, "transmission"] = "Automatic"
        X.loc[~is_automatic, "transmission"] = "Manual"

        return X

data_imputer = Pipeline([
    ("clean_title_imputer", CleanTitleImputer()),
    ("accident_report_imputer", AccidentReportImputer()),
    ("fuel_type_imputer", FuelTypeImputer()),
    ("transmission_handler", MultipleTransmissionHandler()),
])
