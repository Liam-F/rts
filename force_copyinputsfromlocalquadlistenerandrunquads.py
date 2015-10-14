# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 12:17:33 2014

@author: jmalinchak
"""

#class inheritedclass(initialclass):
#    def __new__(self):
#        self.attr3 = 'three'
#        super(initialclass, self).__init__()
        
class force:
    def __new__(self):
        self.attr3 = 'three'
        c = self.execute_forcequadlistener()
        super(c, self).__init__()
        
    def __init__(self):
        self.execute_forcequadlistener()

    def execute_forcequadlistener(self):
        import os
        import shutil
        import ntpath
        
        destSymbols = ''
        destExpirations = ''
        
        RootWebServer = os.path.join('c:','\Inetpub','wwwroot','rtstock','calendarspreadquads')        
        #RootWebServer = os.path.join('x:','\www','rtstock','calendarspreadquads')        
        import mytools
        mytools.general.make_sure_path_exists(RootWebServer)
        
        
        InputFilesFound = 0
        
        RootInputs = os.path.join('C:','\Documents and Settings','jmalinchak','My Documents','My Python','Active','py','inputs','quad')
        #RootInputs = os.path.join('z:','\jm','My Python','Active','py','Inputs','quad')
        
        print('RootInputs=',RootInputs)
        
        sourceSymbols = os.path.join(RootInputs,'SymbolsListener.txt')
        print('sourceSymbols=',sourceSymbols)
        
        destSymbols = os.path.join(os.getcwd(),'inputs','quad','SymbolsListener.txt')
        print('destSymbols=',destSymbols)
        if os.path.isfile(sourceSymbols) and sourceSymbols.casefold() != destSymbols.casefold():
            shutil.copyfile(sourceSymbols, destSymbols)

        sourceExpirations = os.path.join(RootInputs,'ExpirationsListener.txt')
        print('sourceExpirations=',sourceExpirations)
        destExpirations = os.getcwd() + '\\inputs\\quad\\ExpirationsListener.txt'        
        print('destExpirations=',destExpirations)
        if os.path.isfile(sourceExpirations) and sourceExpirations.casefold() != destExpirations.casefold():
            shutil.copyfile(sourceExpirations, destExpirations)

        if os.path.isfile(destSymbols):
            InputFilesFound = InputFilesFound + 1
            
        if os.path.isfile(destExpirations):
            InputFilesFound = InputFilesFound + 1
            
        print('InputFilesFound=',InputFilesFound)
        
        if InputFilesFound == 2:
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
            
            oserializexmls = serializecsvfilestoxmlcandidatequads.read(downloadsdirectory = 'downloadsquad',
                             replacelistforcreatingdestinationpath = ['\\downloadsquad\\','\\downloadsquadprocessed\\'],
                             minpairspreadpercent = .64,
                             maxvalueatrisk = 1.5,
                             maxbidaskspreadpercentagesell = .25,
                             maxbidaskspreadpercentagebuy = .25,
                             showresults=1)     
                             
            d1 = oserializexmls.DictionaryOfSerializedQuadCandidateXMLPathNames
            #print('len(serializecsvfilestoxmlcandidatequads.read.DictionaryOfSerializedQuadCandidateXMLPathNames)',len(serializecsvfilestoxmlcandidatequads.read.DictionaryOfSerializedQuadCandidateXMLPathNames))
            for k,vFilePath in d1.items():
                print('XmlFile',k,'=',vFilePath)
                head, tail = ntpath.split(vFilePath)
                SymbolFromFilename = tail.split(' ')[1]
                destXMLFile = os.path.join(RootWebServer,SymbolFromFilename + '.xml')
                print('destXMLFile=',destXMLFile)
                print(SymbolFromFilename)
                if os.path.isfile(vFilePath):
                    shutil.copyfile(vFilePath, destXMLFile)
                    
            print('RootWebServer',RootWebServer)
        return None
        
        #########################
        #
        #########################

c = force
o = c.execute_forcequadlistener(c)
if not o is None:
    print('The OutputFilePathString that was inherited is at: ' + o.OutputFilePathString)
    