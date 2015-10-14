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
        c = self.execute_checklistener()
        super(c, self).__init__()
        
    def __init__(self):
        self.execute_checklistener()

    def execute_checklistener(self):
        import os
        import shutil
        SymbolsFile = ''
        ExpirationsFile = ''
        ListenerFileFound = 0
        #RootRemoteListener="Z:\\jm\\My Python\\Remote\\listener"
        RootRemote = os.path.join('z:','\jm','My Python','Remote')
        
        if os.path.isfile(os.path.join(RootRemote,'listener','short.txt')):
            if os.path.isfile(os.path.join(RootRemote,'inputs','SymbolsShort.txt')):
                destSymbols = os.getcwd() + '\\inputs\\SymbolsShort.txt'
                shutil.copyfile('Z:\\jm\\My Python\\Remote\\Inputs\\SymbolsShort.txt', destSymbols)
            if os.path.isfile('Z:\\jm\\My Python\\Remote\\Inputs\\ExpirationsShort.txt'):
                destExpirations = os.getcwd() + '\\inputs\\ExpirationsShort.txt'
                shutil.copyfile('Z:\\jm\\My Python\\Remote\\Inputs\\ExpirationsShort.txt', destExpirations)
            os.remove("Z:\\jm\\My Python\\Remote\\listener\\short.txt") 
            SymbolsFile = 'inputs\\SymbolsShort.txt'
            ExpirationsFile = 'inputs\\ExpirationsShort.txt'
            ListenerFileFound = 1
            
        if os.path.isfile("Z:\\jm\\My Python\\Remote\\listener\\main.txt"):
            if os.path.isfile('Z:\\jm\\My Python\\Remote\\Inputs\\SymbolsMain.txt'):
                shutil.copyfile('Z:\\jm\\My Python\\Remote\\Inputs\\SymbolsMain.txt', 'inputs\\SymbolsMain.txt')
            if os.path.isfile('Z:\\jm\\My Python\\Remote\\Inputs\\ExpirationsMain.txt'):
                shutil.copyfile('Z:\\jm\\My Python\\Remote\\Inputs\\ExpirationsMain.txt', 'inputs\\ExpirationsMain.txt')
            os.remove("Z:\\jm\\My Python\\Remote\\listener\\main.txt") 
            SymbolsFile = 'inputs\\SymbolsMain.txt'
            ExpirationsFile = 'inputs\\ExpirationsMain.txt'
            ListenerFileFound = 1
            
        if os.path.isfile("Z:\\jm\\My Python\\Remote\\listener\\run.txt"):
            os.remove("Z:\\jm\\My Python\\Remote\\listener\\run.txt") 
            SymbolsFile = 'inputs\\Symbols.txt'
            ExpirationsFile = 'inputs\\Expirations.txt'
            ListenerFileFound = 1            
            
        if ListenerFileFound == 0:
            print('no short/main/run file found')
            
        if ListenerFileFound > 0:
            print('listener file found...')
            import mytools
            datetime14 = mytools.mystrings.ConvertDatetime14()
            print(datetime14)
            #outputfilepath = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\output\\' + datetime14 + '.csv'
            import pulloptionscsvbasedoninputfiles
            pulloptionscsvbasedoninputfiles.pull(SymbolsFile,
                                             ExpirationsFile,
                                             'downloads',
                                             'output',
                                             0)
#            import strategytestnew
#            c = strategytestnew.calendarspreads(SymbolsFile,
#                                             ExpirationsFile,
#                                             'downloads',
#                                             'output',
#                                             0)
#                                             
#            outputfilepath = c.OutputFilePathString
#            print('The process create local output file: ' + outputfilepath)
#            head, tail = os.path.split(outputfilepath)
#            print('The file name only: ' + tail)
#            shutil.copyfile(outputfilepath, os.path.join(RootRemote,'output',tail))
#            return c
        #########################
        #
        return None
        #
        #########################
c = check
o = c.execute_checklistener(c)
if not o is None:
    print('The OutputFilePathString that was inherited is at: ' + o.OutputFilePathString)
    