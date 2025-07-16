import pandas as pd
from src.transformers.imputer import data_imputer

data = pd.read_csv("data/train.csv")
data = data_imputer.transform(data)
useless_columns = ["price", "id", "engine", "model", "ext_col", "int_col"]

with open("data/brands.txt", "w") as file:
    for col in data.drop(useless_columns, axis=1).columns:
        if data[col].dtype == "object":
            file.write(f'{col.capitalize()}\n')
            file.write(f'\n')
            for value in set(data[col]):
                file.write(f'{value.lower().replace("-", "_").replace(" ", "_")} = "{value}"\n')
            file.write(f'\n')
