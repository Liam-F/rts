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

import buildfilteredordereddictionaryfromdirectoryofpulledfiles
#c = buildfilteredordereddictionaryfromdirectoryofpulledfiles.build('downloads\\2014-12-27\\11\\60', 0.4)
c = buildfilteredordereddictionaryfromdirectoryofpulledfiles.build('downloads\\2014-12-25\\13\\15', 0.4)
#import printorderedpairdictionary
dOrderedPairDictionary = c.OrderedPairDictionary
#dOrderedPairDictionary
#for k1,v1 in dOrderedPairDictionary.items():
#    #print(k1)
#    earlier = v1[1][0]
#    later = v1[1][1]
#    print(float(earlier.bid)/float(later.ask))
import printorderedpairdictionary
c1 = printorderedpairdictionary.print(dOrderedPairDictionary,'downloads')
print(c1.OutputFilePathString)