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

#    def set_DictionaryOfQualifiedPairsInput(self,DictionaryOfQualifiedPairsInput):
#        self._DictionaryOfQualifiedPairsInput = DictionaryOfQualifiedPairsInput
#    def get_DictionaryOfQualifiedPairsInput(self):
#        return self._DictionaryOfQualifiedPairsInput
#    DictionaryOfQualifiedPairsInput = property(get_DictionaryOfQualifiedPairsInput, set_DictionaryOfQualifiedPairsInput)   
    
    def set_DictionaryOfSortedPairsOutput(self,DictionaryOfSortedPairsOutput):
        self._DictionaryOfSortedPairsOutput = DictionaryOfSortedPairsOutput
    def get_DictionaryOfSortedPairsOutput(self):
        return self._DictionaryOfSortedPairsOutput
    DictionaryOfSortedPairsOutput = property(get_DictionaryOfSortedPairsOutput, set_DictionaryOfSortedPairsOutput)   
    
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
        print('------')
        sortabledictionary = sortabledictionary
        print('Count of dictionary items before sorting',len(sortabledictionary))
        
        from collections import OrderedDict
        dOrdered = OrderedDict(sorted(sortabledictionary.items(), key=lambda t: t[1][0]))
        
        dFullySortedResult = {}
        for k2,v2 in dOrdered.items():
            origkey = v2[4]
            earlier = v2[1]
            later = v2[2]
            datasortedupon = v2[0]
            #origdirectory = v2[3]
            dFullySortedResult[len(dFullySortedResult)] = [datasortedupon,earlier,later,origkey]
            
        print('Count of dictionary items after sorting',len(dFullySortedResult))
        self.DictionaryOfSortedPairsOutput = dFullySortedResult
        
        if showresults == 1:
            for k3,v3 in dFullySortedResult.items():
                earlier = v3[1]
                later = v3[2]
                print(k3,
                        round(v3[0],3),
                        earlier.bid,later.ask,
                        earlier.optionsymbol,
                        later.optionsymbol,
                        #v3[3],
                    v3[3])
            
