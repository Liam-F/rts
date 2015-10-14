# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 00:17:18 2014

@author: jmalinchak
"""
class build:
    def __init__(self, directorylocal,showresults=0):
        print('initialized class readintomemorycreatemaindictionariesfromdirectorylocal')
        self.execute_file_processing(directorylocal,showresults)

    def set_NamedDictionaries(self,NamedDictionaries):
        self._NamedDictionaries = NamedDictionaries
    def get_NamedDictionaries(self):
        return self._NamedDictionaries
    NamedDictionaries = property(get_NamedDictionaries, set_NamedDictionaries)
    
    def execute_file_processing(self,directorylocal,showresults):
        import readintomemoryprocessallfilesindirectorylocal
        #'C:\Documents and Settings\jmalinchak\My Documents\My Python\Active\downloads'
        #print('Here 1')
        ObjectOfProcessedFiles = readintomemoryprocessallfilesindirectorylocal.process(directorylocal,showresults)
        print('Here 2')
#        o = ObjectOfProcessedFiles.DictionaryOfProcessedOptionsFiles[0]
#        f1 = o.get_from_filelocal()
#        print('********************************A')
#        print(f1.bucketquotedatetime)
#        print('********************************A')
        
        if showresults == 1:
            print('111111 readintomemorycreatemaindictionariesfromdirectorylocal.py 111111')

        #print('Count of Symbols= ' + str(len(ObjectOfProcessedFiles.DictionaryOfSymbols)))
        # *************************************************************************************************
        # if filename is prefixed with "Options":
        # *************************************************************************************************
        dProcessedOptionsFiles = ObjectOfProcessedFiles.DictionaryOfProcessedOptionsFiles
        #print('Count of DictionaryOfProcessedOptionsFiles= ' + str(len(dProcessedOptionsFiles)))
        
        dNamedDictionaries = {}
#        dOptionsBySymbol = {}                    
#        dOptionsBySymbolExpirationDate = {}
#        dOptionsBySymbolExpirationDateOptionType = {}
#        dOptionsBySymbolExpirationDateOptionTypeStrike = {}
#        dOptionsBySymbolExpirationDateOptionTypeStrikeBucketQuoteDatetime = {}
        iInstancesFound = 0
        iInstancesLoaded = 0
#        print(str(len(dProcessedOptionsFiles)) + ' items processing via readintomemorycreatemaindictionariesfromdirectorylocal.py')
        #print('Here 2?')
        for kProcessedOptionsFiles,vProcessedOptionsFiles in dProcessedOptionsFiles.items():
            #                                             print(vProcessedOptionsFiles.Symbol + ' ' + str(vProcessedOptionsFiles.ExpirationDate) + ' ' + str(vProcessedOptionsFiles.BucketQuoteDatetime))
        
            if not vProcessedOptionsFiles.Symbol in dNamedDictionaries.keys():
                dNamedDictionaries[vProcessedOptionsFiles.Symbol] = {}
            #dNamedDictionaries[vProcessedOptionsFiles.Symbol] = vProcessedOptionsFiles.Symbol 
            
            if not vProcessedOptionsFiles.ExpirationDate in dNamedDictionaries[vProcessedOptionsFiles.Symbol].keys():
                dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate] = {}
            #dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate] = vProcessedOptionsFiles.ExpirationDate
            
#            if not vProcessedOptionsFiles.OptionType in dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate].keys():
#                dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate][vProcessedOptionsFiles.OptionType] = {}
            #dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate]['C'] = ['C']
            iInstancesFound = iInstancesFound + len(vProcessedOptionsFiles.DictionaryOfOptionInstances)
            for KeyOfTwoValueTuple,ValueOfOptionInstances in vProcessedOptionsFiles.DictionaryOfOptionInstances.items():
                #print(KeyOfTwoValueTuple)
                if not KeyOfTwoValueTuple[1] in dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate].keys():
                    dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate][KeyOfTwoValueTuple[1]] = {}
                #for KeyOfStrikes in dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate][KeyOfTwoValueTuple[1]].keys():
                if not KeyOfTwoValueTuple[0] in dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate][KeyOfTwoValueTuple[1]].keys():
                    #print(KeyOfTwoValueTuple[0])
                    dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate][KeyOfTwoValueTuple[1]][KeyOfTwoValueTuple[0]] = {}
                if not ValueOfOptionInstances.bucketquotedatetime in dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate][KeyOfTwoValueTuple[1]][KeyOfTwoValueTuple[0]].keys():
                    dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate][KeyOfTwoValueTuple[1]][KeyOfTwoValueTuple[0]][ValueOfOptionInstances.bucketquotedatetime] = ValueOfOptionInstances #vProcessedOptionsFiles.DictionaryOfOptionInstances[KeyOfTwoValueTuple[0],[KeyOfTwoValueTuple[1]]]
                    iInstancesLoaded = iInstancesLoaded + 1
                    #print(ValueOfOptionInstances.bucketquotedatetime)
                    #dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate][KeyOfTwoValueTuple[1]][ValueOfOptionInstances][vProcessedOptionsFiles.BucketQuoteDatetime] = vProcessedOptionsFiles.DictionaryOfOptionInstances[ValueOfOptionInstances,[KeyOfTwoValueTuple[1]]]
        print(str(iInstancesFound),'instances found.')
        print(str(iInstancesLoaded),'loaded.')
        self.NamedDictionaries = dNamedDictionaries

#            for KeyOfTwoValueTuple,ValueOfOptionInstances in vProcessedOptionsFiles.DictionaryOfOptionInstances.items():
#                if not KeyOfTwoValueTuple[1] in dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate].keys():
#                    dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate][KeyOfTwoValueTuple] = {}
#                if not ValueOfOptionInstances in dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate][KeyOfTwoValueTuple].keys():
#                    dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate][KeyOfTwoValueTuple][vProcessedOptionsFiles.BucketQuoteDatetime] = vProcessedOptionsFiles.DictionaryOfOptionInstances[KeyOfTwoValueTuple]
               

#            for KeyOfCallStrikes,ValueOfCallStrikes in vProcessedOptionsFiles.DictionaryOfCallStrikes.items():
#                if not ValueOfCallStrikes in dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate]['C'].keys():
#                    dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate]['C'][ValueOfCallStrikes] = {}            
#                    if not vProcessedOptionsFiles.BucketQuoteDatetime in dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate]['C'][ValueOfCallStrikes].keys():
#                        #optionsymbol = 'QQQ141122C00086500'
#                        #dOptionsBySymbol[vProcessedOptionsFiles.Symbol,len(dOptionsBySymbol)] = vProcessedOptionsFiles.DictionaryOfOptionInstances[ValueOfCallStrikes,'C']
#                        dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate]['C'][ValueOfCallStrikes][vProcessedOptionsFiles.BucketQuoteDatetime] = vProcessedOptionsFiles.DictionaryOfOptionInstances[ValueOfCallStrikes,'C']
#                        
#            #    dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate]['C'][ValueOfCallStrikes] = ValueOfCallStrikes
#            #    dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate]['C'][ValueOfCallStrikes][vProcessedOptionsFiles.BucketQuoteDatetime] = vProcessedOptionsFiles.BucketQuoteDatetime
#          
#            for KeyOfPutStrikes,ValueOfPutStrikes in vProcessedOptionsFiles.DictionaryOfPutStrikes.items():
#                if not ValueOfPutStrikes in dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate]['P'].keys():
#                    dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate]['P'][ValueOfPutStrikes] = {}
#                    if not vProcessedOptionsFiles.BucketQuoteDatetime in dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate]['P'][ValueOfPutStrikes].keys():
#                        dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate]['P'][ValueOfPutStrikes][vProcessedOptionsFiles.BucketQuoteDatetime] = vProcessedOptionsFiles.DictionaryOfOptionInstances[ValueOfPutStrikes,'P']
#            #    dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate]['P'][ValueOfPutStrikes] = ValueOfPutStrikes
#            #    dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate]['P'][ValueOfPutStrikes][vProcessedOptionsFiles.BucketQuoteDatetime] = vProcessedOptionsFiles.BucketQuoteDatetime
    
        
#        for KeyOfSymbols in dNamedDictionaries.keys():
#            print(KeyOfSymbols)
#            for KeyofExpirationDates in dNamedDictionaries[KeyOfSymbols].keys():
#                print('    ' + str(KeyofExpirationDates))
#                for KeyofOptionTypes in dNamedDictionaries[KeyOfSymbols][KeyofExpirationDates].keys():
#                    print('        ' + str(KeyofOptionTypes))
#                    for KeyOfStrikes in dNamedDictionaries[KeyOfSymbols][KeyofExpirationDates][KeyofOptionTypes].keys():
#                        print('            ' + str(KeyOfStrikes) + ' ' + KeyofOptionTypes) 
#                        for KeyOfQuoteDateTimes,ValueOfQuoteDateTimes in dNamedDictionaries[KeyOfSymbols][KeyofExpirationDates][KeyofOptionTypes][KeyOfStrikes].items():
#                            print('                ' + str(KeyOfQuoteDateTimes))
#                            print('                    Bid=' + str(ValueOfQuoteDateTimes.bid))
#                            print('                    Ask=' + str(ValueOfQuoteDateTimes.ask))

#        for KeyOfSymbols in dNamedDictionaries.keys():
#            #print(KeyOfSymbols)
#            for KeyofExpirationDates in dNamedDictionaries[KeyOfSymbols].keys():
#                #print('    ' + str(KeyofExpirationDates))
#                for KeyofOptionTypes in dNamedDictionaries[KeyOfSymbols][KeyofExpirationDates].keys():
#                    #print('        ' + str(KeyofOptionTypes))
#                    for KeyOfStrikes in dNamedDictionaries[KeyOfSymbols][KeyofExpirationDates][KeyofOptionTypes].keys():
#                        #print('            ' + str(KeyOfStrikes) + ' ' + KeyofOptionTypes) 
#                        for KeyOfBucketQuoteDateTimes,ValueOfBucketQuoteDateTimes in dNamedDictionaries[KeyOfSymbols][KeyofExpirationDates][KeyofOptionTypes][KeyOfStrikes].items():
#                            print('                ' + str(KeyOfBucketQuoteDateTimes))

