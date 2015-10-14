# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 00:17:18 2014

@author: jmalinchak
"""


def make_sure_filepath_exists(filepath):
    import errno
    import os
    try:
        path = os.path.dirname(os.path.abspath(filepath))
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
########################################################################
#test_downloadpath='C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\downloads\\test'
test_downloadpath='C:\\Documents and Settings\\jmalinchak\My Documents\\My Python\\Active\\downloads\\2014-12-07\\01\\60'
#test_downloadpath='C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\downloads\\2014-12-07\\01\\30'
pathfilelocaloutput='C:\Documents and Settings\jmalinchak\My Documents\My Python\Active\output\\output_readintomemoryinsertcalendarspreadpairsintodictionary.csv'
showresults = 0
########################################################################
import readintomemoryinsertcalendarspreadpairsintodictionary
print('running readintomemoryinsertcalendarspreadpairsintodictionary...')

cal = readintomemoryinsertcalendarspreadpairsintodictionary.read(test_downloadpath,showresults)
#if showresults == 1:
print('completed readintomemoryinsertcalendarspreadpairsintodictionary')

dPairs  = cal.PairsDictionary

dPairsCalculated = {}

switch = 0

#if showresults == 1:
print('building valid pairs...')
    
for k,ls in dPairs.items():
    earlier = ls[0]
    later = ls[1]
    if float(earlier.bid) > 0.20:
        if float(earlier.bid) < 3.50:
            if (earlier.optiontype == 'C' and float(earlier.stockprice) < float(earlier.strike)) or (earlier.optiontype == 'P' and float(earlier.stockprice) > float(earlier.strike)): 
                if float(later.ask) > 0.0 and float(earlier.bid)/float(later.ask) > 0.8:
                    dPairsCalculated[k] = float(earlier.bid)/float(later.ask)
                    if showresults == 1:
                        print(str(len(dPairsCalculated)) + ' valid pairs...')
#            if earlier.optiontype == 'C' and float(earlier.stockprice) < float(earlier.strike):
#                dPairsCalculated[k] = float(earlier.bid)/float(later.ask)                    
#            if earlier.optiontype == 'P' and float(earlier.stockprice) > float(earlier.strike):
#                dPairsCalculated[k] = float(earlier.bid)/float(later.ask)                
            
        #print(earlier.optionsymbol,later.optionsymbol, ' >>> ', earlier.bid, later.ask,float(earlier.bid)/float(later.ask)) #,((earlier.bid+earlier.ask)/2.00), ((later.bid+later.ask)/2.00), ((earlier.bid+earlier.ask)/2.00) - ((later.bid+later.ask)/2.00))
        
            #dPairsCalculated[k] = float(earlier.bid)/float(later.ask)

#from operator import itemgetter, attrgetter, methodcaller
#tPairsSorted = sorted(dPairsCalculated.items(),  key=itemgetter('ratio'))
#if showresults == 1:

print('sorting results...')
    
from collections import OrderedDict
dOrdered = OrderedDict(sorted(dPairsCalculated.items(), key=lambda t: t[1]))
outputlines = {}

#if showresults == 1:
print('putting results into printable dictionary ' + str(len(dOrdered)) + ' lines')
    
for k1,v1 in dOrdered.items():
    #ls = list(dPairs.keys())[list(dPairs.values()).index(k1)]
    ls = dPairs.get(k1)
    earlier = ls[0]
    later = ls[1]
    outputlines[len(outputlines)]=earlier.optionsymbol+','+later.optionsymbol+','+str(later.strike)+','+str(later.stockprice)+','+str(earlier.bid)+','+str(later.ask)+','+'{percent:.0%}'.format(percent=float(earlier.bid)/float(later.ask)) +','+ str(round(float(later.ask)-float(earlier.bid),2))
    #print(outputline)
    #print(earlier.optionsymbol,later.optionsymbol,'<strike>'+later.strike+'<\strike>','<stockprice>'+later.stockprice+'<\stockprice>',' > ',earlier.bid,later.ask,' >>> ','{percent:.0%}'.format(percent=float(earlier.bid)/float(later.ask)))
make_sure_filepath_exists(pathfilelocaloutput)

#if showresults == 1:
print('printing results to ' + pathfilelocaloutput)
    
with open(pathfilelocaloutput, 'w') as f:
    for outputline in outputlines.values():
        f.write(outputline+'\n')
        

#if showresults == 1:
print('done')
    

