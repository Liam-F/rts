# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 11:31:27 2014

@author: jmalinchak
"""
import os

SymbolsFile = os.getcwd() + '\\inputs\\SymbolsShort.txt'
ExpirationsFile = os.getcwd() + '\\inputs\\ExpirationsShort.txt'
#DownloadsRoot = 'downloads\\2014-12-21\\11\\30'
DownloadsRoot = 'downloads\\2014-12-25\\11\\30'
import readintomemorystrategytestonstraddlingearningsdate
c = readintomemorystrategytestonstraddlingearningsdate.read(SymbolsFile,
                                 ExpirationsFile,
                                 DownloadsRoot,
                                 '2015-02-04',
                                 'output',
                                 0)
                                 
#outputfilepath = c.OutputFilePathString
#print('The process create local output file: ' + outputfilepath)