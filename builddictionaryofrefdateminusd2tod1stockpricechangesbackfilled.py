# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 05:35:22 2015

@author: jmalinchak
"""

class perform:
    
    def __init__(self,
                 symbol = 'AAPL' ,
                 param_numberofyears = 4 ,
                 showresults=0):
        print('initialized class builddictionaryofrefdateminusd2tod1stockpricechangesbackfilled.py')
        if showresults == 1:
            print('showresults=' + str(showresults) + ' builddictionaryofrefdateminusd2tod1stockpricechangesbackfilled.py')
        
        self.build(symbol,param_numberofyears,showresults)
    
#    def set_DataFrameResult(self,DataFrameResult):
#        self._DataFrameResult = DataFrameResult
#    def get_DataFrameResult(self):
#        return self._DataFrameResult
#    DataFrameResult = property(get_DataFrameResult, set_DataFrameResult)   

#
#
#
#
#


    def set_DictionaryResult(self,DictionaryResult):
        self._DictionaryResult = DictionaryResult
    def get_DictionaryResult(self):
        return self._DictionaryResult
    DictionaryResult = property(get_DictionaryResult, set_DictionaryResult)

    def build(self,
                     symbol,
                     param_numberofyears ,
                     showresults
                 ):


        import pandas as pd
        #import numpy as np
        
        print('------------------------------------')
        print('mysymbol',symbol)        
        
        #param_numberofyears = 4
        numberofweekstorun = param_numberofyears * 52
        
        from datetime import datetime, timedelta
        dStart = datetime.now().date() + timedelta(weeks = -numberofweekstorun)
        #print(dStart)
        
        index = pd.date_range(dStart+timedelta(days = 0), periods=numberofweekstorun, freq='W-Fri')
        #print(index)
        #columns = ['d1','d2','pRef','p1','p2','Delta2to1','DrawDownMax','DrawUpMax','DrawDownPctChange','DrawUpPctChange']
        #df_ = pd.DataFrame(index=index, columns=columns)
        #df_ = df_.fillna(0) # with 0s rather than NaNs
        #df_ = df_.fillna(method='pad')
        
        
        # ------------------------------------------------------------
        # Change this number after * if changing the number of columns
        #data = np.array([np.arange(len(index))]*10).T
        # ------------------------------------------------------------
        
        
        #df = pd.DataFrame(data, index=index, columns=columns)
        #-------------------------------------------------------------------------------
        
        dEnd = index[-1]
        
        
        import pullprices
        fmt = '%Y-%m-%d'
        
        dDataStart = dStart+timedelta(days = -33)
        
        #import pullprices as pp
        #df = pp.stockhistory('AAPL','2014-01-01','2015-05-15')
        #mydict1 = pp.stockhistorybackfilledtodictionary('AAPL','2015-01-01','2015-05-15')
        #print('mypick',mydict1['2015-05-09']('AdjClose'))

        date_format = "%Y-%m-%d"

        dDataStart_string = dDataStart.strftime(date_format)
        
        dEnd_string = dEnd.strftime(date_format) #datetime.strptime(dEnd, date_format)

        mydict2 = pullprices.stockhistorybackfilledtodictionaryofstockhistoryinstances(symbol,dDataStart_string,dEnd_string)
        #print(mydict2)
        #from collections import OrderedDict
        #dOrdered = OrderedDict(sorted(mydict2.items(), key=lambda t: t[1]['sortbymeasurevalue']))
        #dOrdered = OrderedDict(sorted(mydict2.items()))

        #f=pullprices.stockhistory(symbol, dDataStart, dEnd)

        import calendar        
        dResult = {}        
        import structureford2tod1stockpricechangeinstance
        
        for dKey, dValue in mydict2.items():
             
            dayoftheweek = calendar.day_name[datetime.strptime(dKey, date_format).weekday()]
            
            if dayoftheweek == 'Friday':
                struct = structureford2tod1stockpricechangeinstance.Framework(self)
                
                
                struct.dateref = datetime.strptime(dKey, date_format) # dRef = datetime.strptime(idx, date_format)
                struct.pricedrawdownmax = 0 # pDraw_downmax = 0
                struct.pricedrawupmax = 0 # pDraw_upmax = 0
                #print(idx)
                               
                struct.datemidback = struct.dateref + timedelta(days = -17)
                struct.datemaxback = struct.dateref + timedelta(days = -32)
            
                dRef_string = struct.dateref.strftime(fmt)
                d17_string = struct.datemidback.strftime(fmt)
                d32_string = struct.datemaxback.strftime(fmt)
                
            
                try:
                    struct.pricemaxback= mydict2[d32_string].adjclose
                    #print(d32_string,struct.pricemaxback)
                    
                except: 
                    struct.pricemaxback = float('NaN')
                    #print('no data')
                    pass
                try:
                    struct.pricemidback = mydict2[d17_string].adjclose
                    #struct.pricemidback = f.ix[d17_string]['Adj Close']
                    #print(d17_string,struct.pricemidback)
                except: 
                    struct.pricemidback = float('NaN')
                    #print('no data')
                    pass
                print('ref adj close',mydict2[dRef_string].adjclose)
                try:
                    struct.priceref = mydict2[dRef_string].adjclose
                    #pRef = f.ix[dRef_string]['Adj Close']
                    #print(dRef_string,pRef)
                except:
                    struct.priceref = float('NaN')
                    #print('no data')
                    pass
                try:
                    struct.pricedeltamaxdatebacktomiddateback = struct.pricemidback - struct.pricemaxback
                    #print('pricedelta',pdelta32to17)
                except:
                    struct.pricedeltamaxdatebacktomiddateback = float('NaN')
                    #print('no delta')
            
                for iday in range(1, 32 - 17 + 1):
                    dDraw = struct.datemaxback + timedelta(days = iday)
                    dDraw_string = dDraw.strftime(fmt)
                    #print(dDraw_string)
                    try:
                        pDraw = mydict2[dDraw_string].adjclose
                        #pDraw = f.ix[dDraw_string]['Adj Close'] 
                                        
                        pDelta = pDraw - struct.pricemaxback
                            
                        if pDelta < struct.pricedrawdownmax:
                            struct.pricedrawdownmax = pDelta
                        if pDelta > struct.pricedrawupmax:
                            struct.pricedrawupmax = pDelta
                        if struct.pricemaxback == float('NaN'):
                            struct.pricedrawdownmax = float('NaN')
                            struct.pricedrawupmax = float('NaN')
                    except:
                        pDraw = float('Nan')
                #print(dRef_string,d17_string,d32_string)
                struct.percentpricedrawdownmax = struct.pricedrawdownmax / struct.pricemaxback
                struct.percentpricedrawupmax = struct.pricedrawupmax / struct.pricemaxback 
                #print(struct.dateref)
                dResult[len(dResult)] = struct
                # print(struct.dateref)
#                for k,v in dResult.items():
#                    print(k,v.dateref)
                
        print('datebegin',dDataStart_string)
        print('dateend',dEnd_string)
        print('Number of records',len(dResult))
        print('------------------------')
        self.DictionaryResult = dResult
       
#        self.DictionaryOfSerializedQuadCandidateXMLPathNames = dSerializedQuadCandidateXMLPathNames
                                             