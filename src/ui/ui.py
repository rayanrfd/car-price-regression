import streamlit as st
import requests
import json

from src.api.model.brand import brand_list, Brand
from src.api.model.car import Accident, CarModel, CleanTitle, FuelType, Transmission


st.title("Car Price Estimator")

brand = st.selectbox("What is your car's brand ?", brand_list)

st.write("What is you model year ?")
model_year = st.slider("Model Year", 1990, 2025, 2020)

st.write("What is you car milage ?")
milage = st.slider("Milage", 0, 50000, 1000)

fuel_type = st.selectbox("What is your car fuel type ?", ("Hybrid", "Electric", "E85 Flex Fuel", "Diesel", "Plug-In Hybrid", "Gasoline"))

transmission = st.selectbox("What is your car transmission type ?", ("Manual", "Automatic"))

accident = st.selectbox("Is there an accident reported ?", ("At least 1 accident or damage reported", "None reported"))

clean_title = st.selectbox("Is your car title clean ?", ("Yes", "No"))

car_data = CarModel(
    brand=Brand(brand),
    model_year=model_year,
    milage=milage,
    fuel_type=FuelType(fuel_type),
    transmission=Transmission(transmission),
    accident=Accident(accident),
    clean_title=CleanTitle(clean_title)
)

if st.button("Estimate"):
    res = requests.post(
        url="http://127.0.0.1:8000",
        data=car_data.model_dump_json(),
        headers={
            "Content-Type": "application/json"
        }
    )

    price = float(res.text)

    st.subheader(f"Estimation : {price:.2f}$")
