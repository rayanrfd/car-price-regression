

data_imputer = Pipeline([
    ("clean_title_imputer", CleanTitleImputer()),
    ("accident_report_imputer", AccidentReportImputer()),
    ("fuel_type_imputer", FuelTypeImputer()),
    ("transmission_handler", MultipleTransmissionHandler()),
])

hasher_pipeline = Pipeline([
    ("to_dict", ToDict()),
    ("hash_encoder", FeatureHasher(n_features=1024, input_type="dict"))
])

preprocessor = ColumnTransformer([
    ("hash_encoding", hasher_pipeline, ["model", "engine"]),
    ("one_hot_encoder", OneHotEncoder(handle_unknown="ignore"), ["clean_title", "accident", "transmission"]),
    ("target_encoder", TargetEncoder(), ["ext_col", "int_col", "brand", "fuel_type"])
])

pipeline = Pipeline([
    ("imputer", data_imputer),
    ("preprocessing", preprocessor),
    ("regressor", GradientBoostingRegressor())
])
