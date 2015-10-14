# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 23:11:48 2014

@author: jmalinchak
"""

#for fn in os.listdir('C:\Documents and Settings\jmalinchak\My Documents\My Python\Active\downloads'):
#     if os.path.isfile(fn):
#        print(fn)
class process:
    
    def __init__(self, pathtofile):
        self.loop_through_optionsfiles(pathtofile)

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

    def loop_through_optionsfiles(self,indirectory):
        import readintomemorycreateoptioninstancesfromfilelocal
        import os  
    
        dSymbols={}    
    
        indir = indirectory #'C:\Documents and Settings\jmalinchak\My Documents\My Python\Active\downloads'
        d = {}
        i = 0
        for root, dirs, filenames in os.walk(indir):
            for f in filenames:
                print(f)
                filepath = indir + '\\' + f
                if f.split(' ',4)[0] == 'Options':
                    print('jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj')
                    d1 = readintomemorycreateoptioninstancesfromfilelocal.read(filepath)
                    # Symbol ########################################################
                    print(d1.Symbol)
                    if not d1.Symbol in dSymbols.values():
                        dSymbols[len(dSymbols)] = d1.Symbol
                    print('mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm')   
    #                print('Symbol: ' + str(d1.Symbol))                        
    #                print('QuoteDatetime: ' + str(d1.QuoteDatetime))
    #                print('Expiration Date: ' + str(d1.ExpirationDate))
    #                print('Count of BucketQuoteDatetime: ' + str(d1.BucketQuoteDatetime))
                    #print('Path To File: ' + d1.PathToFile)
    #                print('Count of PriceClassInstances: ' + str(len(d1.DictionaryOfPriceClassInstances)) + '    ' + str(d1.BucketQuoteDatetime))
    #                print('Count of OptionSymbols: ' + str(len(d1.DictionaryOfOptionSymbols)))
    #                print('Count of CallStrikes: ' + str(len(d1.DictionaryOfCallStrikes)))
    #                print('Count of PutStrikes: ' + str(len(d1.DictionaryOfPutStrikes)))
            
                    i =  i + 1
                    d[i] = d1
                
        #        for k1,v1 in d1.DictionaryOfPriceClassInstances.items():
        #            print("OptionSymbol=" + k1 + " Bid=" + v1.bid)
        self.DictionaryOfProcessedOptionsFiles = d
        self.DictionaryOfSymbols = dSymbols
        print(str(len(d)) + ' files processed.')

        
        #log = open(os.path.join(root, f),'r')