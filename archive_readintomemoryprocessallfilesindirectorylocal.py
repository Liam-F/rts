# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 23:11:48 2014

@author: jmalinchak
"""

#for fn in os.listdir('C:\Documents and Settings\jmalinchak\My Documents\My Python\Active\downloads'):
#     if os.path.isfile(fn):
#        print(fn)
class process:
    
    def __init__(self, pathtofile,showresults=0):
        print('initialized class readintomemoryprocessallfilesindirectorylocal')
        if showresults == 1:
            print('showresults=' + str(showresults) + ' readintomemoryprocessallfilesindirectorylocal')
        #self.loop_through_optionsfiles(pathtofile)
        self.loop_through_subdirectories(pathtofile,showresults)

    def set_DictionaryOfSymbols(self,DictionaryOfSymbols):
        self._DictionaryOfSymbols = DictionaryOfSymbols
    def get_DictionaryOfSymbols(self):
        return self._DictionaryOfSymbols
    DictionaryOfSymbols = property(get_DictionaryOfSymbols, set_DictionaryOfSymbols)

    def set_DictionaryOfProcessedOptionsFiles(self,DictionaryOfProcessedOptionsFiles):
        self._DictionaryOfProcessedOptionsFiles = DictionaryOfProcessedOptionsFiles
    def get_DictionaryOfProcessedOptionsFiles(self):
        return self._DictionaryOfProcessedOptionsFiles
    DictionaryOfProcessedOptionsFiles = property(get_DictionaryOfProcessedOptionsFiles, set_DictionaryOfProcessedOptionsFiles)


    def loop_through_subdirectories(self,topdirectory,showresults):
        print('Looping through subdirectories on ' + topdirectory)
        
        if showresults==1:
            print('111111 readintomemoryprocessallfilesindirectorylocal.loop_through_subdirectories 111111')
        import readintomemorycreateoptioninstancesfromfilelocal        
        import os
        dSymbols={}            
        d = {}
        
        #from os.path import join
        print('---------')
        print('     ' + 'processing files in: ' )
        print('     ' )
        print('     ' + topdirectory)
        print('     ' )
        print('---------')
        for (topdirectory, dirs, files) in os.walk(topdirectory):
            if showresults == 1:
                print('here 1')
            for filename in files:
                if showresults == 1:
                    print('here 2')
                if filename[:7] == 'Options' :
                    if showresults == 1:
                        print('here 3')
                    filepath = os.path.join(topdirectory,filename)
                    
                    if showresults==1:
                        print('222222 readintomemoryprocessallfilesindirectorylocal.loop_through_subdirectories 2222222')
                        print('filepath='+filepath)
                        
                    ObjectRepresentingEntireOptionFile = readintomemorycreateoptioninstancesfromfilelocal.read(filepath,showresults)
                    if showresults==1:
                        print('333333 readintomemoryprocessallfilesindirectorylocal.loop_through_subdirectories 333333')
                        if ObjectRepresentingEntireOptionFile.HasError == 1:
                            print('444444 readintomemoryprocessallfilesindirectorylocal.YES errors 444444')
                    if ObjectRepresentingEntireOptionFile.HasError == 0:
                        if showresults==1:
                            print('444444 readintomemoryprocessallfilesindirectorylocal=NO errors 444444')

                        if not ObjectRepresentingEntireOptionFile.Symbol in dSymbols.values():
                            dSymbols[len(dSymbols)] = ObjectRepresentingEntireOptionFile.Symbol
                        
                        d[len(d)] = ObjectRepresentingEntireOptionFile
                
        self.DictionaryOfProcessedOptionsFiles = d
        self.DictionaryOfSymbols = dSymbols
        print(str(len(d)) + ' files processed via readintomemoryprocessallfilesindirectorylocal, please wait...')
        

        #log = open(os.path.join(root, f),'r')

#    def loop_through_optionsfiles(self,indirectory,showresults):
#        print('Looping through options files, please wait...')
#        try:
#            print('111111 readintomemoryprocessallfilesindirectorylocal.loop_through_optionsfiles 111111')
#            import readintomemorycreateoptioninstancesfromfilelocal
#            import os  
#        
#            dSymbols={}    
#        
#            indir = indirectory #'C:\Documents and Settings\jmalinchak\My Documents\My Python\Active\downloads'
#            d = {}
#            i = 0
#            for root, dirs, filenames in os.walk(indir):
#                for f in filenames:
#                    if showresults == 1:
#                        print('2222222 readintomemoryprocessallfilesindirectorylocal,filepath='+ f + ' 2222222')                    #print(f)
#                    filepath = indir + '\\' + f
#                    if f.split(' ',4)[0] == 'Options':
#                        #print('jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj')
#                        if showresults == 1:
#                            print('readintomemorycreateoptioninstancesfromfilelocal,filepath='+filepath)
#                        d1 = readintomemorycreateoptioninstancesfromfilelocal.read(filepath)
#                        
#                        # Symbol ########################################################
#                        #print(d1.Symbol)
#                        print(len(d1.DictionaryOfOptionInstances))
#                        
#                        if not d1.Symbol in dSymbols.values():
#                            print('rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr')
#                            print(d1.Symbol)
#                            dSymbols[len(dSymbols)] = d1.Symbol
#    
#                
#                        i =  i + 1
#                        d[i] = d1
#                    
#            #        for k1,v1 in d1.DictionaryOfPriceClassInstances.items():
#            #            print("OptionSymbol=" + k1 + " Bid=" + v1.bid)
#            self.DictionaryOfProcessedOptionsFiles = d
#            self.DictionaryOfSymbols = dSymbols
#            print(str(len(d)) + ' files processed.')
#        except ValueError as e:
#            print(str(e))
#        except Exception as e:
#            print('there was an error')
#        finally:
#            print('complete')