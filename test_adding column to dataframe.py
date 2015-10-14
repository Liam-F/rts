# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 00:21:07 2015

@author: jmalinchak
"""

# -*- coding: utf-8 -*-
"""
Created on Sat May  9 16:43:23 2015

@author: jmalinchak
"""


# ##########
# Parameters
symbol = 'SPY'
mycomparesym = '^VIX'
expirationdate_string = '2015-07-10'
daysbackmid = 0
myspreadindollars = 1
mycumprob_to_sell_price_lowrange = 0
mycumprob_to_sell_price_highrange = 95
numberofweekstolookback = 300
RollingNumberOfPeriods = 120
showresults = 1
ThreshholdAbove = 0.001 #Percent change above
ThreshholdBelow = -0.001  #Percent change below
#myoutputfolder = 'C:\\Batches\\MyPython\\active\\output'
myoutputfolder = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\New Folder\\output'

# ##########
# Date setup
import datetime
today_date = datetime.date.today()
today_datetime = datetime.datetime.today()
print('today_date',today_date)
expire_date = datetime.datetime.strptime(expirationdate_string,'%Y-%m-%d').date()
print('expire_date',expire_date )
delta = expire_date - today_date
print(delta.days)

import time
millis = int(round(time.time() * 1000))
datestringforfilename = today_datetime.strftime('%Y-%m-%d %H.%M.%S ') + str(millis)

daysbackfar = delta.days

import builddataframeofrefdateminusd2tod1stockpricechanges
df_0 = builddataframeofrefdateminusd2tod1stockpricechanges.perform(symbol,numberofweekstolookback,daysbackmid,daysbackfar,0).DataFrameResult

# ---------------------------------------------------------------------------------
comparesym = mycomparesym
# ##########
# Date setup
import datetime
today_date = datetime.date.today()

today_datetime = datetime.datetime.today()
print('today_date',today_date)

datedelta = datetime.timedelta(weeks=301)
longago_datetime = today_datetime - datedelta
longago_string = str(longago_datetime.date())
print('longago_string',longago_string)

import time
millis = int(round(time.time() * 1000))
datestringforfilename = today_datetime.strftime('%Y-%m-%d %H.%M.%S ') + str(millis)

import pullprices
df_compare = pullprices.stockhistorybackfilledtodatframeofstockhistoryinstances(comparesym, longago_string, str(today_date))

#print(f.loc[f.index == '2015-06-18'])

#f1 = f.loc[f.index.isin(['2015-06-18'])][['Adj Close']]


## ################################################################################################################
import pandas as pd
df_std = pd.rolling_std(df_0[['DrawDownPctChange', 'DrawUpPctChange']], RollingNumberOfPeriods)
df_mean = pd.rolling_mean(df_0[['DrawDownPctChange', 'DrawUpPctChange']], RollingNumberOfPeriods)


#print('rolling std xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
#print(df_std)
#print('rolling mean xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

#print(df_mean)
#print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
#print('testing test_builddataframeofrefdateminusd2tod1stockpricechanges.py')
#print('df_0 Column Names',df_0)
print('df_0 Column Names',df_0.columns)
print('Number Of Observations',len(df_0.index))
#df_prices = df_0['pRef']
#print(df_prices)
#print(df_std.mean(0))

ibeyondabove = 0
ibeyondbelow = 0


df_0['compareiv'] = float('NaN')



# #######################################################################################
# Counts number of observations that hit above and below threshold during trading period
for index, row in df_0.iterrows():
    fartomidpricechangedelta = (row['priceDaysBackMid'] - row['priceDaysBackFar']) / row['priceDaysBackFar']
    if abs(fartomidpricechangedelta) > 0.1:
        print('Far to Mid price delta',fartomidpricechangedelta,row['dateDaysBackMid'],row['dateDaysBackFar'])

    #print('xxxxxxxxxxxxxxxxxxx',row)
    if row['DrawUpPctChange'] > ThreshholdAbove:
        ibeyondabove = ibeyondabove + 1
    if row['DrawDownPctChange'] > abs(ThreshholdBelow):
        ibeyondbelow = ibeyondbelow + 1
    #row['compareiv'] = df_compare.ix[str(index.date()), 'Adj Close']

    #df_0['compareiv'][str(index.date())] = df_compare.ix[str(index.date()), 'Adj Close']
    df_0['compareiv'][str(index.date())] = df_compare['Adj Close'][row['dateDaysBackFar']]
    #print('mystuff',str(index.date()))
    #print('compareiv',df_compare.ix[str(index.date()), 'Adj Close'])

print(df_0)