#!/usr/bin/python
'''Print Title of page
'''

import re
import html
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

user_url = str(input('Input adress of page in format "https://":\n'
                     'For example : https://www.youtube.com/:\n'))

'''getting page from server
'''
headers = {'User-Agent': 'Mozila/5.0 (X11; Fedora; Linux x86_64;)'}
user_request = Request(user_url, headers=headers)
user_page = urlopen(user_request).read()
user_page = user_page.decode('utf-8')


'''getting title of page
'''
search_page = BeautifulSoup(user_page, 'html.parser')
search_section = str(search_page.find('title'))
title = re.sub('</?title>', '', search_section)
print('-'*50)
print('title is : "{}"' .format(title))
