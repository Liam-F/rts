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

import readandbuilddictionaryofsortablepairs_tc
c = readandbuilddictionaryofsortablepairs_tc.read('downloads\\2014-12-27\\11\\60', 0.4)

dSortableDictionary = {}
newkey = 0

#downloaddirectory1='downloads\\2014-12-25\\13\\15'
c = buildpairsdictionarywithcriteriafromdirectoryofpulledfiles.build(o.DownloadDirectoryLocal, 0.4)
                                                
for k1,v1 in c.DictionaryOfFilteredCalendarPairs.items():
    #print(k1)
    earlier = v1[0]
    later = v1[1]
    spreadpercentage = float(earlier.bid)/float(later.ask)
    valueatrisk = -float(earlier.bid)+float(later.ask)
    dSortableDictionary[len(dSortableDictionary)] = [spreadpercentage,earlier,later,o.DownloadDirectoryLocal,k1]

from collections import OrderedDict
dOrdered = OrderedDict(sorted(dSortableDictionary.items(), key=lambda t: t[1][0]))

dFullySortedResult = {}
for k2,v2 in dOrdered.items():
    origkey = v2[4]
    earlier = v2[1]
    later = v2[2]
    datasortedupon = v2[0]
    origdirectory = v2[3]
    dFullySortedResult[len(dFullySortedResult)] = [datasortedupon,earlier,later,origdirectory,origkey]

for k3,v3 in dFullySortedResult.items():
    earlier = v3[1]
    later = v3[2]
    print(k3,
            round(v3[0],3),
            earlier.bid,later.ask,
            earlier.optionsymbol,
            later.optionsymbol,
            v3[3],
        v3[4])