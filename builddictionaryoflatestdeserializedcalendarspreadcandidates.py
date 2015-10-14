# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 07:24:59 2015

@author: jmalinchak


to test:
---
import builddictionaryoflatestdeserializedcalendarspreadcandidates
topdirectory = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\\output\\calendarspreadcandidates'
o = builddictionaryoflatestdeserializedcalendarspreadcandidates.build(topdirectory,6,['DXJ','WAG'],1)
---

"""


class build:
    def __init__(self,
                 topdirectory = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\\output\\calendarspreadcandidates',
                 countoffolderstoinclude = 5,
                 excludesymbols = {},
                 showresults = 0):
                     
        print('initialized class builddictionaryoflatestdeserializedcalendarspreadcandidates.py ')
        self.execute_process(topdirectory,countoffolderstoinclude,excludesymbols,showresults)

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
    
    def execute_process(self,
                            topdirectory,
                            countoffolderstoinclude,
                            excludesymbols,
                            showresults):
                                
        self.Complete = 0
        
        from datetime import datetime
        starttime = datetime.now()
        
        #datetime.strptime(t1, TIME_FORMAT2) - datetime.strptime(t2, TIME_FORMAT2)
        #_.total_seconds()
        #-9.254
        
        showresults = 0
        import os
        
        #topdirectory = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\\output\\calendarspreadcandidates\\2015-01-21\\00\\45'
        #topdirectory = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\\output\\calendarspreadcandidates\\2015-01-21\\00'
        #topdirectory = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\\output\\calendarspreadcandidates\\2015-01-21\\00 archive'
        #topdirectory = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\\output\\calendarspreadcandidates'
        
        fulldictionary = {}
        mydictionary = {}
        
        for dirName, subdirList, fileList in os.walk(topdirectory):
            if len(subdirList) == 0:
                fulldictionary[len(fulldictionary)] = dirName
        #4444444
        for x in range(1, countoffolderstoinclude + 1):
            mydictionary[len(mydictionary)] = fulldictionary[len(fulldictionary) - x]
            print(mydictionary[len(mydictionary)-1])
        
        import deserializefromdictionaryofcandidatexmldirectories
        o_deserialized = deserializefromdictionaryofcandidatexmldirectories.deserialize(mydictionary,excludesymbols)
        d1 = o_deserialized.DictionaryOfDeserializedCalendarSpreadCandidates
        
        self.DictionaryOfDeserializedCalendarSpreadCandidates = d1
        self.DictionaryOfExcludedSymbols = o_deserialized.DictionaryOfExcludedSymbols
        self.Complete = 0
        
        #showresults = 1
        if showresults == 1:
            for k1,v1 in d1.items():
                print('-*-'
                     ,  str(k1+1)
             #        ,  v['keyid']
                     ,  v1['specifications']['symbol']
                     , '='
                     ,  v1['specifications']['stockprice']
                     ,  v1['calculations']['sortbymeasurename']
                     ,  v1['calculations']['sortbymeasurevalue']
                     ,  'VAR'
                     ,  v1['calculations']['valueatriskopen']
                     , 'earlierbid='
                     ,  v1['earlier']['bid']
                     , 'laterask='
                     ,  v1['later']['ask']
                     ,  v1['earlier']['optionsymbol']
                     ,  v1['later']['optionsymbol']
            
                     ,  v1['earlier']['bucketquotedatetime']
                    )
                    ##################################################################
        print('end','builddictionaryoflatestdeserializedcalendarspreadcandidates.py',datetime.now() - starttime)
