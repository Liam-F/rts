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
                 SellEarlyCallOptionSymbol,
                 BuyLaterCallOptionSymbol,
                 SellEarlyPutOptionSymbol,
                 BuyLaterPutOptionSymbol,
                 CallPairSpread,
                 PutPairSpread,
                 showresults=1):
        print(SellEarlyCallOptionSymbol)


        self.execute_quantifyprofitlosssingle(SellEarlyCallOptionSymbol,
                                             BuyLaterCallOptionSymbol,
                                             SellEarlyPutOptionSymbol,
                                             BuyLaterPutOptionSymbol,
                                             CallPairSpread,
                                             PutPairSpread,
                                             showresults)

        #        pathfilelocalsymbols,pathfilelocalexpirations,rootlocalforfilespulled,directorylocaloutput,

    def set_CallPairSpreadCurrent(self,CallPairSpreadCurrent):
        self._CallPairSpreadCurrent = CallPairSpreadCurrent
    def get_CallPairSpreadCurrent(self):
        return self._CallPairSpreadCurrent
    CallPairSpreadCurrent = property(get_CallPairSpreadCurrent, set_CallPairSpreadCurrent)    
        
    def set_OutputFilePathString(self,OutputFilePathString):
        self._OutputFilePathString = OutputFilePathString
    def get_OutputFilePathString(self):
        return self._OutputFilePathString
    OutputFilePathString = property(get_OutputFilePathString, set_OutputFilePathString)    
    
    
    def execute_quantifyprofitlosssingle(self,
                                             SellEarlyCallOptionSymbol,
                                             BuyLaterCallOptionSymbol,
                                             SellEarlyPutOptionSymbol,
                                             BuyLaterPutOptionSymbol,
                                             CallPairSpread,
                                             PutPairSpread,
                                             showresults):

        

        pathfilelocalsymbols='inputs\\SymbolsTemp.txt'
        pathfilelocalexpirations='inputs\\ExpirationsTemp.txt'
        rootlocalforfilespulled='downloads'
        directorylocaloutput='output'

        import mytools as mt
        mysymbol = mt.get_from_optionsymbol.symbol(SellEarlyCallOptionSymbol)
        #file = open(pathfilelocalsymbols, 'w')
        #file.close()
        with open(pathfilelocalsymbols, 'w') as fsymbol:
            fsymbol.write(mysymbol+'\n')
        
        import datetime
        
        dExpirations={}        
        myexpiration=mt.get_from_optionsymbol.expirationdate(SellEarlyCallOptionSymbol)
        if not myexpiration in dExpirations:
            dExpirations[myexpiration] = myexpiration.strftime("%Y-%m-%d")
        myexpiration=mt.get_from_optionsymbol.expirationdate(BuyLaterCallOptionSymbol)
        if not myexpiration in dExpirations:
            dExpirations[myexpiration] = myexpiration.strftime("%Y-%m-%d")
        myexpiration=mt.get_from_optionsymbol.expirationdate(SellEarlyPutOptionSymbol)
        if not myexpiration in dExpirations:
            dExpirations[myexpiration] = myexpiration.strftime("%Y-%m-%d")
        myexpiration=mt.get_from_optionsymbol.expirationdate(BuyLaterPutOptionSymbol)
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
        
        dMyPairs = {}
                
        #if showresults == 1:
        print('building valid pairs...')
        #callpairspreadcurrent = -999
        #putpairspreadcurrent = -999
        callpairspreadcurrent = -999.99
        putpairspreadcurrent = -999.99
        callpairlaterbid = -999.99
        callpairearlierask = -999.99
        putpairlaterbid = -999.99
        putpairearlierask = -999.99
        
        import structureforcalendartrade      
        
        for k,ls in dPairs.items():
            earlier = ls[0]
            later = ls[1]
            
            #print(earlier.optionsymbol + ' ' + later.optionsymbol)

            if earlier.optionsymbol == SellEarlyCallOptionSymbol:
                #print('My Calls',SellEarlyCallOptionSymbol,BuyLaterCallOptionSymbol)
                if later.optionsymbol == BuyLaterCallOptionSymbol:
                    #print('My Calls',SellEarlyCallOptionSymbol,BuyLaterCallOptionSymbol)
                    print('CallEarlierBid = ' + str(float(earlier.bid)))
                    print('CallEarlierAsk = ' + str(float(earlier.ask)))
                    print('CallEarlierMidpoint = ' + str(((float(earlier.bid) + float(earlier.ask)) / 2.0)))
                    print('CallLaterBid = ' + str(float(later.bid)))
                    print('CallLaterAsk = ' + str(float(later.ask)))
                    print('CallLaterMidpoint = ' + str(((float(later.bid) + float(later.ask)) / 2.0)))
                    
#                    callpairearlierask = float(earlier.ask)
#                    callpairspreadcurrent = float(later.bid) - float(earlier.ask)
                    dMyPairs['call'] = ls            
                    structCalendarTradeCall = structureforcalendartrade.Framework(ls)

            if earlier.optionsymbol == SellEarlyPutOptionSymbol:
                #print('My Puts',SellEarlyPutOptionSymbol,BuyLaterPutOptionSymbol)
                if later.optionsymbol == BuyLaterPutOptionSymbol:
                    print('PutEarlierBid = ' + str(float(earlier.bid)))
                    print('PutEarlierAsk = ' + str(float(earlier.ask)))
                    print('PutLaterBid = ' + str(float(later.bid)))
                    print('PutLaterAsk = ' + str(float(later.ask)))

#                    putpairlaterbid = float(later.bid)
#                    putpairearlierask = float(earlier.ask)
#                    putpairspreadcurrent = float(later.bid) - float(earlier.ask)
                    dMyPairs['put'] = ls
                    structCalendarTradePut = structureforcalendartrade.Framework(ls)
            
#        print('callpairlaterbid='+str(structCalendarTrades))
#        print('callpairearlierask='+str(callpairearlierask))
#
#        print('putpairlaterbid='+str(putpairlaterbid))
#        print('putpairearlierask='+str(putpairearlierask))

#        oCallCalendarSpread = structCalendarTradeCall.closingpairspreadmarketprices
#        oPutCalendarSpread = structCalendarTradePut.closingpairspreadmarketprices

        print('openingcallpairspreadmarketprices='+str(structCalendarTradeCall.openingpairspreadmarketprices))
        print('openingputpairspreadmarketprices='+str(structCalendarTradePut.openingpairspreadmarketprices))
        print('openingcallpairspreadmidpointprices='+str(structCalendarTradeCall.openingpairspreadmidpointprices))
        print('openingputpairspreadmidpointprices='+str(structCalendarTradePut.openingpairspreadmidpointprices))   
        
        
        print('closingcallpairspreadmarketprices='+str(structCalendarTradeCall.closingpairspreadmarketprices))
        print('closingputpairspreadmarketprices='+str(structCalendarTradePut.closingpairspreadmarketprices))
        print('closingcallpairspreadmidpointprices='+str(structCalendarTradeCall.closingpairspreadmidpointprices))
        print('closingputpairspreadmidpointprices='+str(structCalendarTradePut.closingpairspreadmidpointprices))        
#                    if (earlier.optiontype == 'C' and float(earlier.stockprice) < float(earlier.strike)) or (earlier.optiontype == 'P' and float(earlier.stockprice) > float(earlier.strike)): 
#                        if later.ask.replace('.','',1).isdigit() and float(later.ask) > 0.0 and float(earlier.bid)/float(later.ask) > 0.6:
#                            dPairsCalculated[k] = float(earlier.bid)/float(later.ask)
#                            if showresults == 1:
#                                print(str(len(dPairsCalculated)) + ' valid pairs...')
#        
#        print('sorting results...')
#            
#        from collections import OrderedDict
#        dOrdered = OrderedDict(sorted(dPairsCalculated.items(), key=lambda t: t[1]))
#        outputlines = {}
#        
#        #if showresults == 1:
#        print('putting results into printable dictionary ' + str(len(dOrdered)) + ' lines')
#            
#        for k1,v1 in dOrdered.items():
#            #ls = list(dPairs.keys())[list(dPairs.values()).index(k1)]
#            ls = dPairs.get(k1)
#            earlier = ls[0]
#            later = ls[1]
#            outputlines[len(outputlines)]=earlier.optionsymbol+','+later.optionsymbol+','+str(later.strike)+','+str(later.stockprice)+','+str(earlier.bid)+','+str(later.ask)+','+'{percent:.0%}'.format(percent=float(earlier.bid)/float(later.ask)) +','+ str(round(float(later.ask)-float(earlier.bid),2))
#            
#        mytools.general.make_sure_path_exists(directorylocaloutput)
#        
#        datetime14 = mytools.mystrings.ConvertDatetime14()
#        print(datetime14)
#        outputfilepath = directorylocaloutput + '\\' + datetime14 + '.csv'
#        #if showresults == 1:
#        print('printing results to ' + outputfilepath)
#            
#        with open(outputfilepath, 'w') as f:
#            for outputline in outputlines.values():
#                f.write(outputline+'\n')
#        
#        #if showresults == 1:
#        print('Finished executing calendarspreadslive...')
#        self.OutputFilePathString = outputfilepath
#        
#            
        ################################################    ################################################    ################################################    
#o = quantify('ORCL141220C00042000','ORCL141226C00042000','ORCL141220P00041000','ORCL141226P00041000',0.11,0.08)
#o = quantify('BRCM141226C00042000','BRCM150102C00042000','BRCM141226P00041000','BRCM150102P00041000',0.11,0.08)
o = quantify('BRCM141226C00042000','BRCM150102C00042000','BRCM141226P00041000','BRCM150102P00041000',0.11,0.08)


        ################################################    ################################################    ################################################    

#ORCL141220C00042000 ORCL141226C00042000
#ORCL141220C00042000 ORCL141226C00042000