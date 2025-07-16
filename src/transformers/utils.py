import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

class ToDict(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        return X.astype(str).to_dict(orient="records")
