# Example file for Advanced Python: Hands On by Joe Marini
# Using the reduce function

import json
from functools import reduce

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# TODO: how much snowfall is in the entire dataset?
# reduce function takes a few parameters. The first is a callback function. There are two arguments in this callback function
# the first is an accumulator and the second is the element. We then need the data we want to run on and the initial value of
# the accumulator. 
total_snowfall = reduce(lambda acc, elem: acc + elem['snow'], weatherdata, 0)

# TODO: how much total precipitation is in the entire dataset?
total_snowfall_precip = reduce(lambda acc, elem: acc + (elem['snow']+elem['prcp']), weatherdata, 0)

# TODO: What was the warmest day in which it snowed? Need to find highest 'tmax' for all
# days where 'snow' > 0
def warm_snow_day(acc, elem):
    # return the elem value if the snow amount > 0 and its tmax value is
    # larger than the tmax value that is in the acc argument
    return elem if elem['snow'] > 0 and elem['tmax'] > acc['tmax'] else acc

# define a "zero" value start date for the reduce function to start with
start_val = {
    "date": "1900-01-01",
    "tmin": 0,
    "tmax": 0,
    "prcp": 0.0,
    "snow": 0.0,
    "snwd": 0.0,
    "awnd": 0.0
}

# TODO: reduce the data set to the warmest snow day
solution = reduce(warm_snow_day, weatherdata, start_val)
print(solution)