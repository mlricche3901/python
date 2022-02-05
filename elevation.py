import requests
from bs4 import BeautifulSoup
import random
import re

#get town name and state from user
town = input("Please enter a city").lower()
state = input("Please enter a state").lower().capitalize()
t_input = town.capitalize()
s_input = state
joined_town = ""
joined_state = ""

if len(town) > 1:
    town = town.split()
    town = [name.capitalize() for name in town]
    joined_town = '_'.join(town)
    if len(state) > 1:
        state = state.split()
        state = [place.capitalize() for place in state]
        joined_state = joined_town + ',_' + '_'.join(state)
    else:
        joined_state = joined_town + ',_' + state
    #print(joined_state)

url = "https://en.wikipedia.org/wiki/" + joined_state
#create url/search wikipedia for town and state
try:
    response = requests.get(url)
except:
    print("Doesn't seem valid")

soup = BeautifulSoup(response.content, 'html.parser')

table = soup.select('tr.mergedtoprow > td.infobox-data')

#find elevation on page
print(t_input, s_input)
for item in table:
    if 'ft' in item.text:
        print("Elevation is", item.text)