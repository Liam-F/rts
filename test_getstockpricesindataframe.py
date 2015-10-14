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
mycumprobthreshold = 80
mycumprob_to_sell_price_lowrange = 0
mycumprob_to_sell_price_highrange = 95
numberofweekstolookback = 300
RollingNumberOfPeriods = 120
showresults = 0



ThreshholdAbove = 0.0001 #Percent change above
ThreshholdBelow = -0.0001  #Percent change below
myoutputfolder = 'C:\\Batches\\MyPython\\active\\output'
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


import time
millis = int(round(time.time() * 1000))
datestringforfilename = today_datetime.strftime('%Y-%m-%d %H.%M.%S ') + str(millis)
datestringforprinting = today_datetime.strftime('%Y-%m-%d %H:%M') 

daysbackfar = delta.days

#import builddataframeofrefdateminusd2tod1stockpricechanges
#df_0 = builddataframeofrefdateminusd2tod1stockpricechanges.perform(symbol,numberofweekstolookback,daysbackmid,daysbackfar,showresults).DataFrameResult

#number_of_observations = len(df_0.index)
#print('  Number Of Observations Found',number_of_observations)

# ---------------------------------------------------------------------------------
comparesym = mycomparesym
# ##########
# Date setup
#import datetime
#today_date = datetime.date.today()

#today_datetime = datetime.datetime.today()
#print('today_date',today_date)

datedelta = datetime.timedelta(weeks=numberofweekstolookback+3)
startdatecalculated_datetime = today_datetime - datedelta
startdatecalculated_string = str(startdatecalculated_datetime.date())
print('  Start Date:',startdatecalculated_string)

#import time
#millis = int(round(time.time() * 1000))
#datestringforfilename = today_datetime.strftime('%Y-%m-%d %H.%M.%S ') + str(millis)

import pullprices
df_compare = pullprices.stockhistorybackfilledtodatframeofstockhistoryinstances(comparesym, startdatecalculated_string, str(today_date))
print df_compare
print('  My Compare Price:',df_compare['Adj Close'][len(df_compare)-1])