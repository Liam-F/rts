# -*- coding: utf-8 -*-
"""
Created on Sat May  9 16:43:23 2015

@author: jmalinchak
"""


# ##########
# Parameters
symbol = 'AAPL'
expirationdate_string = '2015-07-24'
numberofweekstolookback = 300
RollingNumberOfPeriods = 120
daysbackmid = 1
showresults = 0
ThreshholdAbove = 0.001 #Percent change above
ThreshholdBelow = -0.001  #Percent change below


import datetime
today_date = datetime.date.today()
print('today_date',today_date)
expire_date = datetime.datetime.strptime(expirationdate_string,'%Y-%m-%d').date()
print('expire_date',expire_date )
delta = expire_date - today_date
print(delta.days)

daysbackfar = delta.days

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
    fartomidpricechangedelta = (row['priceDaysBackMid'] - row['priceDaysBackFar']) / row['priceDaysBackFar']
    if abs(fartomidpricechangedelta) > 0.1:
        print('Far to Mid price delta',fartomidpricechangedelta,row['dateDaysBackMid'],row['dateDaysBackFar'])

    #print('xxxxxxxxxxxxxxxxxxx',row)
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

maxpercent_drawup = 0

for n in np.linspace(0,1,1000,endpoint=False):
    cumprob = ss.percentileofscore(serDrawUp, n)    
    if cumprob >= 80:
        maxpercent_drawup = n
        print(round(cumprob,1),'percent of observations closed up inside of','{percent:.2%}'.format(percent=n)),'percent'        
        break
    
print('')
print(symbol,'Draw Down:',len(df_0.index), 'observations')
print('   ','DaysBackFar',daysbackfar,'   DaysBackMid:',daysbackmid)
serDrawDown = pd.Series(df_0['DrawDownPctChange'])
serDrawDown.hist(cumulative=True, normed=1, bins=ibeyondbelow)
plt.show()

maxpercent_drawdown = 0
for n in np.linspace(0,1,1000,endpoint=False):
    cumprob = ss.percentileofscore(serDrawDown, n)    
    if cumprob >= 80:
        maxpercent_drawdown = n
        print(round(cumprob,1),'percent of observations closed down inside of','{percent:.2%}'.format(percent=(-1.0)*n)),'percent'

        break

import pullprices as pp
df = pp.options_to_dataframe(symbol,expirationdate_string,0)

if showresults == 1:
    print(df)

stockprice = pp.stock(symbol)
print(stockprice)

import mytools
symbol1 = mytools.get_from_optionsymbol()
rows    = []        
#rows.append(['optionsymbol','stockprice','strike','pdeltapct','cumprob','bid','ask','last'])
rows.append(['exdate','symbol','ty','st','strike','pdeltapct','cumprob','bid','ask','iv','iscandidate'])
d_candidates = {}
for index, row in df.iterrows():
    optionsymbol = row['optionsymbol']
    #print(optionsymbol)
    strike = row['strike']
    exdate = symbol1.expirationdate(row['optionsymbol'])
    symbol = symbol1.symbol(row['optionsymbol'])
    optiontype = mytools.get_from_optionsymbol().optiontype(row['optionsymbol'])
    pdeltapct = (float(strike) - float(stockprice)) / float(stockprice)
    cumprob = float('NaN')
    iscandidate = 0
    # ========================
#    if abs(pdeltapct) > 0.10:
#        print('++++++++++++++++++++++++more than 10',row)
    # ========================
    if optiontype == 'C':
        if pdeltapct > 0:
            cumprob = ss.percentileofscore(serDrawUp, pdeltapct)

    elif optiontype == 'P':
        if pdeltapct < 0:
            cumprob = ss.percentileofscore(serDrawUp,(-1.0) * pdeltapct)
    if cumprob != float('NaN'):
        if cumprob > 50 and cumprob < 90:
            iscandidate = 1
            # ##########
            # candidates are found and put into a dictionary, you might want some other data storage
            #d_candidates[str(strike)+optiontype] = row,rows[len(rows)-1]
        rows.append([exdate,symbol,optiontype,stockprice,strike,'{percent:.2%}'.format(percent=pdeltapct),'{percent:.2%}'.format(percent=cumprob/100),row['bid'],row['ask'],row['impliedvolatility'],iscandidate])
        #d_candidates[strike,optiontype] = [symbol,optiontype,stockprice,strike,'{percent:.2%}'.format(percent=pdeltapct),round(cumprob,1),row['bid'],row['ask'],row['impliedvolatility'],iscandidate]
        
    #print(symbol,'price change from ',stockprice,'to strike',strike,'(','{percent:.2%}'.format(percent=pdeltapct),') exp',exdate,cumprob)
headers = rows.pop(0)
df_01 = pd.DataFrame(rows,columns=headers)
print(df_01)
print('daysbackfar:',daysbackfar,'  daysbackmid:',daysbackmid)

# ####################################################
# Here is where we find the value of the credit spread
#      still need to build the Put credit spread

for index,row in df_01.iterrows():
    if float(row['iscandidate']) == 1:
        sellstockprice = row['st']
        sellstrike = row['strike']
        sellcumprob = row['cumprob']
        pdeltapct = row['pdeltapct']  
        sellbidprice = row['bid']  
        buyaskprice = float('NaN')
        buystrike = float('NaN')
        row_inner_found = []
        if row['ty'] == 'C':         
            for index_inner,row_inner in df_01.iterrows():
                if row_inner['ty'] == row['ty']:
                    if float(row_inner['strike']) == float(row['strike'])+1:
                        row_inner_found = row_inner
                        buyaskprice = row_inner['ask']
                        buystrike = row_inner['strike']
                        print('CALL >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                        
        if row['ty'] == 'P':
            for index_inner,row_inner in df_01.iterrows():
                if row_inner['ty'] == row['ty']:
                    if float(row_inner['strike']) == float(row['strike'])-1:
                        row_inner_found = row_inner
                        buyaskprice = row_inner['ask']
                        buystrike = row_inner['strike']
                        print('PUT >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        print(sellstockprice,pdeltapct,sellstrike,buystrike,sellcumprob,sellbidprice,buyaskprice)
        print(row)
        print('row_inner_found ------------------------------------------------')
        print(row_inner_found)
        
print('End: Candidate where cumprob is between my specified range')

#for k,v in d_candidates.items():
#    print(k)
#    print(v)
'''
        rows    = []        
        rows.append(['strike','optionsymbol','last','bid','ask','change','pctchange','volume','openinterest','impliedvolatility'])
        for tr in table:
            d = [td.text_content().strip().replace(',','') for td in tr.xpath('./td')]
            rows.append(d)
        
        stockprice=stock(symbol)
        headers = rows.pop(0)
        import pandas as pd
        df = pd.DataFrame(rows, columns=headers)
        #import numpy as np
        df['stockprice'] = stockprice
'''