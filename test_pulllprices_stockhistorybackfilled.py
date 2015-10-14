# -*- coding: utf-8 -*-
"""
Created on Sat May 16 12:08:32 2015

@author: jmalinchak
"""
import pullprices as pp
#df = pp.stockhistory('AAPL','2014-01-01','2015-05-15')
#mydict1 = pp.stockhistorybackfilledtodictionary('AAPL','2015-01-01','2015-05-15')
#print('mypick',mydict1['2015-05-09']('AdjClose'))

mydict2 = pp.stockhistorybackfilledtodictionaryofstockhistoryinstances('AAPL','2015-01-01','2015-05-15')

from collections import OrderedDict
#dOrdered = OrderedDict(sorted(mydict2.items(), key=lambda t: t[1]['sortbymeasurevalue']))
dOrdered = OrderedDict(sorted(mydict2.items()))
#print(mydict2)

for k,d in dOrdered.items():
    print(k,d.volume,d.adjclose)
    # make sure you try and put other stock price data into the dictionary

print('my selectioon',dOrdered['2015-05-11'].adjclose)