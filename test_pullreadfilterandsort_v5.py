# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 07:20:16 2014

@author: jmalinchak
"""

dDownloadDirectories = {}
dDownloadDirectories[len(dDownloadDirectories)] = 'downloads\\2014-12-27\\15\\45\\COP'
dDownloadDirectories[len(dDownloadDirectories)] = 'downloads\\2014-12-27\\15\\45\\TWTR'
criteria_for_showresults = 0
criteria_for_minspreadpercent=0.7
criteria_for_maxvalueatrisk = 0.4
criteria_for_sortbymeasure = 'spreadpercentageopening' # # spreadpercentageopening | valueatrisk
import buildpairsdictionarywithcriteriafromdirectoryofpulledfiles
import convertpairsdictionaryfromqualifiedtosortable
import concatonatesortablepairdictionaries

dSortableDictionaries = {}

for k0,v0 in dDownloadDirectories.items():
    
    c = buildpairsdictionarywithcriteriafromdirectoryofpulledfiles.build(rootlocalforfilespulled=v0, 
                                                                         maxvalueatrisk=criteria_for_maxvalueatrisk,
                                                                         showresults=criteria_for_showresults) 
    o = convertpairsdictionaryfromqualifiedtosortable.convert(c.DictionaryOfFilteredCalendarPairs,criteria_for_sortbymeasure)
    r = concatonatesortablepairdictionaries.concatonate(dSortableDictionaries,o.DictionaryOfSortablePairsOutput)
    dSortableDictionaries = r.ResultingDictionaryOfSortablePairsOutput

import sortasortabledictionary
s = sortasortabledictionary.sort(dSortableDictionaries,1)

c = buildpairsdictionarywithcriteriafromdirectoryofpulledfiles.build(rootlocalforfilespulled='downloads\\2014-12-27\\15\\45\\EWZ', 
                                                                     maxvalueatrisk=criteria_for_maxvalueatrisk,
                                                                     showresults=criteria_for_showresults) 
o = convertpairsdictionaryfromqualifiedtosortable.convert(c.DictionaryOfFilteredCalendarPairs,criteria_for_sortbymeasure)
r = concatonatesortablepairdictionaries.concatonate(dSortableDictionaries,o.DictionaryOfSortablePairsOutput)
dSortableDictionaries = r.ResultingDictionaryOfSortablePairsOutput
s = sortasortabledictionary.sort(dSortableDictionaries,0)

dSortedPairsOutput = s.DictionaryOfSortedPairsOutput
for k3,v3 in dSortedPairsOutput.items():
    earlier = v3[1]
    later = v3[2]
    print(k3,
            round(v3[0],3),
            earlier.bid,later.ask,
            earlier.optionsymbol,
            later.optionsymbol,
            #v3[3],
        v3[3])