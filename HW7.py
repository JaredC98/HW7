# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 10:56:49 2022

@author: Jared
"""
#import modules
import requests as req
from sys import argv
from bs4 import BeautifulSoup as soup

#define lat and long based on command line inputs
lat = argv[1]
long = argv[2]

#use {0} and {1} formatting instead, to simplify code
#use 'lat' and 'long' to complete the URL, then access it
page = 'https://forecast.weather.gov/MapClick.php?lat='+lat+'&lon='+long
site = req.get(page)

#check if the page is unavailable
if site.status_code != 200:
    print('Broken Link \n')
    
else:
    days = []
    conds = []
    highs = []
    lows = []
    outH = open('web.txt', 'w', encoding = 'utf-16')
    outF = open('output.txt','w')
    
    #get the html of the page, make it readable, and write to 'web.txt'
    html = soup(site.text, 'html.parser')
    outH.write(html.prettify())
    
    #find city name
    city_cont = html.find('div',{'id':'seven-day-forecast'})
    city = city_cont.find('h2',{'class':'panel-title'}).text
    city = city.strip()
    #find container of data cells
    contain = html.find_all('div', {'id' : 'seven-day-forecast-container'})
    #find the cells in the container
    cell = contain[0].find_all('div', {'class' : 'tombstone-container'})
    
    #a loop to find the day, conditions, and high/lows in each cells
    for i in range(0, len(cell)):
        day = cell[i].find('p', {'class' : 'period-name'}).text
        day = day.replace('Night',' Night')
        days.append(day)
        cond = cell[i].find('p', {'class' : 'short-desc'}).text
        conds.append(cond)
        if 'night' in day or 'Night' in day:
            low = cell[i].find('p',{'class':'temp temp-low'}).text
            low = low.replace(' °F','').replace('Low: ','')
            lows.append(low)
        else:
           high = cell[i].find('p', {'class':'temp temp-high'}).text
           high = high.replace(' °F','').replace('High: ','')
           highs.append(high)
           
#replace the first day/night with the respective day-of-week
#consider making module??
if 'Sunday' in days[-1]:
    days[0] = 'Wednesday'
    days[1] = 'Wednesday Night'
elif 'Monday' in days[-1]:
    days[0] = 'Thursday'
    days[1] = 'Thursday Night'
elif 'Tuesday' in days[-1]:
    days[0] = 'Friday'
    days[1] = 'Friday Night'
elif 'Wednesday' in days[-1]:
    days[0] = 'Saturday'
    days[1] = 'Saturday Night'
elif 'Thursday' in days[-1]:
    days[0] = 'Sunday'
    days[1] = 'Sunday Night'
elif 'Friday' in days[-1]:
    days[0] = 'Monday'
    days[1] = 'Monday Night'
elif 'Saturday' in days[-1]:
    days[0] = 'Tuesday'
    days[1] = 'Tuesday Night'

#begin outputting the data
#output the day
#output the descriptiong
#output the high/low

#create a chart of highs/lows
#output the days, centered
#output High
#output the high for that day, centered
#output Low
#output the low for that day, centered