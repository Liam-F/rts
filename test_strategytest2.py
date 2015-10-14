# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 12:17:33 2014

@author: jmalinchak
"""
import os
import shutil
SymbolsFile = ''
ExpirationsFile = ''

SymbolsFile = 'inputs\\SymbolsShort.txt'
ExpirationsFile = 'inputs\\ExpirationsShort.txt'

if os.path.isfile("Z:\\jm\\My Python\\Remote\\listener\\main.txt"):
    os.remove("Z:\\jm\\My Python\\Remote\\listener\\main.txt") 
    SymbolsFile = 'inputs\\SymbolsMain.txt'
    ExpirationsFile = 'inputs\\ExpirationsMain.txt'

if os.path.isfile("Z:\\jm\\My Python\\Remote\\listener\\run.txt"):
    os.remove("Z:\\jm\\My Python\\Remote\\listener\\run.txt") 
    SymbolsFile = 'inputs\\Symbols.txt'
    ExpirationsFile = 'inputs\\Expirations.txt'
    
if len(SymbolsFile) == 0:
    print('no short/main/run file found')
    
if len(SymbolsFile) > 0:
    import mytools
    datetime14 = mytools.mystrings.ConvertDatetime14()
    print(datetime14)
    outputfilepath = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\output\\' + datetime14 + '.csv'
    import strategytest
    strategytest.calendarspreadslive('C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\downloads',
                                     outputfilepath,
                                     SymbolsFile,
                                     ExpirationsFile)
    
    
    shutil.copyfile(outputfilepath, 'Z:\\jm\\My Python\\Remote\\output\\'+ datetime14 + '.csv')
