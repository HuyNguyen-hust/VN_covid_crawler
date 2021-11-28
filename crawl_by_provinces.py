from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

from selenium.webdriver.chrome.options import Options
opts = Options()
opts.add_argument("user-agent=khdl")

# create a new Chrome session
driver = webdriver.Chrome("chromedriver",options=opts)

#Get the soup
url = "https://e.vnexpress.net/covid-19/covid-19-viet-nam"
driver.get(url)
content = driver.page_source
soup = BeautifulSoup(content)

table = soup.find_all('ul', id='list-tinhthanh', attrs={'class':'list-tinhthanh'})

provinces = []
total_cases = []
deaths = []
yesterday_deaths = []
for idx, province in enumerate(table[0]):
    if idx == 0:
        continue
    info = province.find_all('div')
    info = [figure.text for figure in info]
    provinces.append(info[0])
    total_cases.append(int(info[1].replace(',', '')))
    deaths.append(int(info[3].replace(',', '')))
    yesterday_deaths.append(None if info[4] == '-' else int(info[4].replace(',', '')))

d = {'provinces': provinces, 'total_cases': total_cases, 'deaths': deaths, 'yesterday_deaths': yesterday_deaths}
pd.DataFrame(data = d).to_csv('covid_on_provinces.csv',index=True)