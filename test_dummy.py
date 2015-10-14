# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 10:34:28 2015

@author: jmalinchak
"""

import pandas as pd

print('pandas verion',pd.__version__)

import scipy.stats as ss
print(ss.percentileofscore([1, 2, 3, 4], 3))

import numpy as np
print(np.arange(0,1,0.1))
print(np.linspace(0,1,11))

for n in np.linspace(0,.3,1000,endpoint=False):
    print(n)

import pullprices as pp
df = pp.options_to_dataframe('MSFT','2015-06-19',0)
print(df)

import datetime
today_date = datetime.datetime.now()
print 'from time: ',today_date.strftime('%Y-%m-%d')
print 'from time: ',today_date.strftime('%Y%m%d%H%M%S')
print(today_date)
expire_date = datetime.datetime.strptime('2015-06-19','%Y-%m-%d').date()
print(expire_date )
delta = expire_date - today_date.date()
print(delta.days)

import time
millis = int(round(time.time() * 1000))
print millis
print 'millis',millis