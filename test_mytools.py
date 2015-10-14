# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 11:52:57 2014

@author: jmalinchak
"""

import mytools
mydirectory = mytools.mystrings.appendnormaldateddirectorybasedoncurrenttime15("C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\downloads")
print(mydirectory)
import shutil
shutil.rmtree(mydirectory, ignore_errors=True)

################################################    
import pulllpricesallfromdirectorylocalroot
pulllpricesallfromdirectorylocalroot.pull(mydirectory,
                                          'inputs\\SymbolsShort.txt',
                                          'inputs\\ExpirationsShort.txt')
################################################
