# -*- coding: utf-8 -*-
"""
Created on Thu Dec 04 15:37:23 2014

@author: justin.malinchak
"""

import urllib2
from bs4 import BeautifulSoup

fish_url = 'http://www.fishbase.us/ComNames/CommonNameSearchList.php?CommonName=Salmon'
page = urllib2.urlopen(fish_url)
html_doc = page.read()
#print(html_doc)
soup = BeautifulSoup(html_doc)

scientific_names = [it.text for it in soup.table.find_all('div')]

for item in scientific_names:
    print(item)