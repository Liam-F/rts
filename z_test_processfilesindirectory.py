# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 00:17:18 2014

@author: jmalinchak
"""

import buildnameddictionariesfromdirectory

NameDictionariesObject = buildnameddictionariesfromdirectory.build('C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\Active\\downloads\\a20141129')
dNamedDictionaries = NameDictionariesObject.NamedDictionaries

#for KeyOfSymbols in dNamedDictionaries.keys():
#    print(KeyOfSymbols)
#    for KeyofExpirationDates in dNamedDictionaries[KeyOfSymbols].keys():
#        print('    ' + str(KeyofExpirationDates))
#        for KeyofOptionTypes in dNamedDictionaries[KeyOfSymbols][KeyofExpirationDates].keys():
#            print('        ' + str(KeyofOptionTypes))
#            for KeyOfStrikes in dNamedDictionaries[KeyOfSymbols][KeyofExpirationDates][KeyofOptionTypes].keys():
#                print('            ' + str(KeyOfStrikes) + ' ' + KeyofOptionTypes) 
#                for KeyOfQuoteDateTimes,ValueOfQuoteDateTimes in dNamedDictionaries[KeyOfSymbols][KeyofExpirationDates][KeyofOptionTypes][KeyOfStrikes].items():
#                    print('                ' + str(KeyOfQuoteDateTimes))
#                    print('                    Bid=' + str(ValueOfQuoteDateTimes.bid))
#                    print('                    Ask=' + str(ValueOfQuoteDateTimes.ask))

from datetime import datetime
for KeyOfSymbols in dNamedDictionaries.keys():
    if KeyOfSymbols == 'HPQ':
        for KeyofExpirationDates in dNamedDictionaries[KeyOfSymbols].keys():
            
            date_object = datetime.strptime('2014-12-12', '%Y-%m-%d')
            
            if KeyofExpirationDates == date_object:
        #        print('    ' + str(KeyofExpirationDates))
                for KeyofOptionTypes in dNamedDictionaries[KeyOfSymbols][KeyofExpirationDates].keys():
        #            print('        ' + str(KeyofOptionTypes))
                    for KeyOfStrikes in dNamedDictionaries[KeyOfSymbols][KeyofExpirationDates][KeyofOptionTypes].keys():
        #                print('            ' + str(KeyOfStrikes) + ' ' + KeyofOptionTypes) 
                        if float(KeyOfStrikes) == float('38.5'):
                            for KeyOfQuoteDateTimes,ValueOfQuoteDateTimes in dNamedDictionaries[KeyOfSymbols][KeyofExpirationDates][KeyofOptionTypes][KeyOfStrikes].items():                  
                                print(str(ValueOfQuoteDateTimes.bucketquotedatetime)+ ' ' + ValueOfQuoteDateTimes.optionsymbol + ' ' + ValueOfQuoteDateTimes.bid)
        #                    print('                    Bid=' + str(ValueOfQuoteDateTimes.bid))
        #                    print('                    Ask=' + str(ValueOfQuoteDateTimes.ask))