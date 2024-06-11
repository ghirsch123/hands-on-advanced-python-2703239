# Example file for Advanced Python: Hands On by Joe Marini
# Sort the data in a sequence

import json
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# create a subset of the data for days that had snowfall
dataset = list(filter(lambda d: d['snow'] > 0.0, weatherdata))

# sort the entire data set by how much snowfall there was
# TODO: method 1: use the sorted() function to create a new list
sorted_dataset = sorted(dataset, key = lambda d:d['snow'], reverse=True) # creates a new sorted list

# TODO: method 2: use the sort() function that every list has to sort in-place
dataset.sort(key=lambda d:d['snow'], reverse = True) # sorts original list

# TODO: Sort on multiple fields: first by snowfall, then by average wind speed
sorted_dataset2 = sorted(dataset, key = lambda d:(d['snow'], d['awnd']), reverse=True)

print(sorted_dataset2)