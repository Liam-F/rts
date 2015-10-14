# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 18:02:31 2015

@author: justin.malinchak
"""

#import pullprices_optionsonly as pp
#
#pp.options('VIX',
#        '2015-07-17',
#        'c:\\Batches\\$Work')

from pandas.io.data import Options
temp = Options('SPY','yahoo')
z = temp.get_options_data(7,2014)
print z
