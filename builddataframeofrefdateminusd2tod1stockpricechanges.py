# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 05:35:22 2015

@author: jmalinchak
"""

class perform:
    
    def __init__(self,
                 symbol = 'AAPL' ,
                 param_numberofweeks = 300,
                 daysbackmid = 17,
                 daysbackfar = 32,
                 showresults=0):
        print('Initialized class builddataframeofrefdateminusd2tod1stockpricechanges')
        if showresults == 1:
            print('showresults=' + str(showresults) + ' builddataframeofrefdateminusd2tod1stockpricechanges')
        
        self.build(symbol,param_numberofweeks,daysbackmid,daysbackfar,showresults)
    
#    def set_DataFrameResult(self,DataFrameResult):
#        self._DataFrameResult = DataFrameResult
#    def get_DataFrameResult(self):
#        return self._DataFrameResult
#    DataFrameResult = property(get_DataFrameResult, set_DataFrameResult)   

    #DataFrameResult
    def set_DataFrameResult(self,DataFrameResult):
        self._DataFrameResult = DataFrameResult
    def get_DataFrameResult(self):
        return self._DataFrameResult
    DataFrameResult = property(get_DataFrameResult, set_DataFrameResult)


    def build(self,
                     symbol,
                     param_numberofweeks ,
                     daysbackmid ,
                     daysbackfar ,
                     showresults
                 ):


        import pandas as pd
        import numpy as np
        
        if showresults == 1:
            print('mysymbol',symbol,'------------------------------------')        
        
        #param_numberofweeks = 4
        numberofweekstorun = param_numberofweeks
        
        from datetime import datetime, timedelta
        dStart = datetime.now().date() + timedelta(weeks = -numberofweekstorun)
        #print(dStart)
        
        index = pd.date_range(dStart+timedelta(days = 0), periods=numberofweekstorun, freq='W-Fri')
        #print(index)
        columns = ['dateDaysBackMid','dateDaysBackFar','priceRefDate','priceDaysBackMid','priceDaysBackFar','DeltaFartoMid','DrawDownMax','DrawUpMax','DrawDownPctChange','DrawUpPctChange']
        df_ = pd.DataFrame(index=index, columns=columns)
        df_ = df_.fillna(0) # with 0s rather than NaNs
        #df_ = df_.fillna(method='pad')
        
        
        # ------------------------------------------------------------
        # Change this number after * if changing the number of columns
        data = np.array([np.arange(len(index))]*10).T
        # ------------------------------------------------------------
        
        
        df = pd.DataFrame(data, index=index, columns=columns)
        #-------------------------------------------------------------------------------
        

        
        import pullprices
        fmt = '%Y-%m-%d'
        
        dEnd = index[-1]
        dEnd_string = dEnd.strftime(fmt)
        
        dDataStart = dStart+timedelta(days = (-1 * daysbackfar) - 1)
        dDataStart_string = dDataStart.strftime(fmt)
        #f = pullprices.stockhistory(symbol, dDataStart, dEnd)
        df_backfilled = pullprices.stockhistorybackfilledtodatframeofstockhistoryinstancesusingcache(symbol, dDataStart_string, dEnd_string)
        #df_backfilled_nonan = df_backfilled.dropna(subset=['Open'])
        #print(f)
        for idx, row in df.iterrows():
            pDraw_downmax = 0
            pDraw_upmax = 0
            #print(idx)
            dRef = idx
            ddaysbackmid = dRef + timedelta(days = -1 * daysbackmid)
            ddaysbackfar = dRef + timedelta(days = -1 * daysbackfar)
        
            dRef_string = dRef.strftime(fmt)
            ddaysbackmid_string = ddaysbackmid.strftime(fmt)
            ddaysbackfar_string = ddaysbackfar.strftime(fmt)
            
        
            try:
                pdaysbackfar = df_backfilled.ix[ddaysbackfar_string]['Adj Close']
                #print(ddaysbackfar_string,pdaysbackfar)
                
            except: 
                pdaysbackfar = float('NaN')
                #print('no data')
                pass
            try:
                pdaysbackmid = df_backfilled.ix[ddaysbackmid_string]['Adj Close']
                #print(ddaysbackmid_string,pdaysbackmid)
            except: 
                pdaysbackmid = float('NaN')
                #print('no data')
                pass
            try:
                pRef = df_backfilled.ix[dRef_string]['Adj Close']
                #print(dRef_string,pRef)
            except:
                pRef = float('NaN')
                #print('no data')
                pass
            try:
                pdeltadaysbackfartodaysbackmid = pdaysbackmid - pdaysbackfar
                #print('pricedelta',pdeltadaysbackfartodaysbackmid)
            except:
                pdeltadaysbackfartodaysbackmid = float('NaN')
                #print('no delta')
        
            for iday in range(1, daysbackfar - daysbackmid + 1):
                dDraw = ddaysbackfar + timedelta(days = iday)
                dDraw_string = dDraw.strftime(fmt)
                #print(dDraw_string)
                try:
                    pDraw = df_backfilled.ix[dDraw_string]['Adj Close'] 
                                    
                    pDelta = pDraw - pdaysbackfar
                        
                    if pDelta < pDraw_downmax:
                        pDraw_downmax = pDelta
                    if pDelta > pDraw_upmax:
                        pDraw_upmax = pDelta
                    if pdaysbackfar == float('NaN'):
                        pDraw_downmax = float('NaN')
                        pDraw_upmax = float('NaN')
                except:
                    pDraw = float('Nan')
            #print(dRef_string,ddaysbackmid_string,ddaysbackfar_string)
            #print('inside builddataframeofrefdateminusd2tod1stockpricechanges.py','WAWAWAWAWAW pDraw_downmax,pdaysbackfar',pDraw_downmax,pdaysbackfar)
            
            try:
                pctchangeDraw_downmax = pDraw_downmax / pdaysbackfar
            except:
                pctchangeDraw_downmax = float('NaN')

            try:                
                pctchangeDraw_upmax = pDraw_upmax / pdaysbackfar 
            except:
                pctchangeDraw_upmax = float('NaN')
                
            df.loc[dRef] = pd.Series({'dateDaysBackMid':ddaysbackmid.strftime('%Y-%m-%d')
                                        ,'dateDaysBackFar':ddaysbackfar.strftime('%Y-%m-%d')
                                        ,'priceRefDate':pRef
                                        ,'priceDaysBackMid':pdaysbackmid
                                        ,'priceDaysBackFar':pdaysbackfar
                                        ,'DeltaFartoMid':pdeltadaysbackfartodaysbackmid
                                        ,'DrawDownMax':pDraw_downmax
                                        ,'DrawUpMax':pDraw_upmax
                                        ,'DrawDownPctChange':abs(pctchangeDraw_downmax)
                                        ,'DrawUpPctChange':pctchangeDraw_upmax})
            #print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        
        #df = df.fillna(method='pad')
        
        if showresults == 1:
            print(df)    
            print(len(data))
            print(len(df))
            
            print('------------------------')
            print(dStart)
            print(dEnd)
            print('dRef',dRef)
        self.DataFrameResult = df
       
#        self.DictionaryOfSerializedQuadCandidateXMLPathNames = dSerializedQuadCandidateXMLPathNames
                                             