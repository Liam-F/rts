# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 13:47:46 2014

@author: justin.malinchak
"""

import class_optionprice
a = class_optionprice.PriceAttributes()
a.optionsymbol = "XXX982220000C00"
a.strike = '90'
a.last = '1.9'
a.impliedvolatility = '12%'
a.bid = '4.2'

d = {}
d[1] = a
a = class_optionprice.PriceAttributes()
a.optionsymbol = "YYY82220000C00"
a.strike = "91"
a.last = "2.1"
d[2] = a

a = d[1]
print('strike 1 = ' + a.strike)
print('impliedvolatility 1 = ' + a.impliedvolatility)
print('bid 1 = ' + a.bid)

a = d[2]
print('last 2 = ' + a.last)

#symbols=class_optionprice.Symbols('AAPL','FB')    # Instance 1
#print(symbols.symbolList)
#expirations=class_optionprice.Expirations('2014-11-22','2014-11-28')    # Instance 1
#print(expirations.expirationList)
