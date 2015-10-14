# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 00:17:18 2014

@author: jmalinchak
"""
class read:
    
    def __init__(self, directorylocal,showresults=0):
        if showresults==1:
            print('0000000 readintomemoryinsertcalendarspreadpairsintodictionary.py 0000000')
        self.insert_pairs_into_dictionary(directorylocal,showresults)
        
        
    def set_PairsDictionary(self,PairsDictionary):
        self._PairsDictionary = PairsDictionary
    def get_PairsDictionary(self):
        return self._PairsDictionary
    PairsDictionary = property(get_PairsDictionary, set_PairsDictionary)
    
    def insert_pairs_into_dictionary(self, directorylocal,showresults):
        print('readintomemoryinsertcalendarspreadpairsintodictionary,showresults='+str(showresults))
        import nameddictionary
        
        #nameddictionaryfiltered.nameddictionary.read('C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\Active\\downloads\\20141130b')
        nd = nameddictionary.read(directorylocal,showresults)
        if showresults==1:
            print('111111 readintomemoryinsertcalendarspreadpairsintodictionary.py 111111')
        #from datetime import datetime
        
        dPairs = {}
        symbols = nd.NamedDictionaries
        for symbol in symbols:
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
                                            if strike0 == strike1:
                                                strike = strike0
                                                for bqd0 in nd.NamedDictionaries[symbol][exdate0][optiontype][strike]:
                                                    for bqd1 in nd.NamedDictionaries[symbol][exdate1][optiontype][strike]:
                                                        if bqd0 == bqd1:
                                                            exdate0s = exdate0.strftime('%Y-%m-%d')
                                                            exdate1s = exdate1.strftime('%Y-%m-%d')
                                                            bqds = bqd0.strftime('%Y-%m-%d %H:%M:%S')
                                                            #print(symbol,exdate0s,exdate1s,optiontype,strike,bqds)
                                                            
                                                            d0 =  nd.optioninstances(symbol,exdate0s,optiontype,strike,bqds)
                                                            d1 =  nd.optioninstances(symbol,exdate1s,optiontype,strike,bqds)
        
                                                            if len(d0) >= 1 and len(d1) >= 1:
                                                                earlieroption=d0[0]
                                                                lateroption=d1[0]
                                                                dPairs[len(dPairs)] = [earlieroption,lateroption]
#                                                                ls = dPairs[0]
#                                                                print(ls[0].optionsymbol)
        self.PairsDictionary = dPairs
                                                                