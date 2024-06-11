# Example file for Advanced Python: Hands On by Joe Marini
# Introspect the data to make some determinations

import json
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# TODO: What was the warmest day in the data set?
warmday = max(weatherdata, key=lambda x:x['tmax'])
print(f"the warmest day was {warmday['date']} at {warmday['tmax']} degrees")
# TODO: What was the coldest day in the data set?
coldday = min(weatherdata, key = lambda x:x['tmin'])
print(f"the coldest day was {coldday['date']} at {coldday['tmin']} degrees")
# TODO: How many days had snowfall?
snowdays = [day for day in weatherdata if day['snow'] > 0]
print(len(snowdays))
