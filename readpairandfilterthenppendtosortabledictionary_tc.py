# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 07:20:16 2014

@author: jmalinchak
"""
import os
#import pullpricessbasedonlocalinputfilestodownloaddirectorylocal


dSortableDictionary = {}

#######################################################################
#SymbolsFile = os.getcwd() + '\\inputs\\SymbolsTest.txt'
#ExpirationsFile = os.getcwd() + '\\inputs\\ExpirationsTest.txt'
#DownloadsDirectory = os.getcwd() + '\\downloads'
#print(DownloadsDirectory)
#o = pullpricessbasedonlocalinputfilestodownloaddirectorylocal.pull(SymbolsFile,ExpirationsFile,)

downloadedfilespath = os.path.join(os.getcwd(),'downloads','2014-12-27','15','45')
downloadedfilespathsymbol= os.path.join(downloadedfilespath,'EWZ')
import buildpairsdictionarywithcriteriafromdirectoryofpulledfiles
c = buildpairsdictionarywithcriteriafromdirectoryofpulledfiles.build(downloadedfilespathsymbol, 0.4)
                                                
for k1,v1 in c.DictionaryOfFilteredCalendarPairs.items():
    #print(k1)
    earlier = v1[0]
    later = v1[1]
    spreadpercentage = float(earlier.bid)/float(later.ask)
    valueatrisk = -float(earlier.bid)+float(later.ask)
    dSortableDictionary[len(dSortableDictionary)] = [spreadpercentage,earlier,later,downloadedfilespathsymbol,k1]
#######################################################################
    
    
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