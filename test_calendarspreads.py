# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 00:17:18 2014

@author: jmalinchak
"""

import readintomemoryinsertcalendarspreadpairsintodictionary

cal = readintomemoryinsertcalendarspreadpairsintodictionary.read('C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\downloads\\20141204\\1600test')
#cal = readintomemoryinsertcalendarspreadpairsintodictionary.read('C:\\Batches\\AutomationProjects\\My Python\\downloads\\20141204end')

dPairs  = cal.PairsDictionary

dPairsCalculated = {}

switch = 0

for k,ls in dPairs.items():
    earlier = ls[0]
    later = ls[1]
    if float(earlier.bid) > 0.50:
        if float(earlier.bid) < 3.50:
            if earlier.optiontype == 'C':
                if float(earlier.stockprice) < float(earlier.strike):
                    dPairsCalculated[k] = float(earlier.bid)/float(later.ask)                    
            if earlier.optiontype == 'P':
                if float(earlier.stockprice) > float(earlier.strike):
                    dPairsCalculated[k] = float(earlier.bid)/float(later.ask)                
            
        #print(earlier.optionsymbol,later.optionsymbol, ' >>> ', earlier.bid, later.ask,float(earlier.bid)/float(later.ask)) #,((earlier.bid+earlier.ask)/2.00), ((later.bid+later.ask)/2.00), ((earlier.bid+earlier.ask)/2.00) - ((later.bid+later.ask)/2.00))
        
            #dPairsCalculated[k] = float(earlier.bid)/float(later.ask)

#from operator import itemgetter, attrgetter, methodcaller
#tPairsSorted = sorted(dPairsCalculated.items(),  key=itemgetter('ratio'))
from collections import OrderedDict
dOrdered = OrderedDict(sorted(dPairsCalculated.items(), key=lambda t: t[1]))

for k1,v1 in dOrdered.items():
    #ls = list(dPairs.keys())[list(dPairs.values()).index(k1)]
    ls = dPairs.get(k1)
    earlier = ls[0]
    later = ls[1]
    print(earlier.optionsymbol,later.optionsymbol,later.strike,later.stockprice,' > ',earlier.bid,later.ask,' >>> ','{percent:.0%}'.format(percent=float(earlier.bid)/float(later.ask)))