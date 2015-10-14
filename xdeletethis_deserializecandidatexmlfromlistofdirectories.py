# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 07:24:59 2015

@author: jmalinchak
"""
class deserialize:
    def __init__(self,
                 dictionaryofcandidatexmldirectories,
                 showresults=0):
        print('initialized class serializesortedpairdictionarytoxml.py ')
        self.execute_process(dictionaryofcandidatexmldirectories,showresults)

#    def set_DictionaryOfQualifiedPairsInput(self,DictionaryOfQualifiedPairsInput):
#        self._DictionaryOfQualifiedPairsInput = DictionaryOfQualifiedPairsInput
#    def get_DictionaryOfQualifiedPairsInput(self):
#        return self._DictionaryOfQualifiedPairsInput
#    DictionaryOfQualifiedPairsInput = property(get_DictionaryOfQualifiedPairsInput, set_DictionaryOfQualifiedPairsInput)   
    
    def set_Complete(self,Complete):
        self._Complete = Complete
    def get_Complete(self):
        return self._Complete
    Complete = property(get_Complete, set_Complete) 
    
    def execute_process(self,dictionaryofcandidatexmldirectories,showresults):
        self.Complete = 0
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
        #topdirectory = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\\output\\calendarspreadcandidates\\2015-01-21\\00\\45'
        #topdirectory = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\\output\\calendarspreadcandidates\\2015-01-21\\00'
        #topdirectory = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\\output\\calendarspreadcandidates\\2015-01-21\\00 archive'
        for directoryofcandidatexml in dictionaryofcandidatexmldirectories:
            topdirectory = directoryofcandidatexml #'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\\output\\calendarspreadcandidates\\2015-01-31'
            
            rootdir = topdirectory 
            
            runningsumofxmlfiles = 0
            runningsumofcandidates = 0
            
            #import mytools
            
            for subdir, dirs, files in os.walk(rootdir):
                runningsumofxmlfiles = runningsumofxmlfiles + len(files)
                for file in files:
                    
                    pathfilenamecandidatexml = os.path.join(subdir, file)
                    print('-----------------------------')
                    print('-- ','pathfilenamecandidatexml')
                    print('--  ',pathfilenamecandidatexml)
                    
                    o1 = deserializecandidatesxml.deserialize(pathfilenamecandidatexml)
                    d1 = o1.DictionaryOfCandidatesFromXML
                    
                    runningsumofcandidates = runningsumofcandidates + len(d1)
                    print('--------------------')
                    print('-- processing '+str(len(d1))+' candidates')
                    
                    for k,v in d1.items():
                        d3[len(d3)] = v 
                        
                        if showresults == 1:
                            print(
                                'k'
                                ,  v['keyid']
                                ,  v['specifications']['symbol']
                                ,  v['calculations']['sortbymeasurename']
                                ,  v['calculations']['sortbymeasurevalue']
                                ,  'VAR (open)'
                                ,  v['calculations']['valueatriskopen']
                
                                ,  v['earlier']['optionsymbol']
                                ,  v['later']['optionsymbol']
                                ,  v['earlier']['bucketquotedatetime']
                                )
                    print('')
                    print('--------------------')
                    print('-- End of test_loop_deserializecandidatexml')
            
            
            #endtime1 = datetime.now()
            #difftimexml = endtime1 - starttime # yields a timedelta object
            
            import convertcandidatesdictionarytosortable
            o_convertcandidatesdictionarytosortable = convertcandidatesdictionarytosortable.convert(d3,sortbymeasure='spreadpercentageopen')
            d4 = o_convertcandidatesdictionarytosortable.DictionaryOfSortableCandidatesOutput
            import sortasortablecandidatesdictionary
            o_sortasortablecandidatesdictionary = sortasortablecandidatesdictionary.sort(d4)
            d5 = o_sortasortablecandidatesdictionary.DictionaryOfSortedCandidatesOutput
            for k1,v1 in d5.items():
                v = v1['candidate']
                
                #earlieroptionsymbol = v['earlier']['optionsymbol']
                #expirationdate = mytools.get_from_optionsymbol.expirationdate(earlieroptionsymbol).date()
                #vdate = mytools.mystrings.ConvertStringToDate('2015-02-14')
                
                #if expirationdate <= vdate:
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
            
            endtime = datetime.now()
            print(str(starttime))
            print(str(endtime))
            difftimetotal = endtime - starttime # yields a timedelta object
            
            print('-- ', directoryofcandidatexml)
            print('-- ', str(runningsumofxmlfiles) + ' candidate xml files deserialized')
            print('-- ', str(runningsumofcandidates) + ' total candidates')
            print('-- ', str(len(d3)) + ' candidates now in base dictionary')
            #print('-- ', str(difftimexml.microseconds/100000.0), 'microseconds to process xml files')
            print('-- ', str(difftimetotal.microseconds/100000.0), 'seconds to process everything')
            self.Complete = 1      