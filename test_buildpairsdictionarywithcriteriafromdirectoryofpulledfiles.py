# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 07:20:16 2014

@author: jmalinchak
"""
#import os
#SymbolsFile = os.getcwd() + '\\inputs\\SymbolsTest.txt'
#ExpirationsFile = os.getcwd() + '\\inputs\\ExpirationsTest.txt'
#DownloadsDirectory = os.getcwd() + '\\downloads'
#print(DownloadsDirectory)
#import pullpricessbasedonlocalinputfilestodownloaddirectorylocal
#o = pullpricessbasedonlocalinputfilestodownloaddirectorylocal.pull(SymbolsFile,ExpirationsFile,)

import buildpairsdictionarywithcriteriafromdirectoryofpulledfiles
#c = buildfilteredordereddictionaryfromdirectoryofpulledfiles.build('downloads\\2014-12-27\\11\\60', 0.4)
print('start')
dSortableDictionary = {}

downloaddirectory1='downloadsprocessed\\2015-04-24\\15\\45'
c = buildpairsdictionarywithcriteriafromdirectoryofpulledfiles.build(rootlocalforfilespulled=downloaddirectory1, maxvalueatrisk=0.4)
for k1,v1 in c.DictionaryOfFilteredCalendarPairs.items():
    #print(k1)
    earlier = v1[0]
    later = v1[1]
    spreadpercentage = float(earlier.bid)/float(later.ask)
    valueatrisk = -float(earlier.bid)+float(later.ask)
    dSortableDictionary[len(dSortableDictionary)] = [spreadpercentage,earlier,later,downloaddirectory1,k1]

from collections import OrderedDict
dOrdered = OrderedDict(sorted(dSortableDictionary.items(), key=lambda t: t[1][0]))
for k2,v2 in dOrdered.items():
    newkey = k2
    origkey = v2[4]
    earlier = v2[1]
    later = v2[2]
    datasortedupon = v2[0]
    origdirectory = v2[3]
    print(newkey,datasortedupon,earlier.bid,later.ask,origdirectory,origkey)
#
##import printorderedpairdictionary
#dOrderedPairDictionary = c.OrderedPairDictionary
##dOrderedPairDictionary
##for k1,v1 in dOrderedPairDictionary.items():
##    #print(k1)
##    earlier = v1[1][0]
##    later = v1[1][1]
##    print(float(earlier.bid)/float(later.ask))
#import printorderedpairdictionary
#c1 = printorderedpairdictionary.print(dOrderedPairDictionary,'downloads')
#print(c1.OutputFilePathString)