# -*- coding: utf-8 -*-
"""
***************************************************
contains BucketQuoteDateTimeDerivedFromDirectory
***************************************************

Created on Sun Nov 23 00:17:18 2014

@author: jmalinchak
"""
class read:
    
    def __init__(self, directorylocal,showresults=0):
        print('initialized class readintomemorybuilddictionaryofpairsdictionariesbysymbol.py')
        self.insert_pairs_into_dictionary(directorylocal,showresults)

    
    def set_DictionaryOfSymbols(self,DictionaryOfSymbols):
        self._DictionaryOfSymbols = DictionaryOfSymbols
    def get_DictionaryOfSymbols(self):
        return self._DictionaryOfSymbols
    DictionaryOfSymbols = property(get_DictionaryOfSymbols, set_DictionaryOfSymbols)
    
#    def set_BucketQuoteDateTimeDerivedFromDirectory(self,BucketQuoteDateTimeDerivedFromDirectory):
#        self._BucketQuoteDateTimeDerivedFromDirectory = BucketQuoteDateTimeDerivedFromDirectory
#    def get_BucketQuoteDateTimeDerivedFromDirectory(self):
#        return self._BucketQuoteDateTimeDerivedFromDirectory
#    BucketQuoteDateTimeDerivedFromDirectory = property(get_BucketQuoteDateTimeDerivedFromDirectory, set_BucketQuoteDateTimeDerivedFromDirectory)
    
    def set_DictionaryOfPairsDictionariesBySymbol(self,DictionaryOfPairsDictionariesBySymbol):
        self._DictionaryOfPairsDictionariesBySymbol = DictionaryOfPairsDictionariesBySymbol
    def get_DictionaryOfPairsDictionariesBySymbol(self):
        return self._DictionaryOfPairsDictionariesBySymbol
    DictionaryOfPairsDictionariesBySymbol = property(get_DictionaryOfPairsDictionariesBySymbol, set_DictionaryOfPairsDictionariesBySymbol)
    
    
    def insert_pairs_into_dictionary(self, directorylocal,showresults):
        print('-------')
        print('     Building dictionary using non-matching strikes (slower)')
        print('-------')
        #import os
        import nameddictionary
        
        #nameddictionaryfiltered.nameddictionary.read('C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\Active\\downloads\\20141130b')
        nd = nameddictionary.read(directorylocal,showresults)
        
        print('*****************************')        
        print(directorylocal)   
#        from os.path import normpath, basename
#        finishedbuildingbucketquotedatetime = False
#        basepath = directorylocal
#        while not finishedbuildingbucketquotedatetime:
#            #... do something...
#            #mypath = 'C:/Documents and Settings/jmalinchak/My Documents/My Python/Active/py'
#            print(basename(normpath(basepath)))
#            basepath = os.path.dirname(basepath)
#            
#            finishedbuildingbucketquotedatetime = evaluate_end_condition()
        print('*****************************')
        
        if showresults==1:
            print('111111 readintomemorybuilddictionaryofpairsdictionariesbysymbol.py 111111')
        #from datetime import datetime
        
        symbols = nd.NamedDictionaries
        
                        
        dSymbols = {}
        
        dPairsBySymbol = {}
        for symbol in symbols:
            dSymbols[len(dSymbols)] = symbol
            dPairs = {}
            print(symbol + '= symbol found in readintomemorybuilddictionaryofpairsdictionariesbysymbol.py')
            for exdate0 in nd.NamedDictionaries[symbol]:
                #print(symbol,exdate0)
                for exdate1 in nd.NamedDictionaries[symbol]:
                    if exdate0 < exdate1:
                        #if showresults == 1:
                        print(symbol,exdate0,exdate1)
                        #print(nd.NamedDictionaries[symbol][exdate0])
                        for optiontype0 in nd.NamedDictionaries[symbol][exdate0]:
                            for optiontype1 in nd.NamedDictionaries[symbol][exdate1]:
                                if optiontype0==optiontype1:
                                    optiontype = optiontype0
                                    if showresults ==1:
                                        print(symbol,optiontype,exdate0,exdate1,'checking ' + str(len(nd.NamedDictionaries[symbol][exdate0][optiontype])) + ' vs. ' + str(len(nd.NamedDictionaries[symbol][exdate1][optiontype])) + ' strikes')
                                    for strike0 in nd.NamedDictionaries[symbol][exdate0][optiontype]:
                                        for strike1 in nd.NamedDictionaries[symbol][exdate1][optiontype]:
                                            #if strike0 >= strike1:
                                            if (optiontype == 'C' and float(strike0) >= float(strike1)) or (optiontype == 'P' and float(strike0) <= float(strike1)): 
#                                                if symbol == 'FB' and optiontype =='C':
#                                                    print(str(strike0),str(strike1))
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
            #########################################################################################################
            print('=================================')
            print(str(len(dPairs)) + ' pairs created on ' + symbol)
            print('=================================')
            dPairsBySymbol[symbol] = dPairs
        #########################################################################################################
        self.DictionaryOfPairsDictionariesBySymbol = dPairsBySymbol
        self.DictionaryOfSymbols = dSymbols
        print('completed readintomemorybuilddictionaryofpairsdictionariesbysymbol')
        
        
        
                                                                