#!/usr/bin/python3
'''# getting countries by scraping
'''

from urllib.request import urlopen, Request
COUNTRIES_URL = "http://example.webscraping.com/"

request = Request(COUNTRIES_URL)
page = urlopen(request).read()
content = page.decode('utf-8')

COUNTRY_TAG = '<a href="/places/default/view/'
SEARCH_INDEX = content.find(COUNTRY_TAG)

for i in range (0, 10):
    country_start = content.find(COUNTRY_TAG,SEARCH_INDEX) + len(COUNTRY_TAG)
    country_name = ''
    for char in content[country_start:]:
        if char != '"':
            country_name += char
        else:
            break
    country_name = country_name[:-2]
    print(country_name)
    SEARCH_INDEX = content.find(country_name)
