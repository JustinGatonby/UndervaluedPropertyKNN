import pandas as pd 
from geopy.geocoders import Nominatim
# Set up the geocoder 
geolocator = Nominatim(user_agent="property_geocoder")

def location(data):
    # Apply the functions to each row in the Location column to get latitude and longitude
    data["Latitude"] = data['Location'].apply(get_latitude)
    data["Longitude"] = data['Location'].apply(get_longitude)
    # Save the updated data 
    data.to_csv('property_data(1).csv', index=False)

def get_latitude(location):
    try:
        # Add "Cape Town, South Africa" to make sure we get the right place
        place = f"{location}, Cape Town, South Africa"
        location_data = geolocator.geocode(place)
        if location_data:
            return location_data.latitude 
        else:
            return None 
    except:
        return None

def get_longitude(location):
    try:
        place = f"{location}, Cape Town, South Africa"
        location_data = geolocator.geocode(place)
        if location_data:
            return location_data.longitude  
        else:
            return None
    except:
        return None

def main():
    # Read in data scraped from Property24
    data = pd.read_csv("property_data.csv")
    location(data)
if __name__ == "__main__": main() 
