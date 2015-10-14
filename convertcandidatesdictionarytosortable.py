# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 07:20:16 2014

@author: jmalinchak
"""
class convert:
    def __init__(self,
                 dictionaryofcandidates,
                 sortbymeasure='spreadpercentageopen', # spreadpercentageopen | valueatriskopen
                 showresults=0):
        print('convertcandidatedictionarytosortable.py class iniitalized')             
        self.execute_convert(dictionaryofcandidates,sortbymeasure,showresults)

#    def set_DictionaryOfQualifiedCandidatesInput(self,DictionaryOfQualifiedCandidatesInput):
#        self._DictionaryOfQualifiedCandidatesInput = DictionaryOfQualifiedCandidatesInput
#    def get_DictionaryOfQualifiedCandidatesInput(self):
#        return self._DictionaryOfQualifiedCandidatesInput
#    DictionaryOfQualifiedCandidatesInput = property(get_DictionaryOfQualifiedCandidatesInput, set_DictionaryOfQualifiedCandidatesInput)   
    
    def set_DictionaryOfSortableCandidatesOutput(self,DictionaryOfSortableCandidatesOutput):
        self._DictionaryOfSortableCandidatesOutput = DictionaryOfSortableCandidatesOutput
    def get_DictionaryOfSortableCandidatesOutput(self):
        return self._DictionaryOfSortableCandidatesOutput
    DictionaryOfSortableCandidatesOutput = property(get_DictionaryOfSortableCandidatesOutput, set_DictionaryOfSortableCandidatesOutput)   
    
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

    
    def execute_convert(self,dictionaryofcandidates,sortbymeasure,showresults):

        ################################################    
        #
        # Returns downloaddirectorylocal
        #
        ################################################  
    
        #import os
        #import pullpricessbasedonlocalinputfilestodownloaddirectorylocal
             
        dSortableDictionary = {}
        if showresults == 1:
            print('------------------------------------------------ convertcandidatesdictionaryfromqualifiedtosortable')
        for k1,v1 in dictionaryofcandidates.items():            
            sortbymeasurename = v1['calculations']['sortbymeasurevalue']
            sortbymeasurevalue = float(v1['calculations']['sortbymeasurevalue'])

            dSortableDictionary[len(dSortableDictionary)] = {'sortbymeasurevalue' :sortbymeasurevalue, 'sortbymeasurename' : sortbymeasurename,'candidate' : v1}
        #######################################################################
        self.DictionaryOfSortableCandidatesOutput = dSortableDictionary
            
