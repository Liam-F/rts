# -*- coding: utf-8 -*-
"""
Created on Sat May  9 16:43:23 2015

@author: jmalinchak
"""

# ##########
# Parameters
symbol = 'SPY'
mycomparesym = '^VIX'
expirationdate_string = '2015-07-24'
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
myoutputfolder = 'C:\\Batches\\rts\\output\\condor\\candidates'
myselectedcondorsfolder = 'C:\\Batches\\rts\\output\\condor\\selected'
cachefolder = 'C:\\Batches\\rts\\output\\cache'
#myoutputfolder = 'C:\\Batches\\MyPython\\active\\output'
#myoutputfolder = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\New Folder\\output'

import csv
import os
mysymboloutputfolder = os.path.join(myoutputfolder,symbol)
import mytools
mytools.general.make_sure_path_exists(mysymboloutputfolder)

# ##########
# Date setup
import datetime

today_datetime = datetime.datetime.today()
use_date = datetime.date.today()

while True :
    today_date = use_date
    expire_date = datetime.datetime.strptime(expirationdate_string,'%Y-%m-%d').date()
    if today_date != expire_date:
        break
    use_date = today_date - datetime.timedelta(hours=24)

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
d_stockpricechanges = builddataframeofrefdateminusd2tod1stockpricechanges.perform(symbol,numberofweekstolookback,daysbackmid,daysbackfar,showresults).DataFrameResult

number_of_observations = len(d_stockpricechanges.index)
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
d_comparestockpricehistory = pullprices.stockhistorybackfilledtodatframeofstockhistoryinstances(comparesym, startdatecalculated_string, str(today_date))
compare_stock_price = pullprices.stock(mycomparesym)
print('runtime_delta',datetime.datetime.today() - today_datetime)

#print(f.loc[f.index == '2015-06-18'])
#f1 = f.loc[f.index.isin(['2015-06-18'])][['Adj Close']]


# ################################################################################################################
# performs some general statistics
import pandas as pd
d_std = pd.rolling_std(d_stockpricechanges[['DrawDownPctChange', 'DrawUpPctChange']], RollingNumberOfPeriods)
d_mean = pd.rolling_mean(d_stockpricechanges[['DrawDownPctChange', 'DrawUpPctChange']], RollingNumberOfPeriods)

# #########################################################################
# Adds a column to dataframe to Compare data to something (VIX for example)
d_stockpricechanges['comppratfar'] = float('NaN')
d_stockpricechanges['breachedaboveorbelow'] = int(0)

#print(d_stockpricechanges)
# #######################################################################################
# Counts number of observations that hit above and below threshold during trading period
idrawbeyond_upabove = 0
idrawbeyond_downbelow = 0

#icountfartomidbeyond_above = 0
#icountfartomidbeyond_below = 0
for index, row in d_stockpricechanges.iterrows():
    fartomidpricechangedelta = (row['priceDaysBackMid'] - row['priceDaysBackFar']) / row['priceDaysBackFar']
    if row['DrawUpPctChange'] > ThreshholdAbove:
        idrawbeyond_upabove = idrawbeyond_upabove + 1
    if row['DrawDownPctChange'] > abs(ThreshholdBelow):
        idrawbeyond_downbelow = idrawbeyond_downbelow + 1
    # #################################################
    # Populates the comppratfar field (VIX for example)
    #row['comppratfar'] = d_comparestockpricehistory.ix[row.index, 'Adj Close']
    #d_stockpricechanges['comppratfar'][str(index.date())] = d_comparestockpricehistory.ix[row['dateDaysBackFar'], 'Adj Close']
    d_stockpricechanges['comppratfar'][str(index.date())] = d_comparestockpricehistory['Adj Close'][row['dateDaysBackFar']]
    
    #str(index.date())


if showresults == 1:
    # ==========
    print(d_stockpricechanges)    
   # ==========
       
if showresults == 1:
    print('Last DrawUpPctChange Mean',d_mean.ix[len(d_mean.index)-1,'DrawUpPctChange'])
    print('Last DrawUpPctChange Std',d_std.ix[len(d_std.index)-1,'DrawUpPctChange'])
    
    print('---------------------------------')
    print('Percent Beyond Draw Up')
    print('---------------------------------')
    print('  ',symbol
            ,'{percent:.2%}'.format(percent=idrawbeyond_upabove/len(d_stockpricechanges.index))
            ,'of the'
            ,len(d_stockpricechanges.index)
            ,'observations closed above the '
            ,'{percent:.2%}'.format(percent=ThreshholdAbove)
            ,'threshold between t-',daysbackfar,'and t-',daysbackmid,', a total of'
            ,idrawbeyond_upabove
            ,'observations'
        )
    
    print('---------------------------------')
    print('Percent Beyond Draw Down')
    print('---------------------------------')
    print('  ',symbol
            ,'{percent:.2%}'.format(percent=idrawbeyond_downbelow/len(d_stockpricechanges.index))
            ,'of the'
            ,len(d_stockpricechanges.index)
            ,'observations closed below the'
            ,'{percent:.2%}'.format(percent=ThreshholdBelow)
            ,'threshold between t-',daysbackfar,'and t-',daysbackmid,', a total of'
            ,idrawbeyond_downbelow
            ,'observations'
        )




#////////////////////////////////////////////////////
#               Draw Up and Draw Down analysis 
import scipy.stats as ss
import numpy as np
import matplotlib.pyplot as plt
#////////////////////////////////////////////////////
#               Draw Up analysis
print('')
print(symbol,'Draw Up:',len(d_stockpricechanges.index), 'observations',idrawbeyond_upabove,'breached',ThreshholdAbove)
print('   ','DaysBackFar',daysbackfar,'   DaysBackMid:',daysbackmid)
serDrawUp = pd.Series(d_stockpricechanges['DrawUpPctChange'])

serDrawUp.hist(cumulative=True, normed=1, bins=idrawbeyond_upabove)
maxpercent_drawup = 0
for n in np.linspace(0,1,1000,endpoint=False):
    cumprob_to_sell_price = ss.percentileofscore(serDrawUp, n)    
    if cumprob_to_sell_price >= mycumprobthreshold:
        maxpercent_drawup = n
        print('   ',round(cumprob_to_sell_price,1),'percent of observations closed up inside of','{percent:.2%}'.format(percent=n)),'percent'        
        break
plt.show()

#////////////////////////////////////////////////////
#               Draw Down analysis
print('')
print(symbol,'Draw Down:',len(d_stockpricechanges.index), 'observations',idrawbeyond_upabove,'breached',ThreshholdBelow)
print('   ','DaysBackFar',daysbackfar,'   DaysBackMid:',daysbackmid)
serDrawDown = pd.Series(d_stockpricechanges['DrawDownPctChange'])
serDrawDown.hist(cumulative=True, normed=1, bins=idrawbeyond_downbelow)
maxpercent_drawdown = 0
for n in np.linspace(0,1,1000,endpoint=False):
    cumprob_to_sell_price = ss.percentileofscore(serDrawDown, n)    
    if cumprob_to_sell_price >= mycumprobthreshold:
        maxpercent_drawdown = n
        print('   ',round(cumprob_to_sell_price,1),'percent of observations closed down inside of','{percent:.2%}'.format(percent=(-1.0)*n)),'percent'
        break
plt.show()


# ####################################################
# Get Option Prices
import pullprices as pp
d_optionpricescurrent = pp.options_to_dataframe(symbol,expirationdate_string,0)

if showresults == 1:
    # ==========
    print('-----',symbol,'Option Prices','-----')
    print(d_optionpricescurrent)
    # ==========
    
stockprice = pp.stock(symbol)

# ##########################
# Calculate Analysis Results
#import mytools
osymbol = mytools.get_from_optionsymbol()
rows    = []        
#rows.append(['optionsymbol','stockprice','strike','pdeltapct_to_sell_price','cumprob_to_sell_price','bid','ask','last'])
rows.append(['exdate','symbol','ty','st','strike_at_sell_price','strike_at_buy_price','pdeltapct_to_sell_price','cumprob_to_sell_price','cumprob_to_buy_price','bid','ask','iv','iscandidate'])

d_candidates = {}
pdeltapct_atthreshold_calloption = float('NaN')
pdeltapct_atthreshold_putoption = float('NaN')
previous_pdeltapct_for_put = float('NaN')

# ##################################
# Loop through current option prices

#print(d_optionpricescurrent)
#print('++++++++++++++++++++++++++++++++++++++++++ d_optionpricescurrent')

d_optionpricescurrent['optiontype'] = 'X'
for index, row in d_optionpricescurrent.iterrows():
    optionsymbol = row['optionsymbol']
    d_optionpricescurrent['optiontype'][index] = mytools.get_from_optionsymbol().optiontype(optionsymbol)
    #print(optionsymbol)
    strike_at_sell_price = float(row['strike'])
    strike_at_sell_price_formatted = "%.2f" % strike_at_sell_price
    
    optiontype = mytools.get_from_optionsymbol().optiontype(row['optionsymbol'])
#    if optiontype == 'C':
#        strike_at_buy_price = float(strike_at_sell_price) + float(myspreadindollars)
#    else:
#        strike_at_buy_price = float(strike_at_sell_price) - float(myspreadindollars)

    if optiontype == 'C':
        strike_at_buy_price = float(strike_at_sell_price) + float(1)
    else:
        strike_at_buy_price = float(strike_at_sell_price) - float(1)
        
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
    #print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    if optiontype == 'C':
        if pdeltapct_to_sell_price > 0:
            cumprob_to_sell_price = ss.percentileofscore(serDrawUp, pdeltapct_to_sell_price)
            cumprob_to_buy_price =  ss.percentileofscore(serDrawUp, pdeltapct_to_buy_price)
            if str(pdeltapct_atthreshold_calloption) == 'nan':
                if float(cumprob_to_sell_price) >= float(mycumprobthreshold):
                    print('Yes Call threshold found %%%%%%%%%%%%%%%%%%%%%%%%%%',cumprob_to_sell_price)                    
                    pdeltapct_atthreshold_calloption = pdeltapct_to_sell_price
                    #capturedspread_at_call_threshold_cross
                    print('Call',str(pdeltapct_atthreshold_calloption),'cumprob_to_sell_price > mycumprobthreshold',str(cumprob_to_sell_price),str(mycumprobthreshold),pdeltapct_atthreshold_calloption,pdeltapct_atthreshold_putoption)
#                    # #####################
                
#bbbbbb
    elif optiontype == 'P':
        if pdeltapct_to_sell_price < 0:
            cumprob_to_sell_price = ss.percentileofscore(serDrawUp,(-1.0) * pdeltapct_to_sell_price)
            cumprob_to_buy_price = ss.percentileofscore(serDrawUp,(-1.0) * pdeltapct_to_buy_price)
            
            if str(pdeltapct_atthreshold_putoption) == 'nan':
                
                if float(round(cumprob_to_sell_price,2)) <= float(round(mycumprobthreshold,2)):
                    print('Yes Put threshold found $$$$$$$$$$$$$$$$$$$$$$$$$$',cumprob_to_sell_price)
                    pdeltapct_atthreshold_putoption = previous_pdeltapct_for_put
                    print('Put',str(pdeltapct_atthreshold_putoption),'cumprob_to_sell_price > mycumprobthreshold',str(cumprob_to_sell_price),str(mycumprobthreshold))
#                    # #####################


                previous_pdeltapct_for_put = pdeltapct_to_sell_price
                    
    if cumprob_to_sell_price != float('NaN'):
        if cumprob_to_sell_price > mycumprob_to_sell_price_lowrange and cumprob_to_sell_price < mycumprob_to_sell_price_highrange:
            iscandidate = 1
            # ##########
            # candidates are found and put into a dictionary, you might want some other data storage
            #d_candidates[str(strike_at_sell_price)+optiontype] = row,rows[len(rows)-1]  
        #vvvvvvv
        rows.append([exdate,vsymbol,optiontype,stockprice,strike_at_sell_price,strike_at_buy_price,'{percent:.2%}'.format(percent=pdeltapct_to_sell_price),'{percent:.2%}'.format(percent=cumprob_to_sell_price/100),'{percent:.2%}'.format(percent=cumprob_to_buy_price/100),row['bid'],row['ask'],row['impliedvolatility'],iscandidate])
        #d_candidates[strike_at_sell_price,optiontype] = [symbol,optiontype,stockprice,strike_at_sell_price,'{percent:.2%}'.format(percent=pdeltapct_to_sell_price),round(cumprob_to_sell_price,1),row['bid'],row['ask'],row['impliedvolatility'],iscandidate]
        
    #print(symbol,'price change from ',stockprice,'to strike_at_sell_price',strike_at_sell_price,'(','{percent:.2%}'.format(percent=pdeltapct_to_sell_price),') exp',exdate,cumprob_to_sell_price)
headers = rows.pop(0)
d_cumprobsbystrikeranges = pd.DataFrame(rows,columns=headers)

# qqqqqq
#print(d_cumprobsbystrikeranges)

print('******************************************************************************************')

# #####################
# Based on mycumprobthreshold, how many breached total, up and down
d_stockpricechanges['breachedaboveorbelow'] = int(0)
breachedmycumprobthreshold_total = 0
breachedmycumprobthreshold_up = 0
breachedmycumprobthreshold_down = 0

icountfartomidbeyond_above = 0
icountfartomidbeyond_below = 0

for index, row in d_stockpricechanges.iterrows():
    #fartomidpricechangedelta = (row['priceDaysBackMid'] - row['priceDaysBackFar']) / row['priceDaysBackFar']
    priceToBreachFarToMid_FinishUp = float(row['priceDaysBackFar']) + (float(row['priceDaysBackFar']) * pdeltapct_atthreshold_calloption)
    priceToBreachFarToMid_FinishDown = float(row['priceDaysBackFar']) + (float(row['priceDaysBackFar']) * pdeltapct_atthreshold_putoption)
    if float(row['priceDaysBackMid']) > priceToBreachFarToMid_FinishUp:
        icountfartomidbeyond_above = icountfartomidbeyond_above + 1
    if float(row['priceDaysBackMid']) < priceToBreachFarToMid_FinishDown:
        icountfartomidbeyond_below = icountfartomidbeyond_below + 1
    #print('priceToBreachFarToMid',round(float(row['priceDaysBackMid']),2),'by',round(priceToBreachFarToMid_FinishUp,2),round(priceToBreachFarToMid_FinishDown,2))
    
    isbeyondmycumprobthreshold_total = 0
    if row['DrawUpPctChange'] > pdeltapct_atthreshold_calloption:
        isbeyondmycumprobthreshold_total = 1
        breachedmycumprobthreshold_up = breachedmycumprobthreshold_up + 1
    if row['DrawDownPctChange'] > abs(pdeltapct_atthreshold_putoption):
        isbeyondmycumprobthreshold_total = 1
        breachedmycumprobthreshold_down = breachedmycumprobthreshold_down + 1
    if isbeyondmycumprobthreshold_total != 0:
        breachedmycumprobthreshold_total = breachedmycumprobthreshold_total + 1
        #d_stockpricechanges['breachedaboveorbelow'][str(index.date())] = 'breached mycumprobthreshold (' + str(mycumprobthreshold) + '%) ' + str(pdeltapct_atthreshold_calloption) +  ' ' + str(pdeltapct_atthreshold_putoption) + ' ' + str(isbeyondmycumprobthreshold_total) #breachedaboveorbelow
    d_stockpricechanges['breachedaboveorbelow'][str(index.date())] = isbeyondmycumprobthreshold_total

d_stockpricechanges['pdeltapct_atthreshold_calloption'] = pdeltapct_atthreshold_calloption
d_stockpricechanges['pdeltapct_atthreshold_putoption'] = pdeltapct_atthreshold_putoption

'''
/////////////////////////////////////////////////////////////////////////////////////////
                        SourceData CSV
/////////////////////////////////////////////////////////////////////////////////////////
'''
d_stockpricechanges.to_csv(mysymboloutputfolder + "\\ironcondor sourcedata (" + expirationdate_string + ') '+ symbol +  " " + datestringforfilename + ".csv",columns=('dateDaysBackMid','dateDaysBackFar','priceRefDate','priceDaysBackMid','priceDaysBackFar','DeltaFartoMid','DrawDownMax','DrawUpMax','DrawDownPctChange','DrawUpPctChange','comppratfar','pdeltapct_atthreshold_calloption','pdeltapct_atthreshold_putoption','breachedaboveorbelow'))

                            # ==========
                            #print(d_cumprobsbystrikeranges)
                            # ==========

# ####################################################
# Here is where we find the value of the credit spread
#      still need to build the Put credit spread
candidaterows = []


'''@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                Candidate Header Row
   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'''
candidateheader = ['ty','stkp','spdel','sstrk','bstrk','scump','bcump','sbid','bask','capt','myexdate','currdate','daysbackmid','pricecompare','obsv','sel']
candidaterows.append(candidateheader)

lastmycompareprice = d_comparestockpricehistory['Adj Close'][len(d_comparestockpricehistory)-1]

#print d_cumprobsbystrikeranges
crossedthreshold_call = 0
crossedthreshold_put = 0
sum_of_iter_capt_at_cumprob_cross = float(0)
previousrow = None
for index,row in d_cumprobsbystrikeranges.iterrows():
    sel = ''
    
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

        iter_scump = float(row['cumprob_to_sell_price'].replace('%',''))
        if row['ty'] == 'C' and crossedthreshold_call == 0 and iter_scump >= mycumprobthreshold:
            crossedthreshold_call = 1
            sel = 'x'
            #print '&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'
        if row['ty'] == 'P' and crossedthreshold_put == 0 and iter_scump <= mycumprobthreshold:
            crossedthreshold_put = 1
            prevcandidaterow = candidaterows[len(candidaterows)-1]
            a_indices = [i for i, x in enumerate(candidaterows[0]) if x == 'sel']
            prevcandidaterow[a_indices[0]] = 'x'    

            #print 'tttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt'
            #print prevcandidaterow
            
        if row['ty'] == 'C':         
            for index_inner,row_inner in d_cumprobsbystrikeranges.iterrows():
                if row_inner['ty'] == row['ty']:
                    if float(row_inner['strike_at_sell_price']) == float(row['strike_at_sell_price'])+myspreadindollars:
                        row_inner_found = row_inner
                        buyaskprice = row_inner['ask']
                        buystrike = row_inner['strike_at_sell_price']
                        #print('CALL >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                        
        if row['ty'] == 'P':
            for index_inner,row_inner in d_cumprobsbystrikeranges.iterrows():
                if row_inner['ty'] == row['ty']:
                    if float(row_inner['strike_at_sell_price']) == float(row['strike_at_sell_price'])-myspreadindollars:
                        row_inner_found = row_inner
                        buyaskprice = row_inner['ask']
                        buystrike = row_inner['strike_at_sell_price']

                        #print('PUT >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        previousrow = row
        '''
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                Candidate Value Rows
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        '''

#        row_sel = [x for i, x in enumerate(candidaterows) if x[a_columnidx[0]] == 'x']
#        print(row_sel)
#        row_sel[0][a_columnidx] = round(float(sellbidprice)-float(buyaskprice),3)
#        row_sel[1][a_columnidx] = round(float(sellbidprice)-float(buyaskprice),3)
#        sum_of_iter_capt_at_cumprob_cross = sum_of_iter_capt_at_cumprob_cross - float(prevcandidaterow[a_indices[0]])

        #candidaterows.append(candidateheader)
        candidaterows.append([myoptiontype,sellstockprice,pdeltapct_to_sell_price,sellstrike,buystrike,sellcumprob,buycumprob,sellbidprice,buyaskprice,round(float(sellbidprice)-float(buyaskprice),3),myexdate.strftime('%Y-%m-%d'),datestringforprinting,daysbackmid,compare_stock_price,number_of_observations,sel])
        #print(myexdate.strftime('%Y-%m-%d'),myoptiontype,sellstockprice,pdeltapct_to_sell_price,sellstrike,buystrike,sellcumprob,sellbidprice,buyaskprice,round(float(sellbidprice)-float(buyaskprice),3))
        #print(row)
        #print('row_inner_found ------------------------------------------------')
        #print(row_inner_found)

## #############################
## Example of List Comprehension
#a_columnidx = [i for i, x in enumerate(candidaterows[0]) if x == 'sel']
#print('x[a_columnidx[0]]',a_columnidx[0])
#for r in candidaterows:
#    if r[a_columnidx[0]] == 'x':                
#        print(r)


headers = candidaterows.pop(0)
d_candidates = pd.DataFrame(candidaterows,columns=headers)

## The above is equivalent to below
#d_selectionstoappendtocsv = {}
#for k,candidaterow in d_candidates.iterrows():
#    if candidaterow['sel'] == 'x':
#        d_selectionstoappendtocsv[len(d_selectionstoappendtocsv)] = candidaterow        
#print('2 ##########################################')
#print(d_selectionstoappendtocsv)

'''@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                Candidate Value CSV
   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'''
mycolumns='ty','stkp','spdel','sstrk','bstrk','scump','bcump','sbid','bask','capt','myexdate','currdate','daysbackmid','pricecompare','obsv','sel'
d_candidates.to_csv(mysymboloutputfolder + "\\ironcondor candidates (" + expirationdate_string + ') ' + symbol +  " " + datestringforfilename + ".csv",columns=('ty','stkp','spdel','sstrk','bstrk','scump','bcump','sbid','bask','capt','myexdate','currdate','daysbackmid','pricecompare','obsv','sel'))

# #################################################
# Use Dictionary Comprehension to get selected rows
selectedcondorrows = []
'''@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                Candidate Header Row
   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'''

dict_selectedcondorrows = { k:r for k,r in d_candidates.iterrows() if r['sel'] == 'x'}
print('1 ##########################################')
print(dict_selectedcondorrows)
print('Try dict',type(dict_selectedcondorrows) is dict)
print(list(dict_selectedcondorrows.items()))
print('2 ##########################################')

filepath_to_selectedcondors = os.path.join(myselectedcondorsfolder,expirationdate_string + ' ' + symbol + '.csv')
#import os

#Python 2-3 differences
d_selectedcondorrows = pd.DataFrame(dict_selectedcondorrows, columns=['ty','stkp','spdel','sstrk','bstrk','scump','bcump','sbid','bask','capt','myexdate','currdate','daysbackmid','pricecompare','obsv','sel'])
print(d_selectedcondorrows)
#d_selectedcondorrows = pd.DataFrame(dict_selectedcondorrows.items(), columns=['ty','stkp','spdel','sstrk','bstrk','scump','bcump','sbid','bask','capt','myexdate','currdate','daysbackmid','pricecompare','obsv','sel'])

print('3 ##########################################')
print(d_selectedcondorrows)
if os.path.isfile(filepath_to_selectedcondors) != True:
    d_selectedcondorrows.to_csv(filepath_to_selectedcondors,columns=('ty','stkp','spdel','sstrk','bstrk','scump','bcump','sbid','bask','capt','myexdate','currdate','daysbackmid','pricecompare','obsv','sel'))
    
if len(d_selectedcondorrows) > 0:
    d_fromcsv = pd.read_csv(filepath_to_selectedcondors, index_col=0)
    with open(filepath_to_selectedcondors, 'a') as f:
        (d_selectedcondorrows).to_csv(f, header=False)
#    mytools.general.make_sure_filepath_exists(filepath_to_selectedcondors)
#    #import csv
#    with open(filepath_to_selectedcondors, 'r+b') as f:
#        header = next(csv.reader(f))
#        dict_writer = csv.DictWriter(f, header, -999)
#        dict_writer.writerow(dict_selectedcondorrows)


#print(d_candidates)

crossedthreshold_call = 0
crossedthreshold_put = 0
capturedspread_at_call_threshold_cross = float('Nan')
capturedspread_at_put_threshold_cross = float('Nan')
sellstrike_at_call_threshold_cross = float('Nan')
sellstrike_at_put_threshold_cross = float('Nan')

previousrow = None
for index,row in d_candidates.iterrows():
    iter_scump = float(row['scump'].replace('%',''))
    if row['ty'] == 'C' and crossedthreshold_call == 0 and iter_scump >= mycumprobthreshold:
        crossedthreshold_call = 1
        capturedspread_at_call_threshold_cross = float(row['capt'])
        sellstrike_at_call_threshold_cross = float(row['sstrk'])
    if row['ty'] == 'P' and crossedthreshold_put == 0 and iter_scump <= mycumprobthreshold:
        crossedthreshold_put = 1
        capturedspread_at_put_threshold_cross = float(previousrow['capt'])
        sellstrike_at_put_threshold_cross = float(previousrow['sstrk'])
    previousrow = row
    #print('scump=',iter_scump)

print('-----------------')
print('Symbol:',symbol)
print('  Current stock price:',round(stockprice,2))
print('  Today:',today_date)
print('  Expire Date:',expire_date )
print('  Number of Days to Expiration:',delta.days)
print('  Price changes start date:',startdatecalculated_string)
print('  Number Of Observations Found',number_of_observations)
print('  Price delta % for strike to meet',str(mycumprobthreshold)+'%','cumprob threshold (Call):','{percent:.2%}'.format(percent=pdeltapct_atthreshold_calloption))
print('  Price delta % for strike to meet',str(mycumprobthreshold)+'%','cumprob threshold (Put):','{percent:.2%}'.format(percent=pdeltapct_atthreshold_putoption))


print('DRAW UP & DOWN ---- What happened during')
print('    Breaches at',mycumprobthreshold,'% cumulative prob threshold (Far to Mid)')

print('    Count of Draw UP breaches:  ',breachedmycumprobthreshold_up)
print('    Count of Draw DOWN breaches:',breachedmycumprobthreshold_down)
print('    Count of Draw TOTAL breaches:  ',breachedmycumprobthreshold_total,'of',number_of_observations)
print('    Prcnt of Draw TOTAL breaches:  ','{percent:.2%}'.format(percent=(breachedmycumprobthreshold_total)/float(number_of_observations)))
print('FINISH ---- What happened during')
print('    Count finishes.... Above price set by cumprob threshold=',icountfartomidbeyond_above)
print('    Count finishes.... Below price set by cumprob threshold=',icountfartomidbeyond_below)
print('    Count finishes.... Above or below price set by cumprob =',icountfartomidbeyond_above+icountfartomidbeyond_below,'of',number_of_observations)
print('    Prcnt finishes.... Above or below price set by cumprob =','{percent:.2%}'.format(percent=(icountfartomidbeyond_above+icountfartomidbeyond_below)/float(number_of_observations)))

print('Condor Specs--------')
print('    sellstrike_at_call_threshold_cross=',round(sellstrike_at_call_threshold_cross,2))
print('    sellstrike_at_put_threshold_cross=',round(sellstrike_at_put_threshold_cross,2))
print('    Capture at Call threshold:',capturedspread_at_call_threshold_cross)
print('    Capture at Put threshold:',capturedspread_at_put_threshold_cross)
print('    Capture Total Amt=',round(capturedspread_at_call_threshold_cross+capturedspread_at_put_threshold_cross,2))
print('    sum_of_iter_capt_at_cumprob_cross',sum_of_iter_capt_at_cumprob_cross)
print('  Note: candidates occur where stock price does not close at levels set by cumprob sell price, meaning your condor was a success')
print('  ',mycomparesym+':',round(compare_stock_price,2))
print('-----------------')
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
        d_optionpricescurrent = pd.DataFrame(rows, columns=headers)
        #import numpy as np
        d_optionpricescurrent['stockprice'] = stockprice
'''