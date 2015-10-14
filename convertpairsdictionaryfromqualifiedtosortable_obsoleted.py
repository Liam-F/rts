# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 07:20:16 2014

@author: jmalinchak
"""
class setup:
    def __init__(self,
                 showresults=1):
        print('convertpairsdictionaryfromqualifiedtosortable class iniitalized')             
        

    def set_DictionaryOfQualifiedPairsInput(self,DictionaryOfQualifiedPairsInput):
        self._DictionaryOfQualifiedPairsInput = DictionaryOfQualifiedPairsInput
    def get_DictionaryOfQualifiedPairsInput(self):
        return self._DictionaryOfQualifiedPairsInput
    DictionaryOfQualifiedPairsInput = property(get_DictionaryOfQualifiedPairsInput, set_DictionaryOfQualifiedPairsInput)   
    
    def set_DictionaryOfSortablePairsOutput(self,DictionaryOfSortablePairsOutput):
        self._DictionaryOfSortablePairsOutput = DictionaryOfSortablePairsOutput
    def get_DictionaryOfSortablePairsOutput(self):
        return self._DictionaryOfSortablePairsOutput
    DictionaryOfSortablePairsOutput = property(get_DictionaryOfSortablePairsOutput, set_DictionaryOfSortablePairsOutput)   
    
#    def set_DownloadDirectoryLocalInput(self,DownloadDirectoryLocalInput):
#        self._DownloadDirectoryLocalInput = DownloadDirectoryLocalInput
#    def get_DownloadDirectoryLocalInput(self):
#        return self._DownloadDirectoryLocalInput
#    DownloadDirectoryLocalInput = property(get_DownloadDirectoryLocalInput, set_DownloadDirectoryLocalInput)    

    def set_SortbyMeasure(self,SortbyMeasure):
        self._SortbyMeasure = SortbyMeasure
    def get_SortbyMeasure(self):
        return self._SortbyMeasure
    SortbyMeasure = property(get_SortbyMeasure, set_SortbyMeasure)    

    
    def ExecuteConvert(self,showresults=0):

        ################################################    
        #
        # Returns downloaddirectorylocal
        #
        ################################################  
    
        #import os
        #import pullpricessbasedonlocalinputfilestodownloaddirectorylocal
             
        dSortableDictionary = {}
                                               
        for k1,v1 in self.DictionaryOfQualifiedPairsInput.items():
            #print(k1)
            earlier = v1[0]
            later = v1[1]
            spreadpercentageopening = float(earlier.bid)/float(later.ask)
            valueatrisk = -float(earlier.bid)+float(later.ask)
            if self.SortbyMeasure == 'valueatrisk':
                dSortableDictionary[len(dSortableDictionary)] = [valueatrisk,earlier,later,k1,'valueatrisk']
            else:
                dSortableDictionary[len(dSortableDictionary)] = [spreadpercentageopening,earlier,later,k1,'spreadpercentageopening']
        #######################################################################
        self.DictionaryOfSortablePairsOutput = dSortableDictionary
            
