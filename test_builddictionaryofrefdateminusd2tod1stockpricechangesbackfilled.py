# -*- coding: utf-8 -*-
"""
Created on Sat May  9 16:43:23 2015

@author: jmalinchak
"""

import builddictionaryofrefdateminusd2tod1stockpricechangesbackfilled
o = builddictionaryofrefdateminusd2tod1stockpricechangesbackfilled.perform('AAPL',4,1)
mydict = o.DictionaryResult

for k,v in mydict.items():
    print(k,v.dateref,v.priceref,v.datemaxback,v.pricemaxback)