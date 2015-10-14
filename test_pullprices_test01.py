# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 07:40:39 2015

@author: jmalinchak
"""

import pullprices_test01 as pp
df = pp.options_to_dataframe('^OEX','2015-07-24')
print(df)
# ##########
# Date setup
import datetime
today_datetime = datetime.datetime.today()
today_date = datetime.date.today()
iter_date = today_date

for expirationcounter in range(10):
    #while iter_date.weekday() != 4:
    iter_date += datetime.timedelta(1)   
    print(iter_date,iter_date.weekday())