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
        print('initialized class readintomemorybuilddictionaryofpairsdictionariesbysymbol')
        if showresults == 1:
            print('showresults=' + str(showresults) + ' readintomemorybuilddictionaryofpairsdictionariesbysymbol')
        
        self.build(symbol,param_numberofyears,showresults)
    
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
                     param_numberofyears ,
                     showresults
                 ):


        import pandas as pd
        import numpy as np
        
        print('mysymbol',symbol,'------------------------------------')        
        
        #param_numberofyears = 4
        numberofweekstorun = param_numberofyears * 52
        
        from datetime import datetime, timedelta
        dStart = datetime.now().date() + timedelta(weeks = -numberofweekstorun)
        #print(dStart)
        
        index = pd.date_range(dStart+timedelta(days = 0), periods=numberofweekstorun, freq='W-Fri')
        #print(index)
        columns = ['d1','d2','pRef','p1','p2','Delta2to1','DrawDownMax','DrawUpMax','DrawDownPctChange','DrawUpPctChange']
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
        
        dDataStart = dStart+timedelta(days = -33)
        dDataStart_string = dDataStart.strftime(fmt)
        #f = pullprices.stockhistory(symbol, dDataStart, dEnd)
        f = pullprices.stockhistorybackfilledtodatframeofstockhistoryinstances(symbol, dDataStart_string, dEnd_string)
        print(f)
        for idx, row in df.iterrows():
            pDraw_downmax = 0
            pDraw_upmax = 0
            #print(idx)
            dRef = idx
            d17 = dRef + timedelta(days = -17)
            d32 = dRef + timedelta(days = -32)
        
            dRef_string = dRef.strftime(fmt)
            d17_string = d17.strftime(fmt)
            d32_string = d32.strftime(fmt)
            
        
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
        
            for iday in range(1, 32 - 17 + 1):
                dDraw = d32 + timedelta(days = iday)
                dDraw_string = dDraw.strftime(fmt)
                #print(dDraw_string)
                try:
                    pDraw = f.ix[dDraw_string]['Adj Close'] 
                                    
                    pDelta = pDraw - p32
                        
                    if pDelta < pDraw_downmax:
                        pDraw_downmax = pDelta
                    if pDelta > pDraw_upmax:
                        pDraw_upmax = pDelta
                    if p32 == float('NaN'):
                        pDraw_downmax = float('NaN')
                        pDraw_upmax = float('NaN')
                except:
                    pDraw = float('Nan')
            #print(dRef_string,d17_string,d32_string)
            pctchangeDraw_downmax = pDraw_downmax / p32
            pctchangeDraw_upmax = pDraw_upmax / p32 
            df.loc[dRef] = pd.Series({'d1':d17.strftime('%Y-%m-%d'),'d2':d32.strftime('%Y-%m-%d'), 'pRef':pRef, 'p1':p17,'p2':p32,'Delta2to1':pdelta32to17,'DrawDownMax':pDraw_downmax,'DrawUpMax':pDraw_upmax,'DrawDownPctChange':pctchangeDraw_downmax,'DrawUpPctChange':pctchangeDraw_upmax})
            #print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        
        #df = df.fillna(method='pad')
        
        print(df)    
        print(len(data))
        print(len(df))
        
        print('------------------------')
        print(dStart)
        print(dEnd)
        print('dRef',dRef)
        self.DataFrameResult = df
       
#        self.DictionaryOfSerializedQuadCandidateXMLPathNames = dSerializedQuadCandidateXMLPathNames
                                             