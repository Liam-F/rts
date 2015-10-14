# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 07:20:16 2014

@author: jmalinchak
"""
class convert:
    def __init__(self,
                 dictionaryofpairs,
                 sortbymeasure='spreadpercentageopening',
                 showresults=0):
        print('convertpairsdictionaryfromqualifiedtosortable class iniitalized')             
        self.execute_convert(dictionaryofpairs,sortbymeasure,showresults)

#    def set_DictionaryOfQualifiedPairsInput(self,DictionaryOfQualifiedPairsInput):
#        self._DictionaryOfQualifiedPairsInput = DictionaryOfQualifiedPairsInput
#    def get_DictionaryOfQualifiedPairsInput(self):
#        return self._DictionaryOfQualifiedPairsInput
#    DictionaryOfQualifiedPairsInput = property(get_DictionaryOfQualifiedPairsInput, set_DictionaryOfQualifiedPairsInput)   
    
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

#    def set_SortbyMeasure(self,SortbyMeasure):
#        self._SortbyMeasure = SortbyMeasure
#    def get_SortbyMeasure(self):
#        return self._SortbyMeasure
#    SortbyMeasure = property(get_SortbyMeasure, set_SortbyMeasure)    

    
    def execute_convert(self,dictionaryofpairs,sortbymeasure,showresults):

        ################################################    
        #
        # Returns downloaddirectorylocal
        #
        ################################################  
    
        #import os
        #import pullpricessbasedonlocalinputfilestodownloaddirectorylocal
             
        dSortableDictionary = {}
        if showresults == 1:
            print('------------------------------------------------ convertpairsdictionaryfromqualifiedtosortable')
            
        for k1,v1 in dictionaryofpairs.items():
            #print(k1)
            earlier = v1[0]
            later = v1[1]
            spreadpercentageopening = float(earlier.bid)/float(later.ask)
            valueatrisk = -float(earlier.bid) + float(later.ask)
            
            if sortbymeasure == 'valueatrisk':
                dSortableDictionary[len(dSortableDictionary)] = {'sortbymeasurevalue' : valueatrisk, 'earlier' : earlier, 'later' : later, 'origkey' : k1, 'sortbymeasurename' : 'valueatrisk'}
            else:
                dSortableDictionary[len(dSortableDictionary)] = {'sortbymeasurevalue' : spreadpercentageopening, 'earlier' : earlier, 'later' : later, 'origkey' : k1, 'sortbymeasurename' : 'spreadpercentageopening'}
        #######################################################################
        self.DictionaryOfSortablePairsOutput = dSortableDictionary
            
