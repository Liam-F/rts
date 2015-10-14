# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 21:14:47 2015

@author: jmalinchak
"""

#import readintomemorybuilddictionaryofpairsdictionariesbysymbol        
import readintomemorybuildcondorpairsdictionariesbysymbol
import mytools
import time
o = readintomemorybuildcondorpairsdictionariesbysymbol.read('C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\\downloadsprocessed\\2015-05-01\\14\\45\\AAPL2',0)

dDictionaryOfPairsDictionariesBySymbol = o.DictionaryOfPairsDictionariesBySymbol        
#        dTestValueAndPairTupleSortableByPairSpreadPct = {}
#        dPairsValid = {}
dCalendarPairs = {}
dQualifiedPairsBasedOnAllCriteriaProvided = {}
bContinue = 1   
for kSymbol,vPairsDictionary in dDictionaryOfPairsDictionariesBySymbol.items():
    dPairs  = vPairsDictionary
    #if showresults == 1:
    print('-- ' + kSymbol + ' building valid pairs... ')
    bContinue == 1
    
    for k,ls in dPairs.items():
        short = ls[0]
        long = ls[1]
        strikespread = abs(float(long.strike) - float(short.strike))
        shortstrikeawayfromstockprice = round(abs(float(short.strike)-float(short.stockprice)),2)
        spreadshortlong = round(float(short.bid)-float(long.ask),2)
        exdate = short.expirationdate.strftime('%b%d')
        
        if strikespread <= 1:
            print(spreadshortlong,short.symbol, short.optiontype,shortstrikeawayfromstockprice,strikespread, 'shortbid:',short.bid, 'longask:',long.ask,exdate,short.stockprice)