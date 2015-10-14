# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 21:35:06 2014

@author: jmalinchak
"""

import urllib3

http = urllib3.PoolManager()

r = http.request('GET', 'http://www.msn.com/')

print(r.status, r.data)