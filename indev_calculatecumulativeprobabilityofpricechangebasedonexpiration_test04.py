# -*- coding: utf-8 -*-
"""
Created on Sat May  9 16:43:23 2015

@author: jmalinchak
"""

# ##########
# Parameters
symbol = 'SPY'
mycomparesym = '^VIX'
expirationdate_string = '2015-07-17'
daysbackmid = 0
myspreadindollars = 1
mycumprob_to_sell_price_lowrange = 0
mycumprob_to_sell_price_highrange = 95
numberofweekstolookback = 300
RollingNumberOfPeriods = 120
showresults = 0
ThreshholdAbove = 0.0247 #Percent change above
ThreshholdBelow = -0.0158  #Percent change below
#myoutputfolder = 'C:\\Batches\\MyPython\\active\\output'
myoutputfolder = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\New Folder\\output'



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

daysbackfar = delta.days

import builddataframeofrefdateminusd2tod1stockpricechanges
df_0 = builddataframeofrefdateminusd2tod1stockpricechanges.perform(symbol,numberofweekstolookback,daysbackmid,daysbackfar,showresults).DataFrameResult

number_of_observations = len(df_0.index)
print('  Number Of Observations Found',number_of_observations)

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

#print(f.loc[f.index == '2015-06-18'])

#f1 = f.loc[f.index.isin(['2015-06-18'])][['Adj Close']]


# ################################################################################################################
# performs some general statistics
import pandas as pd
df_std = pd.rolling_std(df_0[['DrawDownPctChange', 'DrawUpPctChange']], RollingNumberOfPeriods)
df_mean = pd.rolling_mean(df_0[['DrawDownPctChange', 'DrawUpPctChange']], RollingNumberOfPeriods)

# #########################################################################
# Adds a column to dataframe to Compare data to something (VIX for example)
df_0['compareiv'] = float('NaN')
df_0['breachedaboveorbelow'] = int(0)

# #######################################################################################
# Counts number of observations that hit above and below threshold during trading period
ibeyondabove = 0
ibeyondbelow = 0
ibeyondtotal = 0
for index, row in df_0.iterrows():
    fartomidpricechangedelta = (row['priceDaysBackMid'] - row['priceDaysBackFar']) / row['priceDaysBackFar']
    #if abs(fartomidpricechangedelta) > 0.1:
    #    print('Far to Mid price delta',fartomidpricechangedelta,row['dateDaysBackMid'],row['dateDaysBackFar'])
    breachedaboveorbelow = 0
    #print('xxxxxxxxxxxxxxxxxxx',row)

    if row['DrawUpPctChange'] > ThreshholdAbove:
        ibeyondabove = ibeyondabove + 1
        ibeyondtotal = ibeyondtotal + 1
        breachedaboveorbelow = 1
    if row['DrawDownPctChange'] > abs(ThreshholdBelow):
        ibeyondbelow = ibeyondbelow + 1
        ibeyondtotal = ibeyondtotal + 1
        breachedaboveorbelow = 1
    # #######################################################################################
    # Populates the compareiv field (VIX for example)
    #row['compareiv'] = df_compare.ix[row.index, 'Adj Close']
    #df_0['compareiv'][str(index.date())] = df_compare.ix[row['dateDaysBackFar'], 'Adj Close']
    df_0['compareiv'][str(index.date())] = df_compare['Adj Close'][row['dateDaysBackFar']]
    df_0['breachedaboveorbelow'][str(index.date())] = breachedaboveorbelow
    #str(index.date())

df_0.to_csv(myoutputfolder + "\\ironcondor sourcedata " + symbol +  " " + datestringforfilename + ".csv",columns=('dateDaysBackMid','dateDaysBackFar','priceRefDate','priceDaysBackMid','priceDaysBackFar','DeltaFartoMid','DrawDownMax','DrawUpMax','DrawDownPctChange','DrawUpPctChange','compareiv','breachedaboveorbelow'))
if showresults == 1:
    # ==========
    print(df_0)    
   # ==========
       
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

import numpy as np
import scipy.stats as ss

# #################
# Draw Up analysis
print('')
print(symbol,'Draw Up:',len(df_0.index), 'observations',ibeyondabove,'breached',ThreshholdAbove)
print('   ','DaysBackFar',daysbackfar,'   DaysBackMid:',daysbackmid)
serDrawUp = pd.Series(df_0['DrawUpPctChange'])
serDrawUp.hist(cumulative=True, normed=1, bins=ibeyondabove)
maxpercent_drawup = 0
for n in np.linspace(0,1,1000,endpoint=False):
    cumprob_to_sell_price = ss.percentileofscore(serDrawUp, n)    
    if cumprob_to_sell_price >= 80:
        maxpercent_drawup = n
        print('   ',round(cumprob_to_sell_price,1),'percent of observations closed up inside of','{percent:.2%}'.format(percent=n)),'percent'        
        break
plt.show()

# #################
# Draw Down analysis
print('')
print(symbol,'Draw Down:',len(df_0.index), 'observations',ibeyondabove,'breached',ThreshholdBelow)
print('   ','DaysBackFar',daysbackfar,'   DaysBackMid:',daysbackmid)
serDrawDown = pd.Series(df_0['DrawDownPctChange'])
serDrawDown.hist(cumulative=True, normed=1, bins=ibeyondbelow)
maxpercent_drawdown = 0
for n in np.linspace(0,1,1000,endpoint=False):
    cumprob_to_sell_price = ss.percentileofscore(serDrawDown, n)    
    if cumprob_to_sell_price >= 80:
        maxpercent_drawdown = n
        print('   ',round(cumprob_to_sell_price,1),'percent of observations closed down inside of','{percent:.2%}'.format(percent=(-1.0)*n)),'percent'
        break
plt.show()

import pullprices as pp
df = pp.options_to_dataframe(symbol,expirationdate_string,0)

if showresults == 1:
    # ==========
    print('-----',symbol,'Option Prices','-----')
    print(df)
    # ==========
    
stockprice = pp.stock(symbol)


# ##########################
# Calculate Analysis Results
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
df_02.to_csv(myoutputfolder + "\\ironcondor candidates " + symbol +  " " + datestringforfilename + ".csv",columns=('ty','stkp','spdel','sstrk','bstrk','scump','bcump','sbid','bask','capt','myexdate','daysbackmid'))
print(df_02)
print('-----------------')
print('Symbol:',symbol)
print('  Current stock price:',stockprice)
print('  Compared to:',mycomparesym)
print('  Today:',today_date)
print('  Expire Date:',expire_date )
print('  Number of Days to Expiration:',delta.days)
print('  Start Date:',startdatecalculated_string)
print('  Number Of Observations Found',number_of_observations)
print('  Note: Candidate where cumprob_to_sell_price is between my specified range')
print('-----------------')
print('End of Process')



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