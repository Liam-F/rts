# -*- coding: utf-8 -*-
"""
Created on Sat May  2 15:32:11 2015

@author: jmalinchak
"""




import pandas as pd
import numpy as np

param_numberofyears = 3
numberofweekstorun = param_numberofyears * 52

from datetime import datetime, timedelta
dStart = datetime.now().date() + timedelta(weeks = -numberofweekstorun)
#print(dStart)

index = pd.date_range(dStart+timedelta(days = 0), periods=numberofweekstorun, freq='W-Fri')
#print(index)
columns = ['Minus32','Minus17','Ref','Delta32to17']
df_ = pd.DataFrame(index=index, columns=columns)
df_ = df_.fillna(0) # with 0s rather than NaNs
data = np.array([np.arange(len(index))]*4).T
df = pd.DataFrame(data, index=index, columns=columns)
#-------------------------------------------------------------------------------

dEnd = index[-1]


import pullprices
fmt = '%Y-%m-%d'

dDataStart = dStart+timedelta(days = -33)

f=pullprices.stockhistory("AAPL", dDataStart, dEnd)

for idx, row in df.iterrows():
    #print(idx)
    dRef = idx
    d17 = dRef + timedelta(days = -17)
    d32 = dRef + timedelta(days = -32)

    dRef_string = dRef.strftime(fmt)
    d17_string = d17.strftime(fmt)
    d32_string = d32.strftime(fmt)
    
    #print(dRef_string,d17_string,d32_string)

    try:
        p32 = f.ix[d32_string]['Adj Close']
        #print(d32_string,p32)
        
    except: 
        p32 = float('NaN')
        #print('no data')
        pass
    try:
        p17 = f.ix[d17_string]['Adj Close']
        #print(d17_string,p17)
    except: 
        p17 = float('NaN')
        #print('no data')
        pass
    try:
        pRef = f.ix[dRef_string]['Adj Close']
        #print(dRef_string,pRef)
    except:
        pRef = float('NaN')
        #print('no data')
        pass
    try:
        pdelta32to17 = p17 - p32
        #print('pricedelta',pdelta32to17)
    except:
        pdelta32to17 = float('NaN')
        #print('no delta')
        
    df.loc[dRef] = pd.Series({'Minus32':p32, 'Minus17':p17, 'Ref':pRef, 'Delta32to17':pdelta32to17})
    #print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    
    
print(df)    
print(len(data))
print(len(df))

print('------------------------')
print(dStart)
print(dEnd)
print('dRef',dRef)


#

#
#
#
#
#lsRefDates=[]
#while True:
#    dRef = dCurrent + timedelta(days = RefMinus7)
#        
#    lsRefDates.append(dRef)
#
#    d17 = dRef + timedelta(days = -17)
#    d32 = dRef + timedelta(days = -32)
#    
#    dRef_string = dRef.strftime(fmt)
#    d17_string = d17.strftime(fmt)
#    d32_string = d32.strftime(fmt)
#    dStart_string = dStart.strftime(fmt)
#    print('dRef',dRef)
#    
#    try:
#        p32 = f.ix[d32_string]['Adj Close']
#        print(d32_string,p32)
#        
#    except: 
#        print('no data')
#        pass
#    try:
#        p17 = f.ix[d17_string]['Adj Close']
#        print(d17_string,p17)
#    except: 
#        print('no data')
#        pass
#    try:
#        pRef = f.ix[dRef_string]['Adj Close']
#        print(dRef_string,pRef)
#    except: 
#        print('no data')
#        pass
#    try:
#        pdelta32to17 = p17 - p32
#        print('pricedelta',pdelta32to17)
#    except:
#        print('no delta')
#    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
#    RefMinus7 = RefMinus7 - 7
#    if RefMinus7 < -800:
#        break
#
#print('dRef',dRef)
#print(df)    
#print(len(data))
#print(len(df))
##
##
###day = '12/Oct/2013'
###dRef = datetime.strptime(day, '%d/%b/%Y')
##import pullprices
##from dateutil.relativedelta import relativedelta, FR
##dCurrent = datetime.now() + relativedelta(weekday=FR(-1))
##dCurrent = dCurrent.replace(hour=0,minute=0,second=0,microsecond=0)
##print('dCurrent',dCurrent)
##fmt = '%Y-%m-%d'
##
##
##
## #dRef = datetime.now()
###start = dRef - timedelta(days = dRef.weekday())
##dStart = dCurrent + timedelta(days = -900)