# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 07:20:16 2014

@author: jmalinchak
"""
import os

import buildpairsdictionarywithcriteriafromdirectoryofpulledfiles
import convertpairsdictionaryfromqualifiedtosortable

dDownloadDirectories = {}
dDownloadDirectories[len(dDownloadDirectories)] = 'downloads\\2014-12-27\\15\\45\\COP'
dDownloadDirectories[len(dDownloadDirectories)] = 'downloads\\2014-12-27\\15\\45\\TWTR'

dDictionaryOfDictionaries = {}
for k0,v0 in dDownloadDirectories.items():
    c = buildpairsdictionarywithcriteriafromdirectoryofpulledfiles.build(v0, 0.4)
    o = convertpairsdictionaryfromqualifiedtosortable.setup()
    o.DictionaryOfQualifiedPairsInput = c.DictionaryOfFilteredCalendarPairs
    o.SortbyMeasure = 'spreadpercentageopening'
    o.ExecuteConvert()
    dDictionaryOfDictionaries[len(dDictionaryOfDictionaries)] = o.DictionaryOfSortablePairsOutput

dSortableDictionaries = {}
for k0,v0 in dDictionaryOfDictionaries.items():
    for k1,v1 in v0.items():
        dSortableDictionaries[len(dSortableDictionaries)] = v1


print('------')
print('Counts',len(dDictionaryOfDictionaries[0]),len(dDictionaryOfDictionaries[1]),len(dSortableDictionaries))

from collections import OrderedDict
dOrdered = OrderedDict(sorted(dSortableDictionaries.items(), key=lambda t: t[1][0]))

dFullySortedResult = {}
for k2,v2 in dOrdered.items():
    origkey = v2[4]
    earlier = v2[1]
    later = v2[2]
    datasortedupon = v2[0]
    #origdirectory = v2[3]
    dFullySortedResult[len(dFullySortedResult)] = [datasortedupon,earlier,later,origkey]

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