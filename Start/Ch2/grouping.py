# Example file for Advanced Python: Hands On by Joe Marini
# Arrange data into groups

import json
from collections import defaultdict
import pprint
from itertools import groupby
# groupby needs sorted data

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# get all the measurements for a particular year
year = [day for day in weatherdata if "2022" in day['date']]

# create manual grouping of days that had a certain level of precipitation
year.sort(key=lambda d:d['prcp'])
datagroup = defaultdict(list)
for d in year:
    datagroup[d['prcp']].append(d['date'])
#print(f"{len(datagroup)} total precipitation groups")
#pprint.pp(datagroup)

# TODO: Use groupby to get the days of a given year by how much precipitation happened
grouped = {k: list (v) for k,v in groupby(year, key = lambda d:d['prcp'])}

# TODO: How many groups do we have? Now we can use len() on the dictionary
print(len(grouped))

# TODO: we can iterate over the dictionary to list each group
for key, data in grouped.items():
    print(f"Precip: {key}, # days {len(data)}, days: {list(map(lambda d:d['date'], data))}")