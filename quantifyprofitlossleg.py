# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 00:17:18 2014

@author: jmalinchak
"""

#                 pathfilelocalsymbols='inputs\\SymbolsTemp.txt',
#                 pathfilelocalexpirations='inputs\\ExpirationsTemp.txt',
#                 rootlocalforfilespulled='downloads',
#                 directorylocaloutput='output',

class quantify:
    def __init__(self,
                 SellEarlyOptionSymbol,
                 BuyLaterOptionSymbol,
                 PairSpread,
                 showresults=1):
        print(SellEarlyOptionSymbol)
        self.execute_quantifyprofitlossleg(SellEarlyOptionSymbol,
                                             BuyLaterOptionSymbol,
                                             PairSpread,
                                             showresults)



        #        pathfilelocalsymbols,pathfilelocalexpirations,rootlocalforfilespulled,directorylocaloutput,

    def set_PairSpreadCurrent(self,PairSpreadCurrent):
        self._PairSpreadCurrent = PairSpreadCurrent
    def get_PairSpreadCurrent(self):
        return self._PairSpreadCurrent
    PairSpreadCurrent = property(get_PairSpreadCurrent, set_PairSpreadCurrent)    
        
    def set_OutputFilePathString(self,OutputFilePathString):
        self._OutputFilePathString = OutputFilePathString
    def get_OutputFilePathString(self):
        return self._OutputFilePathString
    OutputFilePathString = property(get_OutputFilePathString, set_OutputFilePathString)    
    

    def execute_quantifyprofitlossleg(self,
                                             SellEarlyOptionSymbol,
                                             BuyLaterOptionSymbol,
                                             PairSpread,
                                             showresults):

        

        pathfilelocalsymbols='inputs\\SymbolsTemp.txt'
        pathfilelocalexpirations='inputs\\ExpirationsTemp.txt'
        rootlocalforfilespulled='downloads'
        directorylocaloutput='output'

        import mytools as mt
        mysymbol = mt.get_from_optionsymbol.symbol(SellEarlyOptionSymbol)
        #file = open(pathfilelocalsymbols, 'w')
        #file.close()
        with open(pathfilelocalsymbols, 'w') as fsymbol:
            fsymbol.write(mysymbol+'\n')
        
        
        dExpirations={}        
        myexpiration=mt.get_from_optionsymbol.expirationdate(SellEarlyOptionSymbol)
        if not myexpiration in dExpirations:
            dExpirations[myexpiration] = myexpiration.strftime("%Y-%m-%d")
        myexpiration=mt.get_from_optionsymbol.expirationdate(BuyLaterOptionSymbol)
        if not myexpiration in dExpirations:
            dExpirations[myexpiration] = myexpiration.strftime("%Y-%m-%d")

        with open(pathfilelocalexpirations, 'w') as fexpirations:
            for k,v in dExpirations.items():
                fexpirations.write(v+'\n')

                
        #,pathfilelocalsymbols,pathfilelocalexpirations,rootlocalforfilespulled,directorylocaloutput
        ################################################    
        #
        # Returns file name of output
        #
        ################################################    
        import mytools
        downloaddirectorylocal = mytools.mystrings.appendnormaldateddirectorybasedoncurrenttime15(rootlocalforfilespulled)
        print('downloaddirectorylocal=' + downloaddirectorylocal)
        ################################################    
        import shutil
        shutil.rmtree(downloaddirectorylocal, ignore_errors=True)
        
        ################################################    
        import pullpricesallfromdirectorylocalroot
        pullpricesallfromdirectorylocalroot.pull(downloaddirectorylocal,
                                                  pathfilelocalsymbols,
                                                  pathfilelocalexpirations)
        ################################################
        
        import readintomemoryinsertcalendarspreadpairsintodictionary        
        cal = readintomemoryinsertcalendarspreadpairsintodictionary.read(downloaddirectorylocal)
        #if showresults == 1:
                        
        dPairs  = cal.PairsDictionary
        print('completed readintomemoryinsertcalendarspreadpairsintodictionary =' + str(len(dPairs)))
        

                
        #if showresults == 1:
        print('building valid pairs...')
        #PairSpreadcurrent = -999
        #putpairspreadcurrent = -999
        #PairSpreadcurrent = -999.99
        
        import structureforcalendartrade      
        
        for k,ls in dPairs.items():
            earlier = ls[0]
            later = ls[1]
            
            #print(earlier.optionsymbol + ' ' + later.optionsymbol)

            if earlier.optionsymbol == SellEarlyOptionSymbol:
                #print('My s',SellEarlyOptionSymbol,BuyLaterOptionSymbol)
                if later.optionsymbol == BuyLaterOptionSymbol:
                    #print('My s',SellEarlyOptionSymbol,BuyLaterOptionSymbol)
                    print('-----------------------------------------')
                    print('EarlierBid = ' + str(float(earlier.bid)))
                    print('EarlierAsk = ' + str(float(earlier.ask)))
                    print('EarlierMidpoint = ' + str(((float(earlier.bid) + float(earlier.ask)) / 2.0)))
                    print('LaterBid = ' + str(float(later.bid)))
                    print('LaterAsk = ' + str(float(later.ask)))
                    print('LaterMidpoint = ' + str(((float(later.bid) + float(later.ask)) / 2.0)))
                    print('-----------------------------------------')
                    structCalendarTrade = structureforcalendartrade.Framework(ls)

            
#        print('pairlaterbid='+str(structCalendarTrades))
#        print('pairearlierask='+str(pairearlierask))
#
#        print('putpairlaterbid='+str(putpairlaterbid))
#        print('putpairearlierask='+str(putpairearlierask))

#        oCalendarSpread = structCalendarTrade.closingpairspreadmarketprices
#        oPutCalendarSpread = structCalendarTradePut.closingpairspreadmarketprices

        print('openingpairspreadmarketprices='+str(structCalendarTrade.openingpairspreadmarketprices))
        print('openingpairspreadmidpointprices='+str(structCalendarTrade.openingpairspreadmidpointprices))
        
        
        print('closingpairspreadmarketprices='+str(structCalendarTrade.closingpairspreadmarketprices))
        print('closingpairspreadmidpointprices='+str(structCalendarTrade.closingpairspreadmidpointprices))
   
#o = quantify('CIEN141220C00018500','CIEN141226C00018500',0.11)
o = quantify('ORCL141220C00040000','ORCL141226C00040000',0.11)
o = quantify('ORCL141220P00039500','ORCL141226P00039500',0.11)

