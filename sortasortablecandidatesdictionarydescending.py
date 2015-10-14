# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 07:20:16 2014

@author: jmalinchak
"""
class sort:
    def __init__(self,
                 sortabledictionary,
                 showresults=0):
        print('convertpairsdictionaryfromqualifiedtosortable class iniitalized')             
        self.execute_convert(sortabledictionary,showresults)

#    def set_DictionaryOfQualifiedCandidatesInput(self,DictionaryOfQualifiedCandidatesInput):
#        self._DictionaryOfQualifiedCandidatesInput = DictionaryOfQualifiedCandidatesInput
#    def get_DictionaryOfQualifiedCandidatesInput(self):
#        return self._DictionaryOfQualifiedCandidatesInput
#    DictionaryOfQualifiedCandidatesInput = property(get_DictionaryOfQualifiedCandidatesInput, set_DictionaryOfQualifiedCandidatesInput)   
    
    def set_DictionaryOfSortedCandidatesOutput(self,DictionaryOfSortedCandidatesOutput):
        self._DictionaryOfSortedCandidatesOutput = DictionaryOfSortedCandidatesOutput
    def get_DictionaryOfSortedCandidatesOutput(self):
        return self._DictionaryOfSortedCandidatesOutput
    DictionaryOfSortedCandidatesOutput = property(get_DictionaryOfSortedCandidatesOutput, set_DictionaryOfSortedCandidatesOutput)   
    
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

    
    def execute_convert(self,sortabledictionary,showresults):
        if showresults == 1:
            print('------')
            print('Count of candidate dictionary items before sorting',len(sortabledictionary))
        
        from collections import OrderedDict
        dOrdered = OrderedDict(sorted(sortabledictionary.items(), key=lambda t: t[1]['sortbymeasurevalue'],reverse=True))
        
        dFullySortedResult = {}
        for k2,v2 in dOrdered.items():
            sortbymeasurename = v2['sortbymeasurename']
            sortbymeasurevalue = v2['sortbymeasurevalue'] #v2[0]
            candidate = v2['candidate'] #v2[1]
            #dFullySortedResult[len(dFullySortedResult)] = [sortbymeasurevalue,earlier,later,origkey]
            dFullySortedResult[len(dFullySortedResult)] = {'sortbymeasurename':sortbymeasurename,'sortbymeasurevalue':sortbymeasurevalue,'candidate':candidate}
        if showresults == 1:
            print('Count of candidate dictionary items after sorting',len(dFullySortedResult))
        self.DictionaryOfSortedCandidatesOutput = dFullySortedResult
        
#        if showresults == 1:
#            for k3,v3 in dFullySortedResult.items():
#                earlier = v3[1]
#                later = v3[2]
#                print(k3,
#                        round(v3[0],3),
#                        earlier.bid,later.ask,
#                        earlier.optionsymbol,
#                        later.optionsymbol,
#                        #v3[3],
#                    v3[3])
#            
