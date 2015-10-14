# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 11:31:27 2014

@author: jmalinchak
"""
import os

SymbolsFile = os.getcwd() + '\\inputs\\SymbolsShort.txt'
ExpirationsFile = os.getcwd() + '\\inputs\\ExpirationsShort.txt'
#DownloadsRoot = 'downloads\\2014-12-21\\11\\30'
DownloadsRoot = 'downloads\\2014-12-25\\12\\15'
import readintomemorystrategytest
c = readintomemorystrategytest.read(SymbolsFile,
                                 ExpirationsFile,
                                 DownloadsRoot,
                                 'output',
                                 0)
                                 
outputfilepath = c.OutputFilePathString
print('The process create local output file: ' + outputfilepath)