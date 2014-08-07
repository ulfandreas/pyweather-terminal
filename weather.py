#!/usr/bin/python

"""

v0.31

Written by: https://github.com/ulfandreas

Usage: weather.py "location"

TODO:
    Get it to work with argvs
"""

import requests
import bs4
from sys import argv

script, location = argv

url = 'http://thefuckingweather.com/?where=%s' % (location)
r   = requests.get(url)

sauce = bs4.BeautifulSoup(r.text)                               # hi ho, hi ho
temp  = sauce.select('.temperature')                            # off to scrape
wtfw  = sauce.select('.remark')                                 # we go!

print 'It\'s %s F in %s right now... %s' % (temp[0].text, location, wtfw[0].text)

