# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 00:17:18 2014

@author: jmalinchak
"""

class calendarspreadslive:
    def __init__(self,
                 pathfilelocalsymbols='inputs\\SymbolsTest.txt',
                 pathfilelocalexpirations='inputs\\ExpirationsTest.txt',
                 rootlocalforfilespulled='downloads',
                 directorylocaloutput='output',
                 showresults=1):
                     
        self.execute_results(pathfilelocalsymbols,pathfilelocalexpirations,rootlocalforfilespulled,directorylocaloutput,showresults)
    
    def set_OutputFilePathString(self,OutputFilePathString):
        self._OutputFilePathString = OutputFilePathString
    def get_OutputFilePathString(self):
        return self._OutputFilePathString
    OutputFilePathString = property(get_OutputFilePathString, set_OutputFilePathString)    
    
    def execute_results(self,pathfilelocalsymbols,pathfilelocalexpirations,rootlocalforfilespulled,directorylocaloutput,showresults):
        ################################################
        #                                               
        #   Returns file name of output                 
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
        print('completed readintomemoryinsertcalendarspreadpairsintodictionary')
        
        dPairs  = cal.PairsDictionary
        
        dPairsCalculated = {}
                
        #if showresults == 1:
        print('building valid pairs...')
            
        for k,ls in dPairs.items():
            earlier = ls[0]
            later = ls[1]
            if earlier.bid.replace('.','',1).isdigit() and float(earlier.bid) >= 0.25:
                if float(earlier.bid) <= 4.0:
                    if (earlier.optiontype == 'C' and float(earlier.stockprice) < float(earlier.strike)) or (earlier.optiontype == 'P' and float(earlier.stockprice) > float(earlier.strike)): 
                        if later.ask.replace('.','',1).isdigit() and float(later.ask) > 0.0 and float(earlier.bid)/float(later.ask) > 0.6:
                            dPairsCalculated[k] = float(earlier.bid)/float(later.ask)
                            if showresults == 1:
                                print(str(len(dPairsCalculated)) + ' valid pairs...')
        
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
            
        mytools.general.make_sure_path_exists(directorylocaloutput)
        
        datetime14 = mytools.mystrings.ConvertDatetime14()
        print(datetime14)
        outputfilepath = directorylocaloutput + '\\' + datetime14 + '.csv'
        #if showresults == 1:
        print('printing results to ' + outputfilepath)
            
        with open(outputfilepath, 'w') as f:
            for outputline in outputlines.values():
                f.write(outputline+'\n')

        #if showresults == 1:
        print('Finished executing calendarspreadslive...')
        self.OutputFilePathString = outputfilepath
        
            
class calendarspreadslivenofilter:
    def __init__(self,
                 pathfilelocalsymbols='inputs\\SymbolsTest.txt',
                 pathfilelocalexpirations='inputs\\ExpirationsTest.txt',
                 rootlocalforfilespulled='downloads',
                 directorylocaloutput='output',
                 showresults=1):
                     
        self.execute_results(pathfilelocalsymbols,pathfilelocalexpirations,rootlocalforfilespulled,directorylocaloutput,showresults)
    
    def set_OutputFilePathString(self,OutputFilePathString):
        self._OutputFilePathString = OutputFilePathString
    def get_OutputFilePathString(self):
        return self._OutputFilePathString
    OutputFilePathString = property(get_OutputFilePathString, set_OutputFilePathString)    
    
    def execute_results(self,pathfilelocalsymbols,pathfilelocalexpirations,rootlocalforfilespulled,directorylocaloutput,showresults):
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

        import readintomemoryinsertcalendarspreadpairsintodictionarynonmatchingstrikes        
        cal = readintomemoryinsertcalendarspreadpairsintodictionarynonmatchingstrikes.read(downloaddirectorylocal)
        
        #if showresults == 1:
        print('completed readintomemoryinsertcalendarspreadpairsintodictionary')
        
        dPairs  = cal.PairsDictionary
        
        dPairsCalculated = {}
                
        #if showresults == 1:
        print('building valid pairs...')
            
        for k,ls in dPairs.items():
            earlier = ls[0]
            later = ls[1]
            #print(earlier.optionsymbol)
            #print(later.optionsymbol)
            if earlier.bid.replace('.','',1).isdigit(): #and float(earlier.bid) >= 0.25:
                #if float(earlier.bid) <= 4.0:
                    if (earlier.optiontype == 'C' and float(earlier.stockprice) < float(earlier.strike)) or (earlier.optiontype == 'P' and float(earlier.stockprice) > float(earlier.strike)): 
                        
#------------------------------------------
# Set your Percentage cutoff here
########################################## 
                        if later.ask.replace('.','',1).isdigit() and \
                            float(later.ask) > 0.0 and float(earlier.bid)/float(later.ask) > 0.8:
##########################################                                
                            
                            dPairsCalculated[k] = float(earlier.bid)/float(later.ask)
                            if showresults == 1:
                                print(str(len(dPairsCalculated)) + ' valid pairs...')
        
        print('sorting results...')            
        from collections import OrderedDict
        dOrdered = OrderedDict(sorted(dPairsCalculated.items(), key=lambda t: t[1]))
        outputlines = {}
        
        #if showresults == 1:
        print('putting results into printable dictionary ' + str(len(dOrdered)) + ' lines')
        from datetime import datetime 
        for k1,v1 in dOrdered.items():
            #ls = list(dPairs.keys())[list(dPairs.values()).index(k1)]
            ls = dPairs.get(k1)
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
        outputfilepath = directorylocaloutput + '\\calendarspreadslivenofilter ' + datetime14 + '.csv'
        #if showresults == 1:
        print('printing results to ' + outputfilepath)
            
        with open(outputfilepath, 'w') as f:
            for outputline in outputlines.values():
                f.write(outputline+'\n')

        #if showresults == 1:
        print('Finished executing calendarspreadslive...')
        self.OutputFilePathString = outputfilepath
        
            
