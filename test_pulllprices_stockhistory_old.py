# -*- coding: utf-8 -*-
"""
Created on Sat May  2 08:04:20 2015

@author: jmalinchak
"""
from datetime import datetime, timedelta


#day = '12/Oct/2013'
#dRef = datetime.strptime(day, '%d/%b/%Y')
import pullprices
from dateutil.relativedelta import relativedelta, FR
dCurrent = datetime.now() + relativedelta(weekday=FR(-1))
dCurrent = dCurrent.replace(hour=0,minute=0,second=0,microsecond=0)
print('dCurrent',dCurrent)
fmt = '%Y-%m-%d'



 #dRef = datetime.now()
#start = dRef - timedelta(days = dRef.weekday())
dDataStart = dCurrent + timedelta(days = -900)
RefMinus7 = 0

f=pullprices.stockhistory("AAPL", dDataStart, dCurrent)
lsRefDates=[]
while True:
    dRef = dCurrent + timedelta(days = RefMinus7)
        
    lsRefDates.append(dRef)

    d17 = dRef + timedelta(days = -17)
    d32 = dRef + timedelta(days = -32)
    
    dRef_string = dRef.strftime(fmt)
    d17_string = d17.strftime(fmt)
    d32_string = d32.strftime(fmt)
    dDataStart_string = dDataStart.strftime(fmt)
    print('dRef',dRef)
    
    try:
        p32 = f.ix[d32_string]['Adj Close']
        print(d32_string,p32)
        
    except: 
        print('no data')
        pass
    try:
        p17 = f.ix[d17_string]['Adj Close']
        print(d17_string,p17)
    except: 
        print('no data')
        pass
    try:
        pRef = f.ix[dRef_string]['Adj Close']
        print(dRef_string,pRef)
    except: 
        print('no data')
        pass
    try:
        pdelta32to17 = p17 - p32
        print('pricedelta',pdelta32to17)
    except:
        print('no delta')
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    RefMinus7 = RefMinus7 - 7
    if RefMinus7 < -800:
        break

print('dRef',dRef)
#-------------------------------------------------------------------------------
import pandas as pd
import numpy as np

#todays_date = datetime.now().date()
#index = pd.date_range(dRef+timedelta(days = 0), periods=10, freq='W-Fri')
index = lsRefDates
columns = ['Minus32','Minus17','Ref']
df_ = pd.DataFrame(index=index, columns=columns)
df_ = df_.fillna(0) # with 0s rather than NaNs
data = np.array([np.arange(len(lsRefDates))]*3).T
df = pd.DataFrame(data, index=index, columns=columns)
#-------------------------------------------------------------------------------

print(df)    
print(len(lsRefDates))
print(len(df))

    
