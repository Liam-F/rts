# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 23:11:48 2014

@author: jmalinchak
"""

#for fn in os.listdir('C:\Documents and Settings\jmalinchak\My Documents\My Python\Active\downloads'):
#     if os.path.isfile(fn):
#        print(fn)
class process:
    
    def __init__(self, topdirectory,showresults):
        print('initialized class readintomemoryprocessallfilesindirectorylocal')
        if showresults == 1:
            print('showresults=' + str(showresults) + ' readintomemoryprocessallfilesindirectorylocal')
        #self.loop_through_optionsfiles(topdirectory)
        
        self.loop_through_subdirectories(topdirectory,showresults)

    def set_DictionaryOfSymbols(self,DictionaryOfSymbols):
        self._DictionaryOfSymbols = DictionaryOfSymbols
    def get_DictionaryOfSymbols(self):
        return self._DictionaryOfSymbols
    DictionaryOfSymbols = property(get_DictionaryOfSymbols, set_DictionaryOfSymbols)

    def set_CountOfFilesFoundUnderTopDirectory(self,CountOfFilesFoundUnderTopDirectory):
        self._CountOfFilesFoundUnderTopDirectory = CountOfFilesFoundUnderTopDirectory
    def get_CountOfFilesFoundUnderTopDirectory(self):
        return self._CountOfFilesFoundUnderTopDirectory
    CountOfFilesFoundUnderTopDirectory = property(get_CountOfFilesFoundUnderTopDirectory, set_CountOfFilesFoundUnderTopDirectory)

    def set_DictionaryOfProcessedOptionsFiles(self,DictionaryOfProcessedOptionsFiles):
        self._DictionaryOfProcessedOptionsFiles = DictionaryOfProcessedOptionsFiles
    def get_DictionaryOfProcessedOptionsFiles(self):
        return self._DictionaryOfProcessedOptionsFiles
    DictionaryOfProcessedOptionsFiles = property(get_DictionaryOfProcessedOptionsFiles, set_DictionaryOfProcessedOptionsFiles)

    def loop_through_subdirectories(self,topdirectory,showresults):
        print('Looping through subdirectories on ' + topdirectory)
        
        if showresults==1:
            print('111111 \ 111111')
        #import readintomemorycreateoptioninstancesfromfilelocal        
        import os
        self.DictionaryOfSymbols={}            
        self.DictionaryOfProcessedOptionsFiles = {}
        
        #from os.path import join
        print('---------')
        print('     ' + 'processing files in: ' )
        print('     ' )
        print('     ' + topdirectory)
        print('     ' )
        print('-- ------------------------------------------------')
        print('--','readintomemoryprocessallfilesindirectorylocal.py')
        print('--','--', 'read_option_file')
        print('--','--', '--',topdirectory)
        for (topdirectory, dirs, files) in os.walk(topdirectory):
            if showresults == 1:
                print('here 1')
            self.CountOfFilesFoundUnderTopDirectory = len(files)
            for pathfilename in files:
                if showresults == 1:
                    print('here 2')
                if pathfilename[:7] == 'Options' :
                    if showresults == 1:
                        print('here 3')
                    pathfilename = os.path.join(topdirectory,pathfilename)
                    if showresults == 1:
                        print('===','processing:',pathfilename)
                    self.read_option_file(pathfilename,showresults)
                    
#
#                    if showresults==1:
#                        print('222222 readintomemoryprocessallfilesindirectorylocal.loop_through_subdirectories 2222222')
#                        print('pathfilename='+pathfilename)
#                        
#                    ObjectRepresentingEntireOptionFile = readintomemorycreateoptioninstancesfromfilelocal.read(pathfilename,showresults)
#                    if showresults==1:
#                        print('333333 readintomemoryprocessallfilesindirectorylocal.loop_through_subdirectories 333333')
#                        if ObjectRepresentingEntireOptionFile.HasError == 1:
#                            print('444444 readintomemoryprocessallfilesindirectorylocal.YES errors 444444')
#                    if ObjectRepresentingEntireOptionFile.HasError == 0:
#                        if showresults==1:
#                            print('444444 readintomemoryprocessallfilesindirectorylocal=NO errors 444444')
#
#                        if not ObjectRepresentingEntireOptionFile.Symbol in dSymbols.values():
#                            dSymbols[len(dSymbols)] = ObjectRepresentingEntireOptionFile.Symbol
#                        
#                        d[len(d)] = ObjectRepresentingEntireOptionFile
                
        #self.DictionaryOfProcessedOptionsFiles = d
        #self.DictionaryOfSymbols = dSymbols
        #print(str(len(d)) + ' files processed via readintomemoryprocessallfilesindirectorylocal, please wait...')

    def path_leaf(self,path):
        import ntpath
        head, tail = ntpath.split(path)
        return tail or ntpath.basename(head)
        
    def read_option_file(self,pathfilename,showresults):

        if showresults==1:
            print('111111 readintomemoryprocessallfilesindirectorylocal.read_option_file')
            
        import readintomemorycreateoptioninstancesfromfilelocal        
        
        dSymbols=self.DictionaryOfSymbols
        d = self.DictionaryOfProcessedOptionsFiles
        if showresults==1:
            print("000000",'current count',len(d))        
            print('11111X',pathfilename)
            
        filename = self.path_leaf(pathfilename)
        countofoptioninstances = 0
        if showresults==1:
            print(filename)
        if filename[:7] == 'Options' :
            if showresults==1:
                print('11111Y')
            #pathfilename = pathfilename #os.path.join(topdirectory,pathfilename)
            
            if showresults==1:
                print('222222 readintomemoryprocessallfilesindirectorylocal.loop_through_subdirectories 2222222')
#____________________________
#               showresults = 1
#____________________________
            ObjectRepresentingEntireOptionFile = readintomemorycreateoptioninstancesfromfilelocal.read(pathfilename,showresults)
            
            
            if showresults==1:
                print('333333 readintomemoryprocessallfilesindirectorylocal.loop_through_subdirectories 333333')
                if ObjectRepresentingEntireOptionFile.HasError == 1:
                    print('444444 readintomemoryprocessallfilesindirectorylocal.YES errors 444444')
            if ObjectRepresentingEntireOptionFile.HasError == 0:
                countofoptioninstances = len(ObjectRepresentingEntireOptionFile.DictionaryOfOptionInstances)
                if showresults==1:
                    print('444444 readintomemoryprocessallfilesindirectorylocal=NO errors 444444')

                if not ObjectRepresentingEntireOptionFile.Symbol in dSymbols.values():
                    dSymbols[len(dSymbols)] = ObjectRepresentingEntireOptionFile.Symbol
                
                d[len(d)] = ObjectRepresentingEntireOptionFile
                
        self.DictionaryOfProcessedOptionsFiles = d
        self.DictionaryOfSymbols = dSymbols
        
        print('--','--', '--','--',str(len(d)),'of',self.CountOfFilesFoundUnderTopDirectory,'files processed',filename,str(countofoptioninstances) + ' instances')
        
            
