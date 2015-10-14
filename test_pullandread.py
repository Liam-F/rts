# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 07:20:16 2014

@author: jmalinchak
"""
import os
SymbolsFile = os.getcwd() + '\\inputs\\SymbolsTest.txt'
ExpirationsFile = os.getcwd() + '\\inputs\\ExpirationsTest.txt'
DownloadsDirectory = os.getcwd() + '\\downloads'
print(DownloadsDirectory)
import pullpricessbasedonlocalinputfilestodownloaddirectorylocal
o = pullpricessbasedonlocalinputfilestodownloaddirectorylocal.pull(SymbolsFile,ExpirationsFile,)

import readpairteststrategywithcriteria 
c = readpairteststrategywithcriteria.read(o.DownloadDirectoryLocal,
                                 0.4)

