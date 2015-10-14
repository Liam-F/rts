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
        destSymbols = ''
        destExpirations = ''
        
        ListenerFileFound = 0
        #RootRemoteListener="Z:\\jm\\My Python\\Remote\\listener"
        RootRemote = os.path.join('z:','\jm','My Python','Inputs')
        
        sourceSymbols = os.path.join(RootRemote,'SymbolsListener.txt')
        destSymbols = os.getcwd() + '\\inputs\\quad\\SymbolsListener.txt'
        if os.path.isfile(sourceSymbols):
            shutil.copyfile(sourceSymbols, destSymbols)
            ListenerFileFound = ListenerFileFound + 1
        sourceExpirations = os.path.join(RootRemote,'ExpirationsListener.txt')
        destExpirations = os.getcwd() + '\\inputs\\quad\\ExpirationsListener.txt'
        if os.path.isfile(sourceExpirations):
            shutil.copyfile(sourceExpirations, destExpirations)
            ListenerFileFound = ListenerFileFound + 1
                        
        if ListenerFileFound == 2:
            print('listener file found...')
            import mytools
            datetime14 = mytools.mystrings.ConvertDatetime14()
            print(datetime14)

            import pulloptionscsvbasedoninputfiles
            
            opulled = pulloptionscsvbasedoninputfiles.pull(destSymbols,
                                             destExpirations,
                                             'downloadsquad',
                                             0)
                                             
            pulledcsvfilepath = opulled.OutputPathString
            print(pulledcsvfilepath)
        
            import serializecsvfilestoxmlcandidatequads
            
            serializecsvfilestoxmlcandidatequads.read(downloadsdirectory = 'downloadsquad',
                             replacelistforcreatingdestinationpath = ['\\downloadsquad\\','\\downloadsquadprocessed\\'],
                             minpairspreadpercent = .64,
                             maxvalueatrisk = 1.5,
                             maxbidaskspreadpercentagesell = .25,
                             maxbidaskspreadpercentagebuy = .25,
                             showresults=1)                
        
        
        return None
        
        #########################
        #
        #########################

c = check
o = c.execute_checklistener(c)
if not o is None:
    print('The OutputFilePathString that was inherited is at: ' + o.OutputFilePathString)
    