# -*- coding: utf-8 -*-
"""
Created on Sat May  9 16:43:23 2015

@author: jmalinchak
"""


def find(mysymbol = 'SPY'
        ,  mycomparesymbol = '^VIX'
        ,  myweeksahead = 8
        ,  expirationday='friday'):
    # ##########
    # Parameters
    import config
    
    
    
    symbol = 'SPY'
    mycomparesym = '^VIX'
    numberofweeksahead = 8
    expirationday = 'friday' #'friday' #'wednesday'
    
    #replaced by iterdate expirationdate_string = '2015-07-17' #['2015-07-17','2015-07-24','2015-07-31','2015-08-07']
    daysbackmid = 0
    myspreadindollars = 1
    mycumprobthreshold = 80 #Percent in whole number 80 = 80%
    mycumprob_to_sell_price_lowrange = 0
    mycumprob_to_sell_price_highrange = 100 # was 95
    numberofweekstolookback = 150
    RollingNumberOfPeriods = 120
    showresults = 0
    
    ThreshholdAbove = 0.0001 #Percent change above
    ThreshholdBelow = -0.0001  #Percent change below
    
    mycandidatesfolder = config.mycandidatesfolder #'C:\\Batches\\rts\\output\\condor\\candidates'
    mysourcedatafolder = config.mysourcedatafolder #'C:\\Batches\\rts\\output\\condor\\candidates'
    myselectedcandidatesfolder = config.myselectedcandidatesfolder #'C:\\Batches\\rts\\output\\condor\\selectedcandidates'
    mycachefolder = config.mycachefolder #'C:\\Batches\\rts\\output\\cache'
    print('mycandidatesfolder',mycandidatesfolder)
    #mycandidatesfolder = 'C:\\Batches\\MyPython\\active\\output'
    #mycandidatesfolder = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\New Folder\\output'
    
    import ntpath
    def path_leaf(path):
        head, tail = ntpath.split(path)
        return tail or ntpath.basename(head)
    
    def path_base(path):
        head, tail = ntpath.split(path)
        return head or ntpath.basename(head)    
    #def getdictitem(thedict,key):
    def dayofweek_int(dayofweek_word):
        rv = int(-1)
        if dayofweek_word.lower() == 'friday':
            rv = int(4)
        if dayofweek_word.lower() == 'saturday':
            rv = int(5)
        if dayofweek_word.lower() == 'sunday':
            rv = int(6)
        if dayofweek_word.lower() == 'monday':
            rv = int(0)
        if dayofweek_word.lower() == 'tuesday':
            rv = int(1)
        if dayofweek_word.lower() == 'wednesday':
            rv = int(2)
        if dayofweek_word.lower() == 'thursday':
            rv = int(3)
        return rv
        
    #import csv
    import os
    candidatesfolderwithsymbol = os.path.join(mycandidatesfolder,symbol)
    sourcedatafolderwithsymbol = os.path.join(mysourcedatafolder,symbol)
    import mytools
    mygeneral = mytools.general()
    mygeneral.make_sure_path_exists(candidatesfolderwithsymbol) #candidatesfolderwithsymbol
    mygeneral.make_sure_path_exists(sourcedatafolderwithsymbol) #sourcedatafolderwithsymbol
    ## ##########
    ## Date setup
    #import datetime
    #
    #today_datetime = datetime.datetime.today()
    #today_date = datetime.date.today()
    
    
    # ##########
    # Date setup
    import datetime
    today_datetime = datetime.datetime.today()
    today_date = datetime.date.today()
    iter_date = today_date
    
    for expirationcounter in range(numberofweeksahead):
        
        while iter_date.weekday() != dayofweek_int(expirationday):
            iter_date += datetime.timedelta(1)    
        expirationdate_string = str(iter_date)
        iter_date += datetime.timedelta(1)
        print('Doing...',expirationcounter,expirationdate_string)
    
        while True :
           # today_date = today_date
            expire_date = datetime.datetime.strptime(expirationdate_string,'%Y-%m-%d').date()
            if today_date != expire_date:
                break
            today_date = today_date - datetime.timedelta(hours=24)
        
        delta = expire_date - today_date
        
        # ####################################################
        # Get Option Prices
        pricingsymbol = symbol
        if pricingsymbol in ['VIX','RUT']:
            pricingsymbol = '^'+symbol
            
        import pullprices as pp
        df_optionpricescurrent = pp.options_to_dataframe(pricingsymbol,expirationdate_string,0)
        #print('$$$$$$$$$$$$$ cvcvcvcvc $$$$$$$$$$$$$$$$$')
        #print(df_optionpricescurrent)
        if showresults == 1:
            # ==========
            print('-----',symbol,'Option Prices','-----')
            #print(df_optionpricescurrent)
            # ==========
        if len(df_optionpricescurrent) == 0:
            print('-:-:-:-:-:--:-:-:-:-:--:-:-:-:-:- no option prices found for',pricingsymbol,expirationdate_string)
        else:
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
            datestringforcsv = today_datetime.strftime('%Y-%m-%d %H:%M:%S.%f')
            datestringforprinting = today_datetime.strftime('%Y-%m-%d %H:%M') 
            
            daysbackfar = delta.days
            
            import builddataframeofrefdateminusd2tod1stockpricechanges
             
            df_stockpricechanges_unfiltered = builddataframeofrefdateminusd2tod1stockpricechanges.perform(pricingsymbol,numberofweekstolookback,daysbackmid,daysbackfar,showresults).DataFrameResult
            df_stockpricechanges = df_stockpricechanges_unfiltered.dropna(subset=['priceDaysBackFar'])    
            #print(df_stockpricechanges)
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
            startdatecalculatedf_datetime = today_datetime - datedelta
            startdatecalculatedf_string = str(startdatecalculatedf_datetime.date())
            print('  Start Date:',startdatecalculatedf_string)
            
            
            # ###########################
            # Get VIX or comparable stock
            import pullprices
            df_comparestockpricehistory = pullprices.stockhistorybackfilledtodatframeofstockhistoryinstances(comparesym, startdatecalculatedf_string, str(today_date))
            compare_stock_price = pullprices.stock(mycomparesym)
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
            
            #print(df_stockpricechanges)
            # #######################################################################################
            # Counts number of observations that hit above and below threshold during trading period
            idrawbeyondf_upabove = 0
            idrawbeyondf_downbelow = 0
            
            #icountfartomidbeyondf_above = 0
            #icountfartomidbeyondf_below = 0
            
            #zzzzz error was here
            #print df_comparestockpricehistory
            
            for index, row in df_stockpricechanges.iterrows():
                try:
                    fartomidpricechangedelta = (row['priceDaysBackMid'] - row['priceDaysBackFar']) / row['priceDaysBackFar']
                except:
                    fartomidpricechangedelta = float('NaN')
                if row['DrawUpPctChange'] > ThreshholdAbove:
                    idrawbeyondf_upabove = idrawbeyondf_upabove + 1
                if row['DrawDownPctChange'] > abs(ThreshholdBelow):
                    idrawbeyondf_downbelow = idrawbeyondf_downbelow + 1
                # #################################################
                # Populates the comppratfar field (VIX for example)
                #row['comppratfar'] = df_comparestockpricehistory.ix[row.index, 'Adj Close']
                #df_stockpricechanges['comppratfar'][str(index.date())] = df_comparestockpricehistory.ix[row['dateDaysBackFar'], 'Adj Close']
                #print row['dateDaysBackFar'],str(index.date())
                #zzzzz error was here
                if row['dateDaysBackFar'] in df_comparestockpricehistory.index:
                    df_stockpricechanges['comppratfar'][str(index.date())] = df_comparestockpricehistory['Adj Close'][row['dateDaysBackFar']]
                    #df_stockpricechanges.set_value(str(index.date()), 'comppratfar',  df_comparestockpricehistory[df_comparestockpricehistory.'Adj Close' == row['dateDaysBackFar']])
                   # df_stockpricechanges['comppratfar'][str(index.date())] = 
                
                #str(index.date())
            
            
        #    if showresults == 1:
        #        # ==========
        #        print(df_stockpricechanges)    
        #       # ==========
                   
            if showresults == 1:
                print('Last DrawUpPctChange Mean',df_mean.ix[len(df_mean.index)-1,'DrawUpPctChange'])
                print('Last DrawUpPctChange Std',df_std.ix[len(df_std.index)-1,'DrawUpPctChange'])
                
                print('---------------------------------')
                print('Percent Beyond Draw Up')
                print('---------------------------------')
                print('  ',symbol
                        ,'{percent:.2%}'.format(percent=idrawbeyondf_upabove/len(df_stockpricechanges.index))
                        ,'of the'
                        ,len(df_stockpricechanges.index)
                        ,'observations closed above the '
                        ,'{percent:.2%}'.format(percent=ThreshholdAbove)
                        ,'threshold between t-',daysbackfar,'and t-',daysbackmid,', a total of'
                        ,idrawbeyondf_upabove
                        ,'observations'
                    )
                
                print('---------------------------------')
                print('Percent Beyond Draw Down')
                print('---------------------------------')
                print('  ',symbol
                        ,'{percent:.2%}'.format(percent=idrawbeyondf_downbelow/len(df_stockpricechanges.index))
                        ,'of the'
                        ,len(df_stockpricechanges.index)
                        ,'observations closed below the'
                        ,'{percent:.2%}'.format(percent=ThreshholdBelow)
                        ,'threshold between t-',daysbackfar,'and t-',daysbackmid,', a total of'
                        ,idrawbeyondf_downbelow
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
            print(symbol,'Draw Up:',len(df_stockpricechanges.index), 'observations',idrawbeyondf_upabove,'breached',ThreshholdAbove)
            print('   ','DaysBackFar',daysbackfar,'   DaysBackMid:',daysbackmid)
            serDrawUp = pd.Series(df_stockpricechanges['DrawUpPctChange'])
            
            serDrawUp.hist(cumulative=True, normed=1, bins=idrawbeyondf_upabove)
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
            print(symbol,'Draw Down:',len(df_stockpricechanges.index), 'observations',idrawbeyondf_upabove,'breached',ThreshholdBelow)
            print('   ','DaysBackFar',daysbackfar,'   DaysBackMid:',daysbackmid)
            serDrawDown = pd.Series(df_stockpricechanges['DrawDownPctChange'])
            serDrawDown.hist(cumulative=True, normed=1, bins=idrawbeyondf_downbelow)
            maxpercent_drawdown = 0
            for n in np.linspace(0,1,1000,endpoint=False):
                cumprob_to_sell_price = ss.percentileofscore(serDrawDown, n)    
                if cumprob_to_sell_price >= mycumprobthreshold:
                    maxpercent_drawdown = n
                    print('   ',round(cumprob_to_sell_price,1),'percent of observations closed down inside of','{percent:.2%}'.format(percent=(-1.0)*n)),'percent'
                    break
            plt.show()
            
                
            stockprice = pp.stock(pricingsymbol)
            
            # ##########################
            # Calculate Analysis Results
            #import mytools
            osymbol = mytools.get_from_optionsymbol()
            rows_optionpricescurrent    = []        
            #rows_optionpricescurrent.append(['optionsymbol','stockprice','strike','pdeltapct_to_sell_price','cumprob_to_sell_price','bid','ask','last'])
            rows_optionpricescurrent.append(['optionsymbol','exdate','symbol','ty','st','strike_at_sell_price','strike_at_buy_price','pdeltapct_to_sell_price','cumprob_to_sell_price','cumprob_to_buy_price','bid','ask','iv','iscandidate'])
            
            #df_candidates = {}
            pdeltapct_atthreshold_calloption = float('NaN')
            pdeltapct_atthreshold_putoption = float('NaN')
            previous_pdeltapct_for_put = float('NaN')
            
            # ##################################
            # Loop through current option prices
            
            #print(df_optionpricescurrent)
            #print('++++++++++++++++++++++++++++++++++++++++++ df_optionpricescurrent')
            if df_optionpricescurrent is None:
                print('There are no option prices for ' + symbol + ' expdate: '+expirationdate_string)
               
            else:
                df_optionpricescurrent['optiontype'] = 'X'
                
                
                for index, row in df_optionpricescurrent.iterrows():
                    optionsymbol = row['optionsymbol']
                    df_optionpricescurrent['optiontype'][index] = mytools.get_from_optionsymbol().optiontype(optionsymbol)
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
                    #print('stockprice',stockprice)
                    pdeltapct_to_sell_price = (float(strike_at_sell_price) - float(stockprice)) / float(stockprice)
                    #print('pdeltapct_to_sell_price',pdeltapct_to_sell_price)
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
                            #print('cumprob_to_sell_price',cumprob_to_sell_price,mycumprobthreshold)
                            if str(pdeltapct_atthreshold_calloption).lower() == 'nan':
                                if float(cumprob_to_sell_price) >= float(mycumprobthreshold):
                                    print('Yes Call threshold found %%%%%%%%%%%%%%%%%%%%%%%%%%',cumprob_to_sell_price)                    
                                    pdeltapct_atthreshold_calloption = pdeltapct_to_sell_price
                                    #capturedspreadf_at_call_thresholdf_cross
                                    print('Call',str(pdeltapct_atthreshold_calloption),'cumprob_to_sell_price > mycumprobthreshold',str(cumprob_to_sell_price),str(mycumprobthreshold),pdeltapct_atthreshold_calloption,pdeltapct_atthreshold_putoption)
                #                    # #####################
                                else:
                                    print('  No Call threshold found :::::::::::','float(cumprob_to_sell_price) >= float(mycumprobthreshold)',cumprob_to_sell_price,mycumprobthreshold)
                                
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
                            #df_candidates[str(strike_at_sell_price)+optiontype] = row,rows[len(rows)-1]  
                        #vvvvvvv
                        rows_optionpricescurrent.append([optionsymbol,exdate,vsymbol,optiontype,stockprice,strike_at_sell_price,strike_at_buy_price,'{percent:.2%}'.format(percent=pdeltapct_to_sell_price),'{percent:.2%}'.format(percent=cumprob_to_sell_price/100),'{percent:.2%}'.format(percent=cumprob_to_buy_price/100),row['bid'],row['ask'],row['impliedvolatility'],iscandidate])
                        #df_candidates[strike_at_sell_price,optiontype] = [symbol,optiontype,stockprice,strike_at_sell_price,'{percent:.2%}'.format(percent=pdeltapct_to_sell_price),round(cumprob_to_sell_price,1),row['bid'],row['ask'],row['impliedvolatility'],iscandidate]
                        
                    #print(symbol,'price change from ',stockprice,'to strike_at_sell_price',strike_at_sell_price,'(','{percent:.2%}'.format(percent=pdeltapct_to_sell_price),') exp',exdate,cumprob_to_sell_price)
                headers = rows_optionpricescurrent.pop(0)
                df_cumprobsbystrikeranges = pd.DataFrame(rows_optionpricescurrent,columns=headers)
                
                # qqqqqq
                #print(df_cumprobsbystrikeranges)
                
                print('----------------------------- ok got here -------------------------------------')
                
                # #####################
                # Based on mycumprobthreshold, how many breached total, up and down
                df_stockpricechanges['breachedaboveorbelow'] = int(0)
                breachedmycumprobthresholdf_total = 0
                breachedmycumprobthresholdf_up = 0
                breachedmycumprobthresholdf_down = 0
                
                icountfartomidbeyondf_above = 0
                icountfartomidbeyondf_below = 0
                
                for index, row in df_stockpricechanges.iterrows():
                    #fartomidpricechangedelta = (row['priceDaysBackMid'] - row['priceDaysBackFar']) / row['priceDaysBackFar']
                    priceToBreachFarToMidf_FinishUp = float(row['priceDaysBackFar']) + (float(row['priceDaysBackFar']) * pdeltapct_atthreshold_calloption)
                    priceToBreachFarToMidf_FinishDown = float(row['priceDaysBackFar']) + (float(row['priceDaysBackFar']) * pdeltapct_atthreshold_putoption)
                    if float(row['priceDaysBackMid']) > priceToBreachFarToMidf_FinishUp:
                        icountfartomidbeyondf_above = icountfartomidbeyondf_above + 1
                    if float(row['priceDaysBackMid']) < priceToBreachFarToMidf_FinishDown:
                        icountfartomidbeyondf_below = icountfartomidbeyondf_below + 1
                    #print('priceToBreachFarToMid',round(float(row['priceDaysBackMid']),2),'by',round(priceToBreachFarToMidf_FinishUp,2),round(priceToBreachFarToMidf_FinishDown,2))
                    
                    isbeyondmycumprobthresholdf_total = 0
                    if row['DrawUpPctChange'] > pdeltapct_atthreshold_calloption:
                        isbeyondmycumprobthresholdf_total = 1
                        breachedmycumprobthresholdf_up = breachedmycumprobthresholdf_up + 1
                    if row['DrawDownPctChange'] > abs(pdeltapct_atthreshold_putoption):
                        isbeyondmycumprobthresholdf_total = 1
                        breachedmycumprobthresholdf_down = breachedmycumprobthresholdf_down + 1
                    if isbeyondmycumprobthresholdf_total != 0:
                        breachedmycumprobthresholdf_total = breachedmycumprobthresholdf_total + 1
                        #df_stockpricechanges['breachedaboveorbelow'][str(index.date())] = 'breached mycumprobthreshold (' + str(mycumprobthreshold) + '%) ' + str(pdeltapct_atthreshold_calloption) +  ' ' + str(pdeltapct_atthreshold_putoption) + ' ' + str(isbeyondmycumprobthresholdf_total) #breachedaboveorbelow
                    df_stockpricechanges['breachedaboveorbelow'][str(index.date())] = isbeyondmycumprobthresholdf_total
                
                df_stockpricechanges['pdeltapct_atthreshold_calloption'] = pdeltapct_atthreshold_calloption
                df_stockpricechanges['pdeltapct_atthreshold_putoption'] = pdeltapct_atthreshold_putoption
                
                '''
                /////////////////////////////////////////////////////////////////////////////////////////
                                        SourceData CSV
                /////////////////////////////////////////////////////////////////////////////////////////
                '''
                print('Len of df_stockpricechanges',len(df_stockpricechanges))
                df_stockpricechanges.to_csv(sourcedatafolderwithsymbol + "\\ironcondor sourcedata (" + expirationdate_string + ') '+ symbol +  " " + datestringforfilename + ".csv",columns=('dateDaysBackMid','dateDaysBackFar','priceRefDate','priceDaysBackMid','priceDaysBackFar','DeltaFartoMid','DrawDownMax','DrawUpMax','DrawDownPctChange','DrawUpPctChange','comppratfar','pdeltapct_atthreshold_calloption','pdeltapct_atthreshold_putoption','breachedaboveorbelow'))
                
                                            # ==========
                                            #print(df_cumprobsbystrikeranges)
                                            # ==========
                print('================= ok got here dummy#2345245 ==================')
                # ####################################################
                # Here is where we find the value of the credit spread
                #      still need to build the Put credit spread
                candidaterows = []
                
                
                '''@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                                Candidate Header Row
                   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'''
                candidateheader = ['openshortoptsym','openlongoptsym','ty','stkp','spdel','sstrk','bstrk','scump','bcump','sbid','bask','capt','myexdate','currdate','daysbackmid','pricecompare','obsv','siv','sel']
                candidaterows.append(candidateheader)
                
                lastmycompareprice = df_comparestockpricehistory['Adj Close'][len(df_comparestockpricehistory)-1]
                
                #print df_cumprobsbystrikeranges
                crossedthresholdf_call = 0
                crossedthresholdf_put = 0
                sum_of_iter_capt_at_cumprob_cross = float(0)
                previousrow = None
                for index,row in df_cumprobsbystrikeranges.iterrows():
                    sel = ''
                    
                    if float(row['iscandidate']) == 1:
                        openshortoptsym = row['optionsymbol']
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
                        siv = row['iv']
                        row_inner_found = []
                        openlongoptsym = ''
                        iter_scump = float(row['cumprob_to_sell_price'].replace('%',''))
                        if row['ty'] == 'C' and crossedthresholdf_call == 0 and iter_scump >= mycumprobthreshold:
                            crossedthresholdf_call = 1
                            sel = 'x'
                            #print '&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'
                        if row['ty'] == 'P' and crossedthresholdf_put == 0 and iter_scump <= mycumprobthreshold:
                            crossedthresholdf_put = 1
                            prevcandidaterow = candidaterows[len(candidaterows)-1]
                            a_indices = [i for i, x in enumerate(candidaterows[0]) if x == 'sel']
                            prevcandidaterow[a_indices[0]] = 'x'    
                
                            #print 'tttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt'
                            #print prevcandidaterow
                            
                        if row['ty'] == 'C':         
                            for index_inner,row_inner in df_cumprobsbystrikeranges.iterrows():
                                if row_inner['ty'] == row['ty']:
                                    if float(row_inner['strike_at_sell_price']) == float(row['strike_at_sell_price'])+myspreadindollars:
                                        row_inner_found = row_inner
                                        buyaskprice = row_inner['ask']
                                        #buystrike = row_inner['strike_at_sell_price']
                                        buystrike = mytools.get_from_optionsymbol().strike(row_inner['optionsymbol'])
                                        openlongoptsym = row_inner['optionsymbol']
                                        #print('CALL >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                                        
                        if row['ty'] == 'P':
                            for index_inner,row_inner in df_cumprobsbystrikeranges.iterrows():
                                if row_inner['ty'] == row['ty']:
                                    if float(row_inner['strike_at_sell_price']) == float(row['strike_at_sell_price'])-myspreadindollars:
                                        row_inner_found = row_inner
                                        buyaskprice = row_inner['ask']
                                        #buystrike = row_inner['strike_at_sell_price']
                                        buystrike = mytools.get_from_optionsymbol().strike(row_inner['optionsymbol'])
                                        openlongoptsym = row_inner['optionsymbol']
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
                        if len(openshortoptsym) > 0 and len(openlongoptsym) > 0:
                            candidaterows.append([openshortoptsym,openlongoptsym,myoptiontype,sellstockprice,pdeltapct_to_sell_price,sellstrike,buystrike,sellcumprob,buycumprob,sellbidprice,buyaskprice,round(float(sellbidprice)-float(buyaskprice),3),myexdate.strftime('%Y-%m-%d'),datestringforcsv,daysbackmid,compare_stock_price,number_of_observations,siv,sel])
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
                
                print('================= ok got here dummy#42231 ==================')
                headers = candidaterows.pop(0)
                # This might not work - 9999999999999999
                
                print('len(candidaterows)',len(candidaterows))
                if len(candidaterows) > 1:
                    if len(candidaterows[1]) > 0:
                        print('jkjkjkjkjkjkj candidaterows.count',len(candidaterows[1]))
                        df_candidates = pd.DataFrame(candidaterows,columns=headers)
                
                        '''@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                                        Candidate Value CSV
                           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'''
                        df_candidates.to_csv(candidatesfolderwithsymbol + "\\ironcondor candidates (" + expirationdate_string + ') ' + symbol +  " " + datestringforfilename + ".csv",columns=('openshortoptsym','openlongoptsym','ty','stkp','spdel','sstrk','bstrk','scump','bcump','sbid','bask','capt','myexdate','currdate','daysbackmid','pricecompare','obsv','siv','sel'))
                        
                        # #################################################
                        # Use Dictionary Comprehension to get selected rows
                        selectedcandidaterows = []
                        list_selectedcandidaterows_1 = []
                        list_selectedcandidaterows_1.append(candidateheader)
                        
                        
                        #dict_selectedcandidaterows = { k:r for k,r in df_candidates.iterrows() if r['sel'] == 'x'}
                        #list_selectedcandidaterows_2 = [ r for k,r in df_candidates.items() if r['sel'] == 'x']
                        #print('777777777777777777777')
                        #print(list_selectedcandidaterows_2)
                        #selectedcandidaterows = list_selectedcandidaterows_2.extend(list_selectedcandidaterows_1)
                        
                        
                        
                        # ################################
                        # The above is equivalent to below
                        for k,candidaterow in df_candidates.iterrows():
                            if candidaterow['sel'] == 'x':
                                list_selectedcandidaterows_1.append(candidaterow)
                                print('!! !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                                print('!! Found a selected strike from candidate list')
                        headers = list_selectedcandidaterows_1.pop(0)
                        df_selectedcandidates = pd.DataFrame(list_selectedcandidaterows_1,columns=headers)
                        #print('2 ##########################################')
                        #print(df_selectedcandidates)
                        
                        
                        #print('1 ##########################################')
                        #print(list_selectedcandidaterows)
                        #print('Try dict',type(list_selectedcandidaterows) is dict)
                        #print(list(list_selectedcandidaterows.items()))
                        #print('2 ##########################################')
                        
                        filepath_to_selectedcandidates = os.path.join(myselectedcandidatesfolder,symbol,'selectedcandidates ' + expirationdate_string + ' ' + symbol + '.csv')
                        mygeneral.make_sure_path_exists(path_base(filepath_to_selectedcandidates)) #sourcedatafolderwithsymbol
                        #import os
                        
                        #Python 2-3 differences
                        #df_selectedcandidaterows = pd.DataFrame(df_selectedcandidates, columns=['ty','stkp','spdel','sstrk','bstrk','scump','bcump','sbid','bask','capt','myexdate','currdate','daysbackmid','pricecompare','obsv','sel'])
                        #print(df_selectedcandidaterows)
                        #df_selectedcandidaterows = pd.DataFrame(list_selectedcandidaterows.items(), columns=['ty','stkp','spdel','sstrk','bstrk','scump','bcump','sbid','bask','capt','myexdate','currdate','daysbackmid','pricecompare','obsv','sel'])
                        
                        #print('3 ##########################################')
                        '''@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                                        Selected Candidates CSV
                           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'''
                        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                        print('>> here are the current contents of the df_selectedcandidates dataframe')
                        print(df_selectedcandidates)
                        if os.path.isfile(filepath_to_selectedcandidates) != True:
                            df_selectedcandidates.to_csv(filepath_to_selectedcandidates,columns=('openshortoptsym','openlongoptsym','ty','stkp','spdel','sstrk','bstrk','scump','bcump','sbid','bask','capt','myexdate','currdate','daysbackmid','pricecompare','obsv','siv','sel'))
                            
                        elif len(df_selectedcandidates) > 0:
                            #df_fromcsv = pd.read_csv(filepath_to_selectedcandidates, index_col=0)
                            existingcsvfile = open(filepath_to_selectedcandidates, 'a') # Open file as append mode
                            df_selectedcandidates.to_csv(existingcsvfile, header = False)
                            existingcsvfile.close()
                        
                        
                        #print(df_candidates)
                        
                        crossedthresholdf_call = 0
                        crossedthresholdf_put = 0
                        capturedspreadf_at_call_thresholdf_cross = float('Nan')
                        capturedspreadf_at_put_thresholdf_cross = float('Nan')
                        sellstrike_at_call_thresholdf_cross = float('Nan')
                        sellstrike_at_put_thresholdf_cross = float('Nan')
                        
                        previousrow = None
                        for index,row in df_candidates.iterrows():
                            iter_scump = float(row['scump'].replace('%',''))
                            if row['ty'] == 'C' and crossedthresholdf_call == 0 and iter_scump >= mycumprobthreshold:
                                crossedthresholdf_call = 1
                                capturedspreadf_at_call_thresholdf_cross = float(row['capt'])
                                sellstrike_at_call_thresholdf_cross = float(row['sstrk'])
                            if row['ty'] == 'P' and crossedthresholdf_put == 0 and iter_scump <= mycumprobthreshold:
                                crossedthresholdf_put = 1
                                if previousrow != None:
                                    capturedspreadf_at_put_thresholdf_cross = float(previousrow['capt'])
                                    sellstrike_at_put_thresholdf_cross = float(previousrow['sstrk'])
                                # previousrow need only to be done for put side
                                previousrow = row
                            #print('scump=',iter_scump)
                        
                        print('-- ------------------------------------------')
                        print('-- here are some result written out')
                        print('Symbol:',symbol)
                        print('  Current stock price:',round(stockprice,2))
                        print('  Today:',today_date)
                        print('  Expire Date:',expire_date )
                        print('  Number of Days to Expiration:',delta.days)
                        print('  Price changes start date:',startdatecalculatedf_string)
                        print('  Number Of Observations Found',number_of_observations)
                        print('  Price delta % for strike to meet',str(mycumprobthreshold)+'%','cumprob threshold (Call):','{percent:.2%}'.format(percent=pdeltapct_atthreshold_calloption))
                        print('  Price delta % for strike to meet',str(mycumprobthreshold)+'%','cumprob threshold (Put):','{percent:.2%}'.format(percent=pdeltapct_atthreshold_putoption))
                        
                        
                        print('DRAW UP & DOWN ---- What happened during')
                        print('    Breaches at',mycumprobthreshold,'% cumulative prob threshold (Far to Mid)')
                        
                        print('    Count of Draw UP breaches:  ',breachedmycumprobthresholdf_up)
                        print('    Count of Draw DOWN breaches:',breachedmycumprobthresholdf_down)
                        print('    Count of Draw TOTAL breaches:  ',breachedmycumprobthresholdf_total,'of',number_of_observations)
                        print('    Prcnt of Draw TOTAL breaches:  ','{percent:.2%}'.format(percent=(breachedmycumprobthresholdf_total)/float(number_of_observations)))
                        print('FINISH ---- What happened during')
                        print('    Count finishes.... Above price set by cumprob threshold=',icountfartomidbeyondf_above)
                        print('    Count finishes.... Below price set by cumprob threshold=',icountfartomidbeyondf_below)
                        print('    Count finishes.... Above or below price set by cumprob =',icountfartomidbeyondf_above+icountfartomidbeyondf_below,'of',number_of_observations)
                        print('    Prcnt finishes.... Above or below price set by cumprob =','{percent:.2%}'.format(percent=(icountfartomidbeyondf_above+icountfartomidbeyondf_below)/float(number_of_observations)))
                        
                        print('Condor Specs--------')
                        print('    sellstrike_at_call_thresholdf_cross=',round(sellstrike_at_call_thresholdf_cross,2))
                        print('    sellstrike_at_put_thresholdf_cross=',round(sellstrike_at_put_thresholdf_cross,2))
                        print('    Capture at Call threshold:',capturedspreadf_at_call_thresholdf_cross)
                        print('    Capture at Put threshold:',capturedspreadf_at_put_thresholdf_cross)
                        print('    Capture Total Amt=',round(capturedspreadf_at_call_thresholdf_cross+capturedspreadf_at_put_thresholdf_cross,2))
                        print('    sum_of_iter_capt_at_cumprob_cross',sum_of_iter_capt_at_cumprob_cross)
                        print('  Note: candidates occur where stock price does not close at levels set by cumprob sell price, meaning your condor was a success')
                        print('  ',mycomparesym+':',round(compare_stock_price,2))
                        print('-----------------')
                        #for k,v in df_candidates.items():
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
                                df_optionpricescurrent = pd.DataFrame(rows, columns=headers)
                                #import numpy as np
                                df_optionpricescurrent['stockprice'] = stockprice
                        '''