# -*- coding: utf-8 -*-
"""
Created on Sat May  9 16:43:23 2015

@author: jmalinchak
"""

# ##########
# Parameters
symbol = 'MSFT'
numberofweekstolookback = 300
RollingNumberOfPeriods = 120
daysbackmid = 1
daysbackfar = 14
showresults = 0
ThreshholdAbove = 0.001 #Percent change above
ThreshholdBelow = -0.001  #Percent change below

import builddataframeofrefdateminusd2tod1stockpricechanges
df_0 = builddataframeofrefdateminusd2tod1stockpricechanges.perform(symbol,numberofweekstolookback,daysbackmid,daysbackfar,showresults).DataFrameResult

# ==========
print(df_0)
# ==========

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

for index, row in df_0.iterrows():
    if row['DrawUpPctChange'] > ThreshholdAbove:
        ibeyondabove = ibeyondabove + 1
    if row['DrawDownPctChange'] > abs(ThreshholdBelow):
        ibeyondbelow = ibeyondbelow + 1

print('Last DrawUpPctChange Mean',df_mean.ix[len(df_mean.index)-1,'DrawUpPctChange'])
print('Last DrawUpPctChange Std',df_std.ix[len(df_std.index)-1,'DrawUpPctChange'])

print('---------------------------------')
print('Percent Beyond Draw Up')
print('---------------------------------')
print('  ',symbol
        ,'{percent:.2%}'.format(percent=ibeyondabove/len(df_0.index))
        ,'of the'
        ,len(df_0.index)
        ,'observations closed above the '
        ,'{percent:.2%}'.format(percent=ThreshholdAbove)
        ,'threshold between t-',daysbackfar,'and t-',daysbackmid,', a total of'
        ,ibeyondabove
        ,'observations'
    )
    
print('---------------------------------')
print('Percent Beyond Draw Down')
print('---------------------------------')
print('  ',symbol
        ,'{percent:.2%}'.format(percent=ibeyondbelow/len(df_0.index))
        ,'of the'
        ,len(df_0.index)
        ,'observations closed below the'
        ,'{percent:.2%}'.format(percent=ThreshholdBelow)
        ,'threshold between t-',daysbackfar,'and t-',daysbackmid,', a total of'
        ,ibeyondbelow
        ,'observations'
    )


#import pandas as pd
#
#import numpy as np
#
print('')
print(symbol,'Draw Up:',len(df_0.index), 'observations')
print('   ','DaysBackFar',daysbackfar,'   DaysBackMid:',daysbackmid)
serDrawUp = pd.Series(df_0['DrawUpPctChange'])
serDrawUp.hist(cumulative=True, normed=1, bins=ibeyondabove)
plt.show()

import numpy as np
import scipy.stats as ss

for n in np.linspace(0,1,1000,endpoint=False):
    cumprob = ss.percentileofscore(serDrawUp, n)    
    if cumprob >= 80:
        print(round(cumprob,1),'percent of observations closed up inside of','{percent:.2%}'.format(percent=n)),'percent'
        break
    
print('')
print(symbol,'Draw Down:',len(df_0.index), 'observations')
print('   ','DaysBackFar',daysbackfar,'   DaysBackMid:',daysbackmid)
serDrawDown = pd.Series(df_0['DrawDownPctChange'])
serDrawDown.hist(cumulative=True, normed=1, bins=ibeyondbelow)
plt.show()
for n in np.linspace(0,1,1000,endpoint=False):
    cumprob = ss.percentileofscore(serDrawDown, n)    
    if cumprob >= 80:
        print(round(cumprob,1),'percent of observations closed down inside of','{percent:.2%}'.format(percent=(-1)*n)),'percent'
        break

import pullprices as pp
df = pp.options_to_dataframe(symbol,'2015-06-19',0)
print(df)