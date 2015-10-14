# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 00:17:18 2014

@author: jmalinchak
"""
class read:
    
    def __init__(self, directorylocal,showresults=0):
        if showresults==1:
            print('0000000 readintomemoryinsertcalendarspreadpairsintodictionarynonmatchingstrikes.py 0000000')
        self.insert_pairs_into_dictionary(directorylocal,showresults)
        
        
    def set_PairsDictionary(self,PairsDictionary):
        self._PairsDictionary = PairsDictionary
    def get_PairsDictionary(self):
        return self._PairsDictionary
    PairsDictionary = property(get_PairsDictionary, set_PairsDictionary)
    
    def insert_pairs_into_dictionary(self, directorylocal,showresults):
        print('readintomemoryinsertcalendarspreadpairsintodictionarynonmatchingstrikes,showresults='+str(showresults))
        import nameddictionary
        
        #nameddictionaryfiltered.nameddictionary.read('C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\Active\\downloads\\20141130b')
        nd = nameddictionary.read(directorylocal,showresults)
        if showresults==1:
            print('111111 readintomemoryinsertcalendarspreadpairsintodictionarynonmatchingstrikes.py 111111')
        #from datetime import datetime
        
        dPairs = {}
        symbols = nd.NamedDictionaries
        print('Building dictionary of valid calendar spread pairs using non-matchingstrikes (slower)')
        for symbol in symbols:
            print(symbol + ' - readintomemoryinsertcalendarspreadpairsintodictionarynonmatchingstrikes')
            for exdate0 in nd.NamedDictionaries[symbol]:
                #print(symbol,exdate0)
                for exdate1 in nd.NamedDictionaries[symbol]:
                    if exdate0 < exdate1:
                        #print(symbol,exdate0,exdate1)
                        #print(nd.NamedDictionaries[symbol][exdate0])
                        for optiontype0 in nd.NamedDictionaries[symbol][exdate0]:
                            for optiontype1 in nd.NamedDictionaries[symbol][exdate1]:
                                if optiontype0==optiontype1:
                                    optiontype = optiontype0
                                    for strike0 in nd.NamedDictionaries[symbol][exdate0][optiontype]:
                                        for strike1 in nd.NamedDictionaries[symbol][exdate1][optiontype]:
                                            #if strike0 >= strike1:
                                            if (optiontype == 'C' and float(strike0) >= float(strike1)) or (optiontype == 'P' and float(strike0) <= float(strike1)): 
                                                if symbol == 'FB' and optiontype =='C':
                                                    print(str(strike0),str(strike1))
                                                for bqd0 in nd.NamedDictionaries[symbol][exdate0][optiontype][strike0]:
                                                    for bqd1 in nd.NamedDictionaries[symbol][exdate1][optiontype][strike1]:
                                                        if bqd0 == bqd1:
                                                            exdate0s = exdate0.strftime('%Y-%m-%d')
                                                            exdate1s = exdate1.strftime('%Y-%m-%d')
                                                            bqds = bqd0.strftime('%Y-%m-%d %H:%M:%S')
                                                            #print(symbol,exdate0s,exdate1s,optiontype,strike,bqds)
                                                            
                                                            d0 =  nd.optioninstances(symbol,exdate0s,optiontype,strike0,bqds)
                                                            d1 =  nd.optioninstances(symbol,exdate1s,optiontype,strike1,bqds)
        
                                                            if len(d0) >= 1 and len(d1) >= 1:
                                                                earlieroption=d0[0]
                                                                lateroption=d1[0]
                                                                dPairs[len(dPairs)] = [earlieroption,lateroption]
#                                                                ls = dPairs[0]
#                                                                print(ls[0].optionsymbol)
        self.PairsDictionary = dPairs
                                                                