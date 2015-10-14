# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 06:09:44 2015

@author: jmalinchak
"""
symbol = 'FB'
numberofweekstolookback = 200
daysbackmid = 0
daysbackfar = 16
showresults = 0

import builddataframeofrefdateminusd2tod1stockpricechanges
pricingsymbol = symbol
if pricingsymbol in ['VIX','RUT']:
    pricingsymbol = '^'+symbol
df_stockpricechanges = builddataframeofrefdateminusd2tod1stockpricechanges.perform(pricingsymbol,numberofweekstolookback,daysbackmid,daysbackfar,showresults).DataFrameResult
print(len(df_stockpricechanges))
df_stockpricechanges_nonan = df_stockpricechanges.dropna(subset=['priceDaysBackFar'])
print(len(df_stockpricechanges_nonan.index))
#print(df_stockpricechanges_nonan)