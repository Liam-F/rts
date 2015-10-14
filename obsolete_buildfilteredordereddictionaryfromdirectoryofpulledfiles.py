# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 11:35:00 2014

@author: jmalinchak
"""
class build:
    def __init__(self,
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
                             rootlocalforfilespulled,
                             #onlyoutofthemoney, # onlyoutofthemoney 1 for yes, 0 for no
                             maxvalueatrisk,
                             maxsellearlyprice, # MaxSellEarlyPrice
                             minbuylaterprice, # MinBuyLaterPrice
                             minspreadpercent, # MinimumSpreadPercentage
                             maxspreadpercent, # MinimumSpreadPercentage
                             earningsdatestring,
                             directorylocaloutput,showresults)
#TestValueAndPairTuple
    def set_UnOrderedPairDictionary(self,UnOrderedPairDictionary):
        self._UnOrderedPairDictionary = UnOrderedPairDictionary
    def get_UnOrderedPairDictionary(self):
        return self._UnOrderedPairDictionary
    UnOrderedPairDictionary = property(get_UnOrderedPairDictionary, set_UnOrderedPairDictionary)    

                             
    def set_OrderedPairDictionary(self,OrderedPairDictionary):
        self._OrderedPairDictionary = OrderedPairDictionary
    def get_OrderedPairDictionary(self):
        return self._OrderedPairDictionary
    OrderedPairDictionary = property(get_OrderedPairDictionary, set_OrderedPairDictionary)    
    
    
    
    def execute_results(self,
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
 #       import mytools
        downloaddirectorylocal = rootlocalforfilespulled #mytools.mystrings.appendnormaldateddirectorybasedoncurrenttime15(rootlocalforfilespulled)
        print('downloaddirectorylocal=' + downloaddirectorylocal)
        
        import readintomemorybuilddictionaryofpairsdictionariesbysymbol        
        o = readintomemorybuilddictionaryofpairsdictionariesbysymbol.read(downloaddirectorylocal)
        
        dDictionaryOfPairsDictionariesBySymbol = o.DictionaryOfPairsDictionariesBySymbol
        
        dTestValueAndPairTupleSortableByPairSpreadPct = {}
#        dPairsValid = {}
        

        
        dQualifiedPairsBasedOnCalendar = {}
        dQualifiedPairsBasedOnAllCriteriaProvided = {}
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
                    dQualifiedPairsBasedOnCalendar[len(dQualifiedPairsBasedOnCalendar)] = ls
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
                                            dQualifiedPairsBasedOnAllCriteriaProvided[len(dQualifiedPairsBasedOnAllCriteriaProvided)] = ls
                                            dTestValueAndPairTupleSortableByPairSpreadPct[len(dTestValueAndPairTupleSortableByPairSpreadPct)] = [float(earlier.bid)/float(later.ask),ls]
                                            #dPairsValid[len(dPairsValid)] = ls
                                            if showresults == 1:
                                                print(str(len(dTestValueAndPairTupleSortableByPairSpreadPct)) + ' valid pairs...')
        print(str(len(dQualifiedPairsBasedOnCalendar)) + ' qualified pairs based on straddling expiration date')
        print('sorting results...')            
        from collections import OrderedDict
        dOrdered = OrderedDict(sorted(dTestValueAndPairTupleSortableByPairSpreadPct.items(), key=lambda t: t[1][0]))
        self.OrderedPairDictionary = dOrdered
        self.UnOrderedPairDictionary = dQualifiedPairsBasedOnAllCriteriaProvided

#        for k1,v1 in dOrderedPairDictionary.items():
#            #print(k1)
#            earlier = v1[1][0]
#            later = v1[1][1]
#            print(float(earlier.bid)/float(later.ask))
 