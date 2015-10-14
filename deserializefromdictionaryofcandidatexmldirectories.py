# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 07:24:59 2015

@author: jmalinchak
"""
class deserialize:
    def __init__(self,
                 dictionaryofcandidatexmldirectories,
                 excludesymbols = {},
                 showresults=0):
        print('initialized class deserializefromdictionaryofcandidatexmldirectories.py')
        print('- -','called from builddictionaryoflatestdeserializedcalendarspreadcandidates.py')
        self.execute_process(dictionaryofcandidatexmldirectories,excludesymbols,showresults)

    def set_DictionaryOfDeserializedCalendarSpreadCandidates(self,DictionaryOfDeserializedCalendarSpreadCandidates):
        self._DictionaryOfDeserializedCalendarSpreadCandidates = DictionaryOfDeserializedCalendarSpreadCandidates
    def get_DictionaryOfDeserializedCalendarSpreadCandidates(self):
        return self._DictionaryOfDeserializedCalendarSpreadCandidates
    DictionaryOfDeserializedCalendarSpreadCandidates = property(get_DictionaryOfDeserializedCalendarSpreadCandidates, set_DictionaryOfDeserializedCalendarSpreadCandidates)   

    def set_DictionaryOfExcludedSymbols(self,DictionaryOfExcludedSymbols):
        self._DictionaryOfExcludedSymbols = DictionaryOfExcludedSymbols
    def get_DictionaryOfExcludedSymbols(self):
        return self._DictionaryOfExcludedSymbols
    DictionaryOfExcludedSymbols = property(get_DictionaryOfExcludedSymbols, set_DictionaryOfExcludedSymbols)   
    

    def set_Complete(self,Complete):
        self._Complete = Complete
    def get_Complete(self):
        return self._Complete
    Complete = property(get_Complete, set_Complete) 
    
    def execute_process(self,dictionaryofcandidatexmldirectories,excludesymbols,showresults):
        self.Complete = 0
        d_candidates ={}
        from datetime import datetime
        starttime = datetime.now()
        
        #datetime.strptime(t1, TIME_FORMAT2) - datetime.strptime(t2, TIME_FORMAT2)
        #_.total_seconds()
        #-9.254
        
        showresults = 0
        import os
        import deserializecandidatesxml
        
        d1 = {}
        #d2 = {}
        d3 = {}
        d_exclude = {}
        runningsumofxmlfiles = 0
        totalcandidatepairs = 0
        
        #topdirectory = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\\output\\calendarspreadcandidates\\2015-01-21\\00\\45'
        #topdirectory = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\\output\\calendarspreadcandidates\\2015-01-21\\00'
        #topdirectory = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\\output\\calendarspreadcandidates\\2015-01-21\\00 archive'
        for k,directoryofcandidatexml in dictionaryofcandidatexmldirectories.items():
            topdirectory = directoryofcandidatexml #'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\\output\\calendarspreadcandidates\\2015-01-31'
            
            rootdir = topdirectory 
            

            
            #import mytools
            
            for subdir, dirs, files in os.walk(rootdir):
                runningsumofxmlfiles = runningsumofxmlfiles + len(files)
                
                for file in files:
                    #testvalid = file[:15]
                    #if file.find(excludesymbols) == -1:
                    print(file)
                    pathfilenamecandidatexml = os.path.join(subdir, file)
                    print('  ','-----------------------------')
                    print('  ','-- Iterating: deserializefromdictionaryofcandidatexmldirectories.py')

                    
                    o1 = deserializecandidatesxml.deserialize(pathfilenamecandidatexml)
                    d1 = o1.DictionaryOfCandidatesFromXML
                    
                    totalcandidatepairs = totalcandidatepairs + len(d1)
                    
                    #print('   --',len(d1),'candidate pairs found')
                    
                    for k,v in d1.items():
                        if v['specifications']['symbol'] in excludesymbols.values():
                            if not v['specifications']['symbol'] in d_exclude.values():
                                d_exclude[len(d_exclude)] = v['specifications']['symbol']
                                
                        if not v['specifications']['symbol'] in excludesymbols.values():
                            d3[len(d3)] = v 
                        
                    print('   --',len(d1),'candidate pairs in',v['specifications']['symbol'])
                    
                    print('  ','--',pathfilenamecandidatexml)
            
            #endtime1 = datetime.now()
            #difftimexml = endtime1 - starttime # yields a timedelta object
            print('---------------------------------------------------')
            print('-- Iterating Complete','---------------------------')
            print('---------------------------------------------------')
        import convertcandidatesdictionarytosortable
        o_convertcandidatesdictionarytosortable = convertcandidatesdictionarytosortable.convert(d3,sortbymeasure='spreadpercentageopen')
        d4 = o_convertcandidatesdictionarytosortable.DictionaryOfSortableCandidatesOutput
        import sortasortablecandidatesdictionarydescending
        o_sortasortablecandidatesdictionary = sortasortablecandidatesdictionarydescending.sort(d4)
        d5 = o_sortasortablecandidatesdictionary.DictionaryOfSortedCandidatesOutput
        for k1,v1 in d5.items():
            v = v1['candidate']
            d_candidates[len(d_candidates)] = v
            #earlieroptionsymbol = v['earlier']['optionsymbol']
            #expirationdate = mytools.get_from_optionsymbol.expirationdate(earlieroptionsymbol).date()
            #vdate = mytools.mystrings.ConvertStringToDate('2015-02-14')
            
            #if expirationdate <= vdate:
            
            ##################################################################
            #showresults = 0
            if showresults == 1:
                print(
                     'k'
                     ,  str(k1+1)
             #        ,  v['keyid']
                     ,  v['specifications']['symbol']
                     , '='
                     ,  v['specifications']['stockprice']
                     ,  v['calculations']['sortbymeasurename']
                     ,  v['calculations']['sortbymeasurevalue']
                     ,  'VAR'
                     ,  v['calculations']['valueatriskopen']
                     , 'earlierbid='
                     ,  v['earlier']['bid']
                     , 'laterask='
                     ,  v['later']['ask']
                     ,  v['earlier']['optionsymbol']
                     ,  v['later']['optionsymbol']
            
                     ,  v['earlier']['bucketquotedatetime']
                    )
            ##################################################################
            
        endtime = datetime.now()
        print('-- ','Started',str(starttime))
        #print(str(endtime))
        difftimetotal = endtime - starttime # yields a timedelta object
        print('-- --', 'Directory count',len(dictionaryofcandidatexmldirectories))
        
        print('-- --', runningsumofxmlfiles,'candidate xml files deserialized')
        #print('-- --', totalcandidatepairs,'total candidate xml files')
        print('-- --', len(d_candidates), ' candidates in base dictionary')
        print('-- --', len(d_exclude),'candidate(s) excluded')
        #print('-- --', str(difftimexml.microseconds/100000.0), 'microseconds to process xml files')
        
        print('--','Ended:',str(endtime))
        print('--', str(difftimetotal.microseconds/100000.0), 'seconds to process')
        print('Source',dictionaryofcandidatexmldirectories.items())
        self.DictionaryOfDeserializedCalendarSpreadCandidates = d_candidates        
        self.DictionaryOfExcludedSymbols = d_exclude    
        self.Complete = 1      