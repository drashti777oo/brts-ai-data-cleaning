import pandas as pd
from geopy.geocoders import Nominatim
import time

print("Loading reduced locations...")

df = pd.read_csv("../output/reduced_locations.csv")

geolocator = Nominatim(user_agent="brts_project")

locations = []

def get_location(lat,lon):
    try:
        location = geolocator.reverse(f"{lat},{lon}")
        if location:
            return location.address
        else:
            return "Unknown"
    except:
        return "Error"

print("Starting geocoding...")

for i,row in df.iterrows():

    lat = row['Lat_round']
    lon = row['Lon_round']

    loc = get_location(lat,lon)

    locations.append(loc)

    # Progress print
    if i % 50 == 0:
        print("Processed:",i)

    # Delay to avoid blocking
    time.sleep(1)

df['LocationName'] = locations

df.to_csv("../output/location_lookup.csv",index=False)

print("Location lookup completed")