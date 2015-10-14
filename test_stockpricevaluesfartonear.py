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
mycumprobthreshold = 80 #Percent in whole number 80 = 80%
mycumprob_to_sell_price_lowrange = 0
mycumprob_to_sell_price_highrange = 95
numberofweekstolookback = 100
RollingNumberOfPeriods = 120
showresults = 0



ThreshholdAbove = 0.0001 #Percent change above
ThreshholdBelow = -0.0001  #Percent change below
myoutputfolder = 'C:\\$Work\\Batches\\MyPython\\active\\output'
#myoutputfolder = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\New Folder\\output'



# ##########
# Date setup
import datetime
today_date = datetime.date.today()
today_datetime = datetime.datetime.today()

expire_date = datetime.datetime.strptime(expirationdate_string,'%Y-%m-%d').date()

delta = expire_date - today_date


# ########
# Initialize notes
print('Initialized:','calculatecumulativeprobabilityofpricechangebasedonexpiration.py')
print('-----------')
print('Symbol:',symbol)
print('  Compared to:',mycomparesym)
print('  Today:',today_date)
print('  Expire Date:',expire_date )
print('  Number of Days to Expiration:',delta.days)

# ##########
# Date setup
import time
millis = int(round(time.time() * 1000))
datestringforfilename = today_datetime.strftime('%Y-%m-%d %H.%M.%S ') + str(millis)
datestringforprinting = today_datetime.strftime('%Y-%m-%d %H:%M') 

daysbackfar = delta.days

import builddataframeofrefdateminusd2tod1stockpricechanges
df_stockpricechanges = builddataframeofrefdateminusd2tod1stockpricechanges.perform(symbol,numberofweekstolookback,daysbackmid,daysbackfar,showresults).DataFrameResult

number_of_observations = len(df_stockpricechanges.index)
print('  Number Of Observations Found',number_of_observations)
print('runtime_delta',datetime.datetime.today() - today_datetime)
# ---------------------------------------------------------------------------------
comparesym = mycomparesym

#import datetime
#today_date = datetime.date.today()

#today_datetime = datetime.datetime.today()
#print('today_date',today_date)

datedelta = datetime.timedelta(weeks=numberofweekstolookback+3)
startdatecalculated_datetime = today_datetime - datedelta
startdatecalculated_string = str(startdatecalculated_datetime.date())
print('  Start Date:',startdatecalculated_string)


# ###########################
# Get VIX or comparable stock
import pullprices
df_compare = pullprices.stockhistorybackfilledtodatframeofstockhistoryinstances(comparesym, startdatecalculated_string, str(today_date))

print('runtime_delta',datetime.datetime.today() - today_datetime)

#print(f.loc[f.index == '2015-06-18'])
#f1 = f.loc[f.index.isin(['2015-06-18'])][['Adj Close']]


# ################################################################################################################
# performs some general statistics
import pandas as pd
df_std = pd.rolling_std(df_stockpricechanges[['DrawDownPctChange', 'DrawUpPctChange']], RollingNumberOfPeriods)
df_mean = pd.rolling_mean(df_stockpricechanges[['DrawDownPctChange', 'DrawUpPctChange']], RollingNumberOfPeriods)

# #########################################################################
# Adds a column to dataframe to Compare data to something (VIX for example)
df_stockpricechanges['comppratfar'] = float('NaN')
df_stockpricechanges['breachedaboveorbelow'] = int(0)

print(df_stockpricechanges)