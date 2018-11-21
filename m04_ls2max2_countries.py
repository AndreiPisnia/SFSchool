#!/usr/bin/python3
'''# getting countries by scraping
'''
import time
from urllib.request import urlopen, Request

for i in range(0,26):

    COUNTRIES_URL = "http://example.webscraping.com/places/default/index/" + str(i)

    request = Request(COUNTRIES_URL)
    page = urlopen(request).read()
    content = page.decode('utf-8')

    COUNTRY_TAG = '<a href="/places/default/view/'
    SEARCH_INDEX = content.find(COUNTRY_TAG)

    for j in range (0, 10):
        country_start = content.find(COUNTRY_TAG,SEARCH_INDEX) + len(COUNTRY_TAG)
#        print(country_start)
        country_name = ''
        for char in content[country_start:]:
            if char != '"':
                country_name += char
            else:
                break
            
        if i == 0:
            country_name = country_name[:-2]
        elif i >= 1 and i <=9:
            country_name = country_name[:-3]
        else:
            country_name = country_name[:-4]
        print(country_name)
        if country_name == "Zimbabwe":
            break
        SEARCH_INDEX = content.find(country_name)
        
    time.sleep(1)
