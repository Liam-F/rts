# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 00:17:18 2014

@author: jmalinchak
"""
class read:
    def __init__(self, directorylocal='',symbol='',expirationdate='',optiontype='',strike='',bucketquotedatetime='',showresults=1):
        self.execute_results(directorylocal,symbol,expirationdate,optiontype,strike,bucketquotedatetime,showresults)
        
#    def set_MainDictionariesObject(self,MainDictionariesObject):
#        self._MainDictionariesObject = MainDictionariesObject
#    def get_MainDictionariesObject(self):
#        return self._MainDictionariesObject
#    MainDictionariesObject = property(get_MainDictionariesObject, set_MainDictionariesObject)
    
    def set_DictionaryOfFilteredInstances(self,DictionaryOfFilteredInstances):
        self._DictionaryOfFilteredInstances = DictionaryOfFilteredInstances
    def get_DictionaryOfFilteredInstances(self):
        return self._DictionaryOfFilteredInstances
    DictionaryOfFilteredInstances = property(get_DictionaryOfFilteredInstances, set_DictionaryOfFilteredInstances)
    
    def set_DictionaryOfAllInstances(self,DictionaryOfAllInstances):
        self._DictionaryOfAllInstances = DictionaryOfAllInstances
    def get_DictionaryOfAllInstances(self):
        return self._DictionaryOfAllInstances
    DictionaryOfAllInstances = property(get_DictionaryOfAllInstances, set_DictionaryOfAllInstances)
    
    def execute_results(self,directorylocal,symbol,expirationdate,optiontype,strike,bucketquotedatetime,showresults):
        import readintomemoryfilterresults
        print("executing readintomemory...")
        o = readintomemoryfilterresults.read(directorylocal)
        o.filterresults(symbol,expirationdate,optiontype,strike,bucketquotedatetime)
        self.NamedDictionaries = o.NamedDictionaries
        self.DictionaryOfFilteredInstances = o.DictionaryOfFilteredInstances
        if showresults == 1:
            for KeyOfOptionInstances,ValueOfOptionInstances in self.DictionaryOfFilteredInstances.items():
                ValueOfOptionInstances.printdelim(' ')
                
        