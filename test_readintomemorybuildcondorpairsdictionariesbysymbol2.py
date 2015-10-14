# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 21:14:47 2015

@author: jmalinchak
"""

 
#import readintomemorybuilddictionaryofpairsdictionariesbysymbol        
import readintomemorybuildcondorpairsdictionariesbysymbol
o = readintomemorybuildcondorpairsdictionariesbysymbol.read('C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\\downloads\\2015-04-24\\15\\45\\PG',1)

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
        earlier = ls[0]
        later = ls[1]
        print(earlier.optionsymbol,later.optionsymbol)