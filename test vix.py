# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 22:24:11 2015

@author: jmalinchak
"""
comparesym = '^VIX'
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
f = pullprices.stockhistorybackfilledtodatframeofstockhistoryinstances('^VIX', longago_string, str(today_date))
print(f)
print(f.loc[f.index == '2015-06-18'])
print(f.loc[f.index.isin(['2015-06-18'])])
f1 = f.loc[f.index.isin(['2015-06-18'])][['Adj Close']]
print('---------------')
yourvalue = f.ix['2015-06-18', 'Adj Close']
print(yourvalue)
myoutputfolder = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\New Folder\\output'
f.to_csv(myoutputfolder + "\\ironcondor prices " + comparesym +  " " + datestringforfilename + ".csv",columns=('Open','High','Low','Close','Volume','Adj Close','Back Filled'))
