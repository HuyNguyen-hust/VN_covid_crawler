import requests
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt
 
# URL for scrapping data
url = 'https://www.worldometers.info/coronavirus/country/viet-nam/'
 
# get URL html
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

covid_data = dict()

def convert_to_list(text):
  l = text[1:-1].split(',')
  return [None if (x == 'null') else int(x) for x in l]

lines = str(soup).splitlines()

for line in lines:
  if 'name: \'' in line:
    tmp_name = re.search("'.+'", line).group()
  if 'data: [' in line:
    tmp_list = convert_to_list(re.search("\[.+\d\]", line).group())
    covid_data[tmp_name] = tmp_list

#covid data for last month
#for item in covid_data:
#  print(item)
#  print(covid_data[item][-30:])

