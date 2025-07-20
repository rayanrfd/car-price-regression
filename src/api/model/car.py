from pydantic import BaseModel
from enum import Enum
from .brand import Brand

class FuelType(str, Enum):
    hybrid = "Hybrid"
    electric = "Electric"
    e85_flex_fuel = "E85 Flex Fuel"
    diesel = "Diesel"
    plug_in_hybrid = "Plug-In Hybrid"
    gasoline = "Gasoline"

class Transmission(str, Enum):
    automatic = "Automatic"
    manual = "Manual"

class Accident(str, Enum):
    at_least_1_accident_or_damage_reported = "At least 1 accident or damage reported"
    none_reported = "None reported"

class CleanTitle(str, Enum):
    yes = "Yes"
    no = "No"

class CarModel(BaseModel):
    brand: Brand
    model_year: int
    milage: int
    fuel_type: FuelType
    transmission: Transmission
    accident: Accident
    clean_title: CleanTitle
