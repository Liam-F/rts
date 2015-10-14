# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 07:20:16 2014

@author: jmalinchak
"""
import os
#SymbolsFile = os.getcwd() + '\\inputs\\SymbolsTest.txt'
#ExpirationsFile = os.getcwd() + '\\inputs\\ExpirationsTest.txt'
#DownloadsDirectory = os.getcwd() + '\\downloads'
#print(DownloadsDirectory)
#import pullpricessbasedonlocalinputfilestodownloaddirectorylocal
#o = pullpricessbasedonlocalinputfilestodownloaddirectorylocal.pull(SymbolsFile,ExpirationsFile,)
#
##import readpairteststrategywithcriteria 
##c = readpairteststrategywithcriteria.read(o.DownloadDirectoryLocal,
##                                 0.4)
#
##c = buildfilteredordereddictionaryfromdirectoryofpulledfiles.build('downloads\\2014-12-27\\11\\60', 0.4)
#
#dSortableDictionary = {}
#newkey = 0

#downloaddirectory1='downloads\\2014-12-25\\13\\15'
import buildpairsdictionarywithcriteriafromdirectoryofpulledfiles
import convertpairsdictionaryfromqualifiedtosortable_tc

c = buildpairsdictionarywithcriteriafromdirectoryofpulledfiles.build('downloads\\2014-12-27\\15\\45\\COP', 0.4)
o = convertpairsdictionaryfromqualifiedtosortable_tc.setup()
o.DictionaryOfQualifiedPairsInput = c.DictionaryOfFilteredCalendarPairs
o.SortbyMeasure = 'spreadpercentageopening'
o.ExecuteConvert()
dSortableDictionary1 = o.DictionaryOfSortablePairsOutput

c = buildpairsdictionarywithcriteriafromdirectoryofpulledfiles.build('downloads\\2014-12-27\\15\\45\\TWTR', 0.4)
o = convertpairsdictionaryfromqualifiedtosortable_tc.setup()
o.DictionaryOfQualifiedPairsInput = c.DictionaryOfFilteredCalendarPairs
o.SortbyMeasure = 'spreadpercentageopening'
o.ExecuteConvert()
dSortableDictionary2 = o.DictionaryOfSortablePairsOutput

#from functools import reduce
#from functools import partial
#dSortableDictionaries = partial(reduce, lambda a,b: dict(a, **b))
dSortableDictionaries = {}
for k,v in dSortableDictionary1.items():
    dSortableDictionaries[len(dSortableDictionaries)] = v
for k,v in dSortableDictionary2.items():
    dSortableDictionaries[len(dSortableDictionaries)] = v

#from functools import reduce
#dSortableDictionaries = reduce(lambda x,y: dict(x, **y), (dSortableDictionary1, dSortableDictionary2))

print('------')
print('Counts',len(dSortableDictionary1),len(dSortableDictionary2),len(dSortableDictionaries))
#for k1,v1 in c.DictionaryOfFilteredCalendarPairs.items():
#    #print(k1)
#    earlier = v1[0]
#    later = v1[1]
#    spreadpercentage = float(earlier.bid)/float(later.ask)
#    valueatrisk = -float(earlier.bid)+float(later.ask)
#    dSortableDictionary[len(dSortableDictionary)] = [spreadpercentage,earlier,later,o.DownloadDirectoryLocal,k1]

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