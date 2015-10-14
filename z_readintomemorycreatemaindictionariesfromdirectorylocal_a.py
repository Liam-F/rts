# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 00:17:18 2014

@author: jmalinchak
"""
class build:
    def __init__(self, directorylocal):
        print('22222222222222222222222222222222222')
        self.execute_file_processing(directorylocal)

    def set_NamedDictionaries(self,NamedDictionaries):
        self._NamedDictionaries = NamedDictionaries
    def get_NamedDictionaries(self):
        return self._NamedDictionaries
    NamedDictionaries = property(get_NamedDictionaries, set_NamedDictionaries)
    
    def execute_file_processing(self,directorylocal):
        print('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')                
        import readintomemoryprocessallfilesindirectorylocal
        print('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')
        #'C:\Documents and Settings\jmalinchak\My Documents\My Python\Active\downloads'
        ObjectOfProcessedFiles = readintomemoryprocessallfilesindirectorylocal.process(directorylocal)
        
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
        
        for kProcessedOptionsFiles,vProcessedOptionsFiles in dProcessedOptionsFiles.items():
            #                                             print(vProcessedOptionsFiles.Symbol + ' ' + str(vProcessedOptionsFiles.ExpirationDate) + ' ' + str(vProcessedOptionsFiles.BucketQuoteDatetime))
        
            if not vProcessedOptionsFiles.Symbol in dNamedDictionaries.keys():
                dNamedDictionaries[vProcessedOptionsFiles.Symbol] = {}
            #dNamedDictionaries[vProcessedOptionsFiles.Symbol] = vProcessedOptionsFiles.Symbol 
            
            if not vProcessedOptionsFiles.ExpirationDate in dNamedDictionaries[vProcessedOptionsFiles.Symbol].keys():
                dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate] = {}
            #dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate] = vProcessedOptionsFiles.ExpirationDate
            
            if not 'C' in dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate].keys():
                dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate]['C'] = {}
            #dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate]['C'] = ['C']
            
            if not 'P' in dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate].keys():
                dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate]['P'] = {}   
            #dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate]['P'] = ['P']
            
            for KeyOfCallStrikes,ValueOfCallStrikes in vProcessedOptionsFiles.DictionaryOfCallStrikes.items():
                if not ValueOfCallStrikes in dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate]['C'].keys():
                    dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate]['C'][ValueOfCallStrikes] = {}            
                    if not vProcessedOptionsFiles.BucketQuoteDatetime in dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate]['C'][ValueOfCallStrikes].keys():
                        #optionsymbol = 'QQQ141122C00086500'
                        #dOptionsBySymbol[vProcessedOptionsFiles.Symbol,len(dOptionsBySymbol)] = vProcessedOptionsFiles.DictionaryOfContentsByStrikeAndOptionType[ValueOfCallStrikes,'C']
                        dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate]['C'][ValueOfCallStrikes][vProcessedOptionsFiles.BucketQuoteDatetime] = vProcessedOptionsFiles.DictionaryOfContentsByStrikeAndOptionType[ValueOfCallStrikes,'C']
                        
            #    dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate]['C'][ValueOfCallStrikes] = ValueOfCallStrikes
            #    dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate]['C'][ValueOfCallStrikes][vProcessedOptionsFiles.BucketQuoteDatetime] = vProcessedOptionsFiles.BucketQuoteDatetime
          
            for KeyOfPutStrikes,ValueOfPutStrikes in vProcessedOptionsFiles.DictionaryOfPutStrikes.items():
                if not ValueOfPutStrikes in dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate]['P'].keys():
                    dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate]['P'][ValueOfPutStrikes] = {}
                    if not vProcessedOptionsFiles.BucketQuoteDatetime in dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate]['P'][ValueOfPutStrikes].keys():
                        dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate]['P'][ValueOfPutStrikes][vProcessedOptionsFiles.BucketQuoteDatetime] = vProcessedOptionsFiles.DictionaryOfContentsByStrikeAndOptionType[ValueOfPutStrikes,'P']
            #    dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate]['P'][ValueOfPutStrikes] = ValueOfPutStrikes
            #    dNamedDictionaries[vProcessedOptionsFiles.Symbol][vProcessedOptionsFiles.ExpirationDate]['P'][ValueOfPutStrikes][vProcessedOptionsFiles.BucketQuoteDatetime] = vProcessedOptionsFiles.BucketQuoteDatetime
    
        
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

        self.NamedDictionaries = dNamedDictionaries