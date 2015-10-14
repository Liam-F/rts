# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 12:17:33 2014

@author: jmalinchak
"""

#class inheritedclass(initialclass):
#    def __new__(self):
#        self.attr3 = 'three'
#        super(initialclass, self).__init__()
        
class check:
    def __new__(self):
        self.attr3 = 'three'
        c = self.execute_results()
        super(c, self).__init__()

    def __init__(self):
        self.execute_results()

    def execute_results(self):
        import os
        import shutil
        SymbolsFile = ''
        ExpirationsFile = ''
        
        
        if os.path.isfile("Z:\\jm\\My Python\\Remote\\listener\\short.txt"):
            os.remove("Z:\\jm\\My Python\\Remote\\listener\\short.txt") 
            SymbolsFile = 'inputs\\SymbolsShort.txt'
            ExpirationsFile = 'inputs\\ExpirationsShort.txt'
            if os.path.isfile('Z:\\jm\\My Python\\Remote\\Input\\SymbolsShort.txt'):
                shutil.copyfile('Z:\\jm\\My Python\\Remote\\Input\\SymbolsShort.txt', 'inputs\\SymbolsShort.txt')
            if os.path.isfile('Z:\\jm\\My Python\\Remote\\Input\\ExpirationsShort.txt'):
                shutil.copyfile('Z:\\jm\\My Python\\Remote\\Input\\ExpirationShort.txt', 'inputs\\ExpirationShort.txt')
        
        if os.path.isfile("Z:\\jm\\My Python\\Remote\\listener\\main.txt"):
            os.remove("Z:\\jm\\My Python\\Remote\\listener\\main.txt") 
            SymbolsFile = 'inputs\\SymbolsMain.txt'
            ExpirationsFile = 'inputs\\ExpirationsMain.txt'
            if os.path.isfile('Z:\\jm\\My Python\\Remote\\Input\\SymbolsMain.txt'):
                shutil.copyfile('Z:\\jm\\My Python\\Remote\\Input\\SymbolsMain.txt', 'inputs\\SymbolsMain.txt')
            if os.path.isfile('Z:\\jm\\My Python\\Remote\\Input\\ExpirationsMain.txt'):
                shutil.copyfile('Z:\\jm\\My Python\\Remote\\Input\\ExpirationsMain.txt', 'inputs\\ExpirationsMain.txt')
        
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
            #outputfilepath = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\output\\' + datetime14 + '.csv'
            import strategytest
            c = strategytest.calendarspreadslive(SymbolsFile,
                                             ExpirationsFile,
                                             'downloads',
                                             'output')
                                             
            outputfilepath = strategytest.OutputFilePathString
            
            shutil.copyfile(outputfilepath, 'Z:\\jm\\My Python\\Remote\\output\\'+ datetime14 + '.csv')
            return c

o = check.execute_results()
print('Your file can be found at: ' + o.OutputFilePathString)