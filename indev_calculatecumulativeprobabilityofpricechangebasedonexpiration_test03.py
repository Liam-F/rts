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
df_0 = builddataframeofrefdateminusd2tod1stockpricechanges.perform(symbol,numberofweekstolookback,daysbackmid,daysbackfar,showresults).DataFrameResult

if showresults == 1:
    # ==========
    print(df_0)
    df_0.to_csv(myoutputfolder + "\\ironcondor sourcedata " + symbol +  " " + datestringforfilename + ".csv",columns=('dateDaysBackMid','dateDaysBackFar','priceRefDate','priceDaysBackMid','priceDaysBackFar','DeltaFartoMid','DrawDownMax','DrawUpMax','DrawDownPctChange','DrawUpPctChange'))

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
        
if showresults == 1:
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
    cumprob_to_sell_price = ss.percentileofscore(serDrawUp, n)    
    if cumprob_to_sell_price >= 80:
        maxpercent_drawup = n
        print(round(cumprob_to_sell_price,1),'percent of observations closed up inside of','{percent:.2%}'.format(percent=n)),'percent'        
        break
    
print('')
print(symbol,'Draw Down:',len(df_0.index), 'observations')
print('   ','DaysBackFar',daysbackfar,'   DaysBackMid:',daysbackmid)
serDrawDown = pd.Series(df_0['DrawDownPctChange'])
serDrawDown.hist(cumulative=True, normed=1, bins=ibeyondbelow)
plt.show()

maxpercent_drawdown = 0
for n in np.linspace(0,1,1000,endpoint=False):
    cumprob_to_sell_price = ss.percentileofscore(serDrawDown, n)    
    if cumprob_to_sell_price >= 80:
        maxpercent_drawdown = n
        print(round(cumprob_to_sell_price,1),'percent of observations closed down inside of','{percent:.2%}'.format(percent=(-1.0)*n)),'percent'

        break

import pullprices as pp
df = pp.options_to_dataframe(symbol,expirationdate_string,0)

if showresults == 1:
    # ==========
    print(df)
    # ==========
    
stockprice = pp.stock(symbol)
print(stockprice)

import mytools
osymbol = mytools.get_from_optionsymbol()
rows    = []        
#rows.append(['optionsymbol','stockprice','strike','pdeltapct_to_sell_price','cumprob_to_sell_price','bid','ask','last'])
rows.append(['exdate','symbol','ty','st','strike_at_sell_price','pdeltapct_to_sell_price','cumprob_to_sell_price','cumprob_to_buy_price','bid','ask','iv','iscandidate'])
d_candidates = {}
for index, row in df.iterrows():
    optionsymbol = row['optionsymbol']
    #print(optionsymbol)
    strike_at_sell_price = row['strike']
    optiontype = mytools.get_from_optionsymbol().optiontype(row['optionsymbol'])
    if optiontype == 'C':
        strike_at_buy_price = float(strike_at_sell_price) + float(myspreadindollars)
    else:
        strike_at_buy_price = float(strike_at_sell_price) - float(myspreadindollars)
        
    exdate = osymbol.expirationdate(row['optionsymbol'])
    vsymbol = osymbol.symbol(row['optionsymbol'])

    pdeltapct_to_sell_price = (float(strike_at_sell_price) - float(stockprice)) / float(stockprice)
    pdeltapct_to_buy_price = (float(strike_at_buy_price) - float(stockprice)) / float(stockprice)
    cumprob_to_sell_price = float('NaN')
    cumprob_to_buy_price = float('NaN')
    iscandidate = 0
    # ========================
#    if abs(pdeltapct_to_sell_price) > 0.10:
#        print('++++++++++++++++++++++++more than 10',row)
    # ========================
    if optiontype == 'C':
        if pdeltapct_to_sell_price > 0:
            cumprob_to_sell_price = ss.percentileofscore(serDrawUp, pdeltapct_to_sell_price)
            cumprob_to_buy_price =  ss.percentileofscore(serDrawUp, pdeltapct_to_buy_price)
    elif optiontype == 'P':
        if pdeltapct_to_sell_price < 0:
            cumprob_to_sell_price = ss.percentileofscore(serDrawUp,(-1.0) * pdeltapct_to_sell_price)
            cumprob_to_buy_price = ss.percentileofscore(serDrawUp,(-1.0) * pdeltapct_to_buy_price)
            
    if cumprob_to_sell_price != float('NaN'):
        if cumprob_to_sell_price > mycumprob_to_sell_price_lowrange and cumprob_to_sell_price < mycumprob_to_sell_price_highrange:
            iscandidate = 1
            # ##########
            # candidates are found and put into a dictionary, you might want some other data storage
            #d_candidates[str(strike_at_sell_price)+optiontype] = row,rows[len(rows)-1]
        rows.append([exdate,vsymbol,optiontype,stockprice,strike_at_sell_price,'{percent:.2%}'.format(percent=pdeltapct_to_sell_price),'{percent:.2%}'.format(percent=cumprob_to_sell_price/100),'{percent:.2%}'.format(percent=cumprob_to_buy_price/100),row['bid'],row['ask'],row['impliedvolatility'],iscandidate])
        #d_candidates[strike_at_sell_price,optiontype] = [symbol,optiontype,stockprice,strike_at_sell_price,'{percent:.2%}'.format(percent=pdeltapct_to_sell_price),round(cumprob_to_sell_price,1),row['bid'],row['ask'],row['impliedvolatility'],iscandidate]
        
    #print(symbol,'price change from ',stockprice,'to strike_at_sell_price',strike_at_sell_price,'(','{percent:.2%}'.format(percent=pdeltapct_to_sell_price),') exp',exdate,cumprob_to_sell_price)
headers = rows.pop(0)
df_01 = pd.DataFrame(rows,columns=headers)

                            # ==========
                            #print(df_01)
                            # ==========

print('daysbackfar:',daysbackfar,'  daysbackmid:',daysbackmid)

# ####################################################
# Here is where we find the value of the credit spread
#      still need to build the Put credit spread
candidaterows = []        
candidaterows.append(['ty','stkp','spdel','sstrk','bstrk','scump','bcump','sbid','bask','capt','myexdate','daysbackmid'])

for index,row in df_01.iterrows():
    if float(row['iscandidate']) == 1:
        myexdate = row['exdate']
        myoptiontype = row['ty'] 
        sellstockprice = row['st']
        sellstrike = row['strike_at_sell_price']
        sellcumprob = row['cumprob_to_sell_price']
        buycumprob = row['cumprob_to_buy_price']
        pdeltapct_to_sell_price = row['pdeltapct_to_sell_price']  
        sellbidprice = row['bid']  
        buyaskprice = float('NaN')
        buystrike = float('NaN')
        row_inner_found = []
        if row['ty'] == 'C':         
            for index_inner,row_inner in df_01.iterrows():
                if row_inner['ty'] == row['ty']:
                    if float(row_inner['strike_at_sell_price']) == float(row['strike_at_sell_price'])+myspreadindollars:
                        row_inner_found = row_inner
                        buyaskprice = row_inner['ask']
                        buystrike = row_inner['strike_at_sell_price']
                        #print('CALL >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                        
        if row['ty'] == 'P':
            for index_inner,row_inner in df_01.iterrows():
                if row_inner['ty'] == row['ty']:
                    if float(row_inner['strike_at_sell_price']) == float(row['strike_at_sell_price'])-myspreadindollars:
                        row_inner_found = row_inner
                        buyaskprice = row_inner['ask']
                        buystrike = row_inner['strike_at_sell_price']
                        #print('PUT >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        candidaterows.append([myoptiontype,sellstockprice,pdeltapct_to_sell_price,sellstrike,buystrike,sellcumprob,buycumprob,sellbidprice,buyaskprice,round(float(sellbidprice)-float(buyaskprice),3),myexdate.strftime('%Y-%m-%d'),daysbackmid])
        #print(myexdate.strftime('%Y-%m-%d'),myoptiontype,sellstockprice,pdeltapct_to_sell_price,sellstrike,buystrike,sellcumprob,sellbidprice,buyaskprice,round(float(sellbidprice)-float(buyaskprice),3))
        #print(row)
        #print('row_inner_found ------------------------------------------------')
        #print(row_inner_found)

headers = candidaterows.pop(0)
df_02 = pd.DataFrame(candidaterows,columns=headers)
print(df_02)
print('End: Candidate where cumprob_to_sell_price is between my specified range')

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
f = pullprices.stockhistorybackfilledtodatframeofstockhistoryinstances('^VIX', longago_string, str(today_date))




df_02.to_csv(myoutputfolder + "\\ironcondor candidates " + symbol +  " " + datestringforfilename + ".csv",columns=('ty','stkp','spdel','sstrk','bstrk','scump','bcump','sbid','bask','capt','myexdate','daysbackmid'))

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