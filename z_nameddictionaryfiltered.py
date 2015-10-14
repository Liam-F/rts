# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 00:17:18 2014

@author: jmalinchak
"""
import nameddictionary #
class filter(nameddictionary):
    def __init__(self,directorylocal,Symbol,ExpirationDate,OptionType,Strike,QuoteDatetime):
        nd = self.read(directorylocal)
        return self.execute_filtering(Symbol,ExpirationDate,OptionType,Strike,QuoteDatetime)

    def set_DictionaryOfFilteredInstances(self,DictionaryOfFilteredInstances):
        self._DictionaryOfFilteredInstances = DictionaryOfFilteredInstances
    def get_DictionaryOfFilteredInstances(self):
        return self._DictionaryOfFilteredInstances
    DictionaryOfFilteredInstances = property(get_DictionaryOfFilteredInstances, set_DictionaryOfFilteredInstances)
    
    def execute_filtering(self,Symbol,ExpirationDate,OptionType,Strike,QuoteDatetime):
        dNamedDictionary = self.MainDictionariesObject.NamedDictionary
        #from datetime import datetime
        dResult = {}
        for KeyOfSymbols in dNamedDictionary.keys():
            if KeyOfSymbols == Symbol or len(Symbol) == 0:
                #print(KeyOfSymbols)
                for KeyofExpirationDates in dNamedDictionary[KeyOfSymbols].keys():
                    
#                    cdate = read.convertdate(ExpirationDate)
#                    #print(str(datetime.date(1900,1,1)))
#                    
#                    date_object = cdate
#                    if not date_object == datetime.date(1900,1,1):
#                        date_object = datetime.strptime(ExpirationDate, '%Y-%m-%d')
                    import datetime
#                    cdate = datetime.datetime.strptime(ExpirationDate, '%Y-%m-%d').date()
#                    print(cdate)
                    if KeyofExpirationDates.date() == datetime.datetime.strptime(ExpirationDate, '%Y-%m-%d').date() or len(ExpirationDate) == 0:
                        #print(KeyofExpirationDates)    
                        #print(len(dNamedDictionary[KeyOfSymbols][KeyofExpirationDates]))
                        for KeyofOptionTypes in dNamedDictionary[KeyOfSymbols][KeyofExpirationDates].keys():
                            #print(KeyofOptionTypes+' ssssssssssssssssssssssssssssss')
                            if KeyofOptionTypes == OptionType or len(OptionType) == 0:
                                #print(KeyofOptionTypes)
                                for KeyOfStrikes in dNamedDictionary[KeyOfSymbols][KeyofExpirationDates][KeyofOptionTypes].keys():
                    #                print('            ' + str(KeyOfStrikes) + ' ' + KeyofOptionTypes) 
                                    if len(Strike) == 0 or float(KeyOfStrikes) == float(Strike):
                                            for KeyOfQuoteDateTimes,ValueOfOptionInstances in dNamedDictionary[KeyOfSymbols][KeyofExpirationDates][KeyofOptionTypes][KeyOfStrikes].items():
                                                #print(KeyOfQuoteDateTimes)
                                                dResult[len(dResult)] = ValueOfOptionInstances #str(ValueOfOptionInstances.bucketquotedatetime)+ ' ' + str(ValueOfOptionInstances.quotedatetime)+ ' ' +ValueOfOptionInstances.optionsymbol + ' ' + ValueOfOptionInstances.bid
                                                #print(str(ValueOfOptionInstances.bucketquotedatetime)+ ' ' + ValueOfOptionInstances.optionsymbol + ' ' + ValueOfOptionInstances.bid)
                        #                    print('                    Bid=' + str(ValueOfOptionInstances.bid))
                        #                    print('                    Ask=' + str(ValueOfOptionInstances.ask))
                                                
        self.DictionaryOfFilteredInstances = dResult
        return self.DictionaryOfFilteredInstances