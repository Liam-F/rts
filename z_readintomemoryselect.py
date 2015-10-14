# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 00:17:18 2014

@author: jmalinchak
""" 
#'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\Active\\downloads\\a20141129'

class read:
    
    def __init__(self, directorylocal):
        self.initialize(directorylocal)

    def set_MainDictionariesObject(self,MainDictionariesObject):
        self._MainDictionariesObject = MainDictionariesObject
    def get_MainDictionariesObject(self):
        return self._MainDictionariesObject
    MainDictionariesObject = property(get_MainDictionariesObject, set_MainDictionariesObject)

    def set_ResultDictionary(self,ResultDictionary):
        self._ResultDictionary = ResultDictionary
    def get_ResultDictionary(self):
        return self._ResultDictionary
    ResultDictionary = property(get_ResultDictionary, set_ResultDictionary)


    def set_NamedDictionaries(self,NamedDictionaries):
        self._NamedDictionaries = NamedDictionaries
    def get_NamedDictionaries(self):
        return self._NamedDictionaries
    NamedDictionaries = property(get_NamedDictionaries, set_NamedDictionaries)

    def convertdate(MyString):
        import datetime

        minyear = 1900
        maxyear = 2060
        
        mydate = MyString
        
        dateparts = mydate.split('-')
#        print(dateparts[0])
#        print(dateparts[1])
#        print(dateparts[2])
        try:
            if len(dateparts) != 3:
               raise ValueError("Invalid date format")
            if int(dateparts[0]) > maxyear or int(dateparts[0]) <= minyear:
               raise ValueError("Year out of range")
            
            dateobj = datetime.date(int(dateparts[0]),int(dateparts[1]),int(dateparts[2]))
            #print(str(dateobj)) #str(dateobj
            return dateobj
        except:
            return datetime.date(1900,1,1)
            
    
    def initialize(self,directorylocal):
        import readintomemorycreatemaindictionariesfromdirectorylocal
        self.MainDictionariesObject = readintomemorycreatemaindictionariesfromdirectorylocal.build(directorylocal)
        #NamedDictionaries = MainDictionariesObject.NamedDictionaries
        
    def filter(self,Symbol,ExpirationDate,OptionType,Strike,QuoteDatetime):
        dNamedDictionaries = self.MainDictionariesObject.NamedDictionaries
        #from datetime import datetime
        dResult = {}
        for KeyOfSymbols in dNamedDictionaries.keys():
            if KeyOfSymbols == Symbol or len(Symbol) == 0:
                #print(KeyOfSymbols)
                for KeyofExpirationDates in dNamedDictionaries[KeyOfSymbols].keys():
                    
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
                        #print(len(dNamedDictionaries[KeyOfSymbols][KeyofExpirationDates]))
                        for KeyofOptionTypes in dNamedDictionaries[KeyOfSymbols][KeyofExpirationDates].keys():
                            #print(KeyofOptionTypes+' ssssssssssssssssssssssssssssss')
                            if KeyofOptionTypes == OptionType or len(OptionType) == 0:
                                #print(KeyofOptionTypes)
                                for KeyOfStrikes in dNamedDictionaries[KeyOfSymbols][KeyofExpirationDates][KeyofOptionTypes].keys():
                    #                print('            ' + str(KeyOfStrikes) + ' ' + KeyofOptionTypes) 
                                    if len(Strike) == 0 or float(KeyOfStrikes) == float(Strike):
                                            for KeyOfQuoteDateTimes,ValueOfOptionInstances in dNamedDictionaries[KeyOfSymbols][KeyofExpirationDates][KeyofOptionTypes][KeyOfStrikes].items():
                                                #print(KeyOfQuoteDateTimes)
                                                dResult[len(dResult)] = ValueOfOptionInstances #str(ValueOfOptionInstances.bucketquotedatetime)+ ' ' + str(ValueOfOptionInstances.quotedatetime)+ ' ' +ValueOfOptionInstances.optionsymbol + ' ' + ValueOfOptionInstances.bid
                                                #print(str(ValueOfOptionInstances.bucketquotedatetime)+ ' ' + ValueOfOptionInstances.optionsymbol + ' ' + ValueOfOptionInstances.bid)
                        #                    print('                    Bid=' + str(ValueOfOptionInstances.bid))
                        #                    print('                    Ask=' + str(ValueOfOptionInstances.ask))
        return dResult