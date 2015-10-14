# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 09:53:32 2015

@author: jmalinchak
"""

import pullprices as pp
df = pp.options_to_dataframe('^VIX','2015-07-24')
#df = pp.options_to_dataframe('SPY','2015-07-24')
print('len(df)',len(df))