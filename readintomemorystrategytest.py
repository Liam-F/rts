# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 11:35:00 2014

@author: jmalinchak
"""
class read:
    def __init__(self,
             pathfilelocalsymbols='inputs\\SymbolsTest.txt',
             pathfilelocalexpirations='inputs\\ExpirationsTest.txt',
             rootlocalforfilespulled='downloads\\2014-12-21\\11\\30',
             directorylocaloutput='output',
             showresults=1):
        self.execute_results(pathfilelocalsymbols,pathfilelocalexpirations,rootlocalforfilespulled,directorylocaloutput,showresults)

    def set_OutputFilePathString(self,OutputFilePathString):
        self._OutputFilePathString = OutputFilePathString
    def get_OutputFilePathString(self):
        return self._OutputFilePathString
    OutputFilePathString = property(get_OutputFilePathString, set_OutputFilePathString)    
    
    def execute_results(self,pathfilelocalsymbols,pathfilelocalexpirations,rootlocalforfilespulled,directorylocaloutput,showresults):
        import mytools
        downloaddirectorylocal = rootlocalforfilespulled #mytools.mystrings.appendnormaldateddirectorybasedoncurrenttime15(rootlocalforfilespulled)
        print('downloaddirectorylocal=' + downloaddirectorylocal)
        
        import readintomemorybuilddictionaryofpairsdictionariesbysymbol        
        o = readintomemorybuilddictionaryofpairsdictionariesbysymbol.read(downloaddirectorylocal)
        
        dDictionaryOfPairsDictionariesBySymbol = o.DictionaryOfPairsDictionariesBySymbol
        
        dPairsCalculated = {}
        dPairsValid = {}
        
        for kSymbol,vPairsDictionary in dDictionaryOfPairsDictionariesBySymbol.items():
            dPairs  = vPairsDictionary
            #if showresults == 1:
            print('building valid pairs... ' + kSymbol)
                
            for k,ls in dPairs.items():
                earlier = ls[0]
                later = ls[1]
                if earlier.bid.replace('.','',1).isdigit(): #and float(earlier.bid) >= 0.25:
                    #if float(earlier.bid) <= 4.0:
                        if (earlier.optiontype == 'C' and float(earlier.stockprice) < float(earlier.strike)) or (earlier.optiontype == 'P' and float(earlier.stockprice) > float(earlier.strike)): 
    #------------------------------------------
    #-- Set your Percentage cutoff here
    #------------------------------------------
                            if later.ask.replace('.','',1).isdigit() and float(later.ask) > 0.0:
                                if float(earlier.bid)/float(later.ask) > 0.8:
                                    #if float(earlier.bid)/float(later.ask) <= 1.0:
                                    dPairsCalculated[len(dPairsCalculated)] = float(earlier.bid)/float(later.ask)
                                    dPairsValid[len(dPairsValid)] = ls
                                    if showresults == 1:
                                        print(str(len(dPairsCalculated)) + ' valid pairs...')
        
        print('sorting results...')            
        from collections import OrderedDict
        dOrdered = OrderedDict(sorted(dPairsCalculated.items(), key=lambda t: t[1]))
        print(str(len(dOrdered))+ ' items in Ordered dictionary')
        outputlines = {}
        
        #if showresults == 1:
        print('putting results into printable dictionary ' + str(len(dOrdered)) + ' lines')
        from datetime import datetime 
        for k1,v1 in dOrdered.items():
            #ls = list(dPairs.keys())[list(dPairs.values()).index(k1)]
            ls = dPairsValid.get(k1)
            earlier = ls[0]
            later = ls[1]
            outputlines[len(outputlines)]=earlier.optionsymbol + ',' + \
                later.optionsymbol + ',' + \
                "'" + str(earlier.strike) + '/' + str(later.strike) + ',' + \
                later.optiontype + ',' + \
                str(earlier.expirationdate-datetime.today()) + ',' + \
                str(later.expirationdate-earlier.expirationdate) + ',' + \
                str(float(earlier.strike) - float(later.strike)) + ',' + \
                str(later.stockprice) + ',' + \
                str(earlier.bid) + ',' + \
                str(later.ask) + ',' + '{percent:.0%}'.format(percent=float(earlier.bid)/float(later.ask)) + ',' + \
                str(float(later.ask)-float(earlier.bid)) + ',' + \
                str(later.inthemoney)
            
        mytools.general.make_sure_path_exists(directorylocaloutput)
        
        datetime14 = mytools.mystrings.ConvertDatetime14()
        print(datetime14)
        outputfilepath = directorylocaloutput + '\\calendarspreads ' + datetime14 + '.csv'
        #if showresults == 1:
        print('printing results to ' + outputfilepath)
            
        with open(outputfilepath, 'w') as f:
            for outputline in outputlines.values():
                f.write(outputline+'\n')

        #if showresults == 1:
        print('Finished executing calendarspreadslive...')
        self.OutputFilePathString = outputfilepath
 