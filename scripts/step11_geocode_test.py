import pandas as pd
from geopy.geocoders import Nominatim
import time

print("Loading reduced locations...")

df = pd.read_csv("../output/reduced_locations.csv")

# Take small sample
sample = df.head(10)

geolocator = Nominatim(user_agent="brts_project")

def get_location(lat,lon):
    try:
        location = geolocator.reverse(f"{lat},{lon}")
        if location:
            return location.address
        else:
            return "Unknown"
    except:
        return "Error"

print("Testing geocoding...")

sample['LocationName'] = sample.apply(
    lambda row: get_location(row['Lat_round'],row['Lon_round']),
    axis=1
)

print(sample)