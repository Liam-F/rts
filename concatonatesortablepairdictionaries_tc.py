# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 07:20:16 2014

@author: jmalinchak
"""
class concatonate:
    def __init__(self, existing,appending,
                 showresults=0):
        self.execute_concate(existing,appending,showresults)
        print('concatonatesortablepairdictionaries_tc.py class iniitalized')             
        
#    def set_ExistingDictionaryOfSortablePairsInput(self,ExistingDictionaryOfSortablePairsInput):
#        self._ExistingDictionaryOfSortablePairsInput = ExistingDictionaryOfSortablePairsInput
#    def get_ExistingDictionaryOfSortablePairsInput(self):
#        return self._ExistingDictionaryOfSortablePairsInput
#    ExistingDictionaryOfSortablePairsInput = property(get_ExistingDictionaryOfSortablePairsInput, set_ExistingDictionaryOfSortablePairsInput)   
#    
#
#    def set_AppendingDictionaryOfSortablePairsInput(self,AppendingDictionaryOfSortablePairsInput):
#        self._AppendingDictionaryOfSortablePairsInput = AppendingDictionaryOfSortablePairsInput
#    def get_AppendingDictionaryOfSortablePairsInput(self):
#        return self._AppendingDictionaryOfSortablePairsInput
#    AppendingDictionaryOfSortablePairsInput = property(get_AppendingDictionaryOfSortablePairsInput, set_AppendingDictionaryOfSortablePairsInput)   
#
    def set_ResultingDictionaryOfSortablePairsOutput(self,ResultingDictionaryOfSortablePairsOutput):
        self._ResultingDictionaryOfSortablePairsOutput = ResultingDictionaryOfSortablePairsOutput
    def get_ResultingDictionaryOfSortablePairsOutput(self):
        return self._ResultingDictionaryOfSortablePairsOutput
    ResultingDictionaryOfSortablePairsOutput = property(get_ResultingDictionaryOfSortablePairsOutput, set_ResultingDictionaryOfSortablePairsOutput)   
        

    
    def execute_concate(self,existing,appending,showresults=0):
        
        dSortableDictionaries = existing #self.ExistingDictionaryOfSortablePairsInput
        for k0,v0 in appending.items(): # self.AppendingDictionaryOfSortablePairsInput.items():
                dSortableDictionaries[len(dSortableDictionaries)] = v0
        print('------')
        self.ResultingDictionaryOfSortablePairsOutput = dSortableDictionaries
        #self.ResultingDictionaryOfSortablePairsOutput = dSortableDictionaries
        
        ##################################################################
        # Ordering done outside
    #    from collections import OrderedDict
    #    dOrdered = OrderedDict(sorted(dSortableDictionaries.items(), key=lambda t: t[1][0]))
    #    
    #    dFullySortedResult = {}
    #    for k2,v2 in dOrdered.items():
    #        origkey = v2[4]
    #        earlier = v2[1]
    #        later = v2[2]
    #        datasortedupon = v2[0]
    #        #origdirectory = v2[3]
    #        dFullySortedResult[len(dFullySortedResult)] = [datasortedupon,earlier,later,origkey]
    #    
    #    for k3,v3 in dFullySortedResult.items():
    #        earlier = v3[1]
    #        later = v3[2]
    #        print(k3,
    #                round(v3[0],3),
    #                earlier.bid,later.ask,
    #                earlier.optionsymbol,
    #                later.optionsymbol,
    #                #v3[3],
    #            v3[3])