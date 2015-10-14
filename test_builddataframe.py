# -*- coding: utf-8 -*-
"""
Created on Sat May 23 09:44:06 2015

@author: jmalinchak
"""

import pullprices
mydataframe = pullprices.stockhistorybackfilledtodatframeofstockhistoryinstances('AAPL','2013-12-01','2015-05-22')
print(mydataframe)
