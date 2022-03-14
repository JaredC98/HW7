# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 10:56:49 2022

@author: Jared
"""
#import modules
import requests as req
from sys import argv
from bs4 import BeautifulSoup as soup

'''USER-DEFINED CITY'''
#define lat and long based on command line inputs
lat = argv[1]
long = argv[2]

#use 'lat' and 'long' to complete the URL, then access it
#CHANGE 0 AND 1 TO 1 AND 2???????????????????????????????????????????????????????????????????
page = 'https://forecast.weather.gov/MapClick.php?lat={0}&lon={1}'
page = page.format(lat,long)
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
        cond = cell[i].find('p', {'class' : 'short-desc'}).get_text(separator=' ')
        conds.append(cond)
        if 'night' in day or 'Night' in day:
            low = cell[i].find('p',{'class':'temp temp-low'}).text
            #removes any non-digit characters from the temperature
            #below was a previous method, but it was not as robust
            #low = low.replace(' °F','').replace('Low: ','')
            num_fil = filter(str.isdigit, low)
            num_str = ''.join(num_fil)
            low = num_str
            lows.append(low)
        else:
           high = cell[i].find('p', {'class':'temp temp-high'}).text
           #removes any non-digit characters from the temperature
           #below was a previous method, but it was not as robust
           #high = high.replace(' °F','').replace('High: ','')
           num_fil = filter(str.isdigit, high)
           num_str = ''.join(num_fil)
           high = num_str
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

'''PRE-DEFINED CITY'''
#all variables are the same as above, but with "p_" preceeding them
#define lat and long based on command line inputs
p_lat = str(39.32920000000007)
p_long = str(-82.09978499999994)

#use {0} and {1} formatting instead, to simplify code
#use 'lat' and 'long' to complete the URL, then access it
p_page = 'https://forecast.weather.gov/MapClick.php?lat='+p_lat+'&lon='+p_long
p_site = req.get(p_page)

#check if the page is unavailable
if p_site.status_code != 200:
    print('Broken Link \n')
    
else:
    p_days = []
    p_conds = []
    p_highs = []
    p_lows = []
    outH = open('web.txt', 'w', encoding = 'utf-16')
    
    #get the html of the page, make it readable, and write to 'web.txt'
    p_html = soup(p_site.text, 'html.parser')
    outH.write(p_html.prettify())
    
    #find city name
    p_city_cont = p_html.find('div',{'id':'seven-day-forecast'})
    p_city = p_city_cont.find('h2',{'class':'panel-title'}).text
    p_city = p_city.strip()
    #find container of data cells
    p_contain = p_html.find_all('div', {'id' : 'seven-day-forecast-container'})
    #find the cells in the container
    p_cell = p_contain[0].find_all('div', {'class' : 'tombstone-container'})
    
    #a loop to find the day, conditions, and high/lows in each cells
    for i in range(0, len(p_cell)):
        p_day = p_cell[i].find('p', {'class' : 'period-name'}).text
        p_day = p_day.replace('Night',' Night')
        p_days.append(p_day)
        p_cond = p_cell[i].find('p', {'class' : 'short-desc'}).get_text(separator=' ')
        p_conds.append(p_cond)
        if 'night' in p_day or 'Night' in p_day:
            p_low = p_cell[i].find('p',{'class':'temp temp-low'}).text
            #removes any non-digit characters from the temperature
            #below was a previous method, but it was not as robust
            #p_low = p_low.replace(' °F','').replace('Low: ','')
            num_fil = filter(str.isdigit, p_low)
            num_str = ''.join(num_fil)
            p_low = num_str
            p_lows.append(p_low)
        else:
           p_high = p_cell[i].find('p', {'class':'temp temp-high'}).text
           #removes any non-digit characters from the temperature
           #below was a previous method, but it was not as robust
           #p_high = p_high.replace(' °F','').replace('High: ','')
           num_fil = filter(str.isdigit, p_high)
           num_str = ''.join(num_fil)
           p_high = num_str
           p_highs.append(p_high)
           
#replace the first day/night with the respective day-of-week
#consider making module??
if 'Sunday' in p_days[-1]:
    p_days[0] = 'Wednesday'
    p_days[1] = 'Wednesday Night'
elif 'Monday' in p_days[-1]:
    p_days[0] = 'Thursday'
    p_days[1] = 'Thursday Night'
elif 'Tuesday' in p_days[-1]:
    p_days[0] = 'Friday'
    p_days[1] = 'Friday Night'
elif 'Wednesday' in p_days[-1]:
    p_days[0] = 'Saturday'
    p_days[1] = 'Saturday Night'
elif 'Thursday' in p_days[-1]:
    p_days[0] = 'Sunday'
    p_days[1] = 'Sunday Night'
elif 'Friday' in p_days[-1]:
    p_days[0] = 'Monday'
    p_days[1] = 'Monday Night'
elif 'Saturday' in p_days[-1]:
    p_days[0] = 'Tuesday'
    p_days[1] = 'Tuesday Night'
    
#begin outputting the data for the user's city
#counters for highs/lows and conditions
l = 0
h = 0
c = 0
#output the city name followed by dashes under it
outF.write(city+" Forecast Summary\n"+'-'*(len(city)+17)+'\n')

for d in days:
    #output the day
    outF.write(d+'\n')
    #output the description
    outF.write('\t'+p_conds[c]+'\n')
    c+=1
    #output the low
    if 'Night' in d:
        outF.write('\tLow: '+lows[l]+'\n\n')
        l+=1
    #output the high
    else:
        outF.write('\tHigh: '+highs[h]+'\n\n')
        h+=1
outF.write('\n\n')

#begin outputting the data for the predefined city
#counters for highs/lows and conditions
l = 0
h = 0
c = 0
#output the city name followed by dashes under it
outF.write(p_city+" Forecast Summary\n"+'-'*(len(p_city)+17)+'\n')

for d in p_days:
    #output the day
    outF.write(d+'\n')
    #output the description
    outF.write('\t'+p_conds[c]+'\n')
    c+=1
    #output the low
    if 'Night' in d:
        outF.write('\tLow: '+p_lows[l]+'\n\n')
        l+=1
    #output the high
    else:
        outF.write('\tHigh: '+p_highs[h]+'\n\n')
        h+=1


#create a chart of highs/lows
#output the days, centered
#output High
#output the high for that day, centered
#output Low
#output the low for that day, centered
outH.close()
outF.close()