# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 11:35:00 2014

@author: jmalinchak
"""
class read:
    def __init__(self,
#             pathfilelocalsymbols='inputs\\SymbolsTest.txt',
#             pathfilelocalexpirations='inputs\\ExpirationsTest.txt',
             rootlocalforfilespulled='downloads\\2014-12-21\\11\\30',
             maxvalueatrisk = 10.0, # maximum loss 0.2 for $200
             #onlyoutofthemoney = 1, # onlyoutofthemoney 1 for yes, 0 for no
             maxsellearlyprice = 20.0, # MaxSellEarlyPrice
             minbuylaterprice = 0.0, # MinBuyLaterPrice
             minspreadpercent = 0.5, # MinimumSpreadPercentage
             maxspreadpercent = 1.0, # MinimumSpreadPercentage
             earningsdatestring='', #EarlierExpirationIsBefore and LaterExpirationIsAfter
             directorylocaloutput='output',
             showresults=0):
        self.execute_results(
#                             pathfilelocalsymbols,
#                             pathfilelocalexpirations,
                             rootlocalforfilespulled,
                             #onlyoutofthemoney, # onlyoutofthemoney 1 for yes, 0 for no
                             maxvalueatrisk,
                             maxsellearlyprice, # MaxSellEarlyPrice
                             minbuylaterprice, # MinBuyLaterPrice
                             minspreadpercent, # MinimumSpreadPercentage
                             maxspreadpercent, # MinimumSpreadPercentage
                             earningsdatestring,
                             directorylocaloutput,showresults)

    def set_OutputFilePathString(self,OutputFilePathString):
        self._OutputFilePathString = OutputFilePathString
    def get_OutputFilePathString(self):
        return self._OutputFilePathString
    OutputFilePathString = property(get_OutputFilePathString, set_OutputFilePathString)    
    
    def execute_results(self,
#                        pathfilelocalsymbols,
#                        pathfilelocalexpirations,
                        rootlocalforfilespulled,
                        #onlyoutofthemoney, # onlyoutofthemoney 1 for yes, 0 for no
                        maxvalueatrisk, 
                        maxsellearlyprice, # MaxSellEarlyPrice
                        minbuylaterprice, # MinBuyLaterPrice
                        minspreadpercent, # MinimumSpreadPercentage
                        maxspreadpercent, # MinimumSpreadPercentage
                        earningsdatestring,
                        directorylocaloutput,
                        showresults):
        import mytools
        downloaddirectorylocal = rootlocalforfilespulled #mytools.mystrings.appendnormaldateddirectorybasedoncurrenttime15(rootlocalforfilespulled)
        print('downloaddirectorylocal=' + downloaddirectorylocal)
        
        import readintomemorybuilddictionaryofpairsdictionariesbysymbol        
        o = readintomemorybuilddictionaryofpairsdictionariesbysymbol.read(downloaddirectorylocal)
        
        dDictionaryOfPairsDictionariesBySymbol = o.DictionaryOfPairsDictionariesBySymbol
        
        dPairsCalculated = {}
        dPairsValid = {}
        

        
        dQualifiedPairsBasedOnDate = {}
        bContinue = 1   
        for kSymbol,vPairsDictionary in dDictionaryOfPairsDictionariesBySymbol.items():
            dPairs  = vPairsDictionary
            #if showresults == 1:
            print('building valid pairs... ' + kSymbol)
            bContinue == 1            
            for k,ls in dPairs.items():
                earlier = ls[0]
                later = ls[1]
                bContinue == 1
                #-- Make sure EarlierExpirationIsBefore and LaterExpirationIsAfter
                if len(earningsdatestring) > 0:
                    bContinue == 0
                    from datetime import datetime
                    earningsdate = datetime.strptime(earningsdatestring, '%Y-%m-%d')
                    print('earningsdate= ' + str(earningsdate))
                    if earlier.expirationdate <= earningsdate and later.expirationdate > earningsdate:
                        bContinue == 1
                if bContinue == 1:
                    dQualifiedPairsBasedOnDate[len(dQualifiedPairsBasedOnDate)] = ls
                    #-- Make sure onlyoutofthemoney is respected
#                    if onlyoutofthemoney == 1:
#                        bContinue == 0
                    if (earlier.optiontype == 'C' and float(earlier.stockprice) < float(earlier.strike)) or (earlier.optiontype == 'P' and float(earlier.stockprice) > float(earlier.strike)):
                            #print('passed',earlier.optiontype ,earlier.stockprice,earlier.strike)
#                            bContinue == 1
#                    print( bContinue,earlier.optiontype ,earlier.stockprice,earlier.strike)
#                    if bContinue == 1:
                        #-- Set your MaxSellEarlyPrice
                        if earlier.bid.replace('.','',1).isdigit() and float(earlier.bid) <= maxsellearlyprice:
                            #-- Set your MinBuyLaterPrice    
                            if later.ask.replace('.','',1).isdigit() and float(later.ask) > minbuylaterprice:
                                #-- Make sure MinimumSpreadPercentage is greater than
                                if float(earlier.bid)/float(later.ask) > minspreadpercent:
                                    #-- Make sure MaximumSpreadPercentage is less than
                                    if float(earlier.bid)/float(later.ask) <= maxspreadpercent:
                                        if float(maxvalueatrisk) >= -float(earlier.bid)+float(later.ask):
                                            dPairsCalculated[len(dPairsCalculated)] = float(earlier.bid)/float(later.ask)
                                            dPairsValid[len(dPairsValid)] = ls
                                            if showresults == 1:
                                                print(str(len(dPairsCalculated)) + ' valid pairs...')
        print(str(len(dQualifiedPairsBasedOnDate)) + ' qualified pairs based on straddling expiration date')
        print('sorting results...')            
        from collections import OrderedDict
        dOrdered = OrderedDict(sorted(dPairsCalculated.items(), key=lambda t: t[1]))
        print(str(len(dOrdered))+ ' items in Ordered dictionary')
        outputlines = {}
        outputlines[len(outputlines)]='earlier.optionsymbol' + ',' + \
                'later.optionsymbol' + ',' + \
                'earlier.strike' + '/' + 'later.strike' + ',' + \
                'later.optiontype' + ',' + \
                'earlier.expirationdate-datetime.today()' + ',' + 'remainder' + ',' + \
                'later.expirationdate-earlier.expirationdate' + ',' + 'remainder' + ',' + \
                'earlier.strike - later.strike' + ',' + \
                'later.stockprice' + ',' + \
                'earlier.bid' + ',' + \
                'later.ask' + ',' + 'percent earlier.bid/later.ask' + ',' + \
                'later.ask-earlier.bid' + ',' + \
                'later.inthemoney'
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
 