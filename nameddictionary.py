# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 00:17:18 2014

@author: jmalinchak
""" 
#'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\Active\\downloads\\a20141129'

class read:
    
    def __init__(self, directorylocal,showresults=0):
        print('initialized class nameddictionary.py')
        self.initialize(directorylocal,showresults)
        
    def set_DirectoryLocal(self,DirectoryLocal):
        self._DirectoryLocal = DirectoryLocal
    def get_DirectoryLocal(self):
        return self._DirectoryLocal
    DirectoryLocal = property(get_DirectoryLocal, set_DirectoryLocal)
        
    def set_MainDictionariesObject(self,MainDictionariesObject):
        self._MainDictionariesObject = MainDictionariesObject
    def get_MainDictionariesObject(self):
        return self._MainDictionariesObject
    MainDictionariesObject = property(get_MainDictionariesObject, set_MainDictionariesObject)

    def set_DictionaryOfFilteredInstances(self,DictionaryOfFilteredInstances):
        self._DictionaryOfFilteredInstances = DictionaryOfFilteredInstances
    def get_DictionaryOfFilteredInstances(self):
        return self._DictionaryOfFilteredInstances
    DictionaryOfFilteredInstances = property(get_DictionaryOfFilteredInstances, set_DictionaryOfFilteredInstances)

    def set_NamedDictionaries(self,NamedDictionaries):
        self._NamedDictionaries = NamedDictionaries
    def get_NamedDictionaries(self):
        return self._NamedDictionaries
    NamedDictionaries = property(get_NamedDictionaries, set_NamedDictionaries)


#    def set_NamedDictionaries(self,NamedDictionaries):
#        self._NamedDictionaries = NamedDictionaries
#    def get_NamedDictionaries(self):
#        return self._NamedDictionaries
#    NamedDictionaries = property(get_NamedDictionaries, set_NamedDictionaries)

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
            
    
    def initialize(self,directorylocal,showresults):
        import os
        directorylocal = os.path.realpath(directorylocal)
        self.DirectoryLocal = directorylocal
        print('directorylocal:',directorylocal)
        files = []
        import os
        import readintomemorycreatemaindictionariesfromdirectorylocal
        for subdir, dirs, files in os.walk(directorylocal):
            break
        print('-- ---------------------')
        print('')        
        print('--','nameddictionary.py')
        print('--',str(len(files)) + ' files found.  Process of reading csv files starts now...')
        print('')        
        print('-- ---------------------')
        o = readintomemorycreatemaindictionariesfromdirectorylocal.build(directorylocal,showresults)
        
        if showresults == 1:
            print('111111 nameddictionary 1111111')

        #print('33333333333333333333333333333333333')
        self.NamedDictionaries = o.NamedDictionaries
        print(str(len(o.NamedDictionaries)) + ' symbols initialized within class nameddictionary.py')
        
#        dNamedDictionaries = o.NamedDictionaries
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
        

        
    def optioninstances(self,Symbol='',ExpirationDate='',OptionType='',Strike='',BucketQuoteDatetime=''):
        dNamedDictionaries = self.NamedDictionaries
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
                                            for KeyOfBucketQuoteDateTimes,ValueOfOptionInstances in dNamedDictionaries[KeyOfSymbols][KeyofExpirationDates][KeyofOptionTypes][KeyOfStrikes].items():
                                                #***********************************************************************************
                                                # reinsert this later. need to format datetime
                                                
                                                #if KeyOfBucketQuoteDateTimes.date() == datetime.datetime.strptime(ExpirationDate, '%Y-%m-%d').date() or len(BucketQuoteDatetime) == 0:
                                                    
                                                #***********************************************************************************
                                                dResult[len(dResult)] = ValueOfOptionInstances #str(ValueOfOptionInstances.bucketquotedatetime)+ ' ' + str(ValueOfOptionInstances.quotedatetime)+ ' ' +ValueOfOptionInstances.optionsymbol + ' ' + ValueOfOptionInstances.bid

                                                
        self.DictionaryOfFilteredInstances = dResult
        return self.DictionaryOfFilteredInstances
#    def filterresults(self,Symbol,ExpirationDate,OptionType,Strike,QuoteDatetime):
#        dNamedDictionaries = self.MainDictionariesObject.NamedDictionaries
#        #from datetime import datetime
#        dResult = {}
#        for KeyOfSymbols in dNamedDictionaries.keys():
#            if KeyOfSymbols == Symbol or len(Symbol) == 0:
#                #print(KeyOfSymbols)
#                for KeyofExpirationDates in dNamedDictionaries[KeyOfSymbols].keys():
#                    
##                    cdate = read.convertdate(ExpirationDate)
##                    #print(str(datetime.date(1900,1,1)))
##                    
##                    date_object = cdate
##                    if not date_object == datetime.date(1900,1,1):
##                        date_object = datetime.strptime(ExpirationDate, '%Y-%m-%d')
#                    import datetime
##                    cdate = datetime.datetime.strptime(ExpirationDate, '%Y-%m-%d').date()
##                    print(cdate)
#                    if KeyofExpirationDates.date() == datetime.datetime.strptime(ExpirationDate, '%Y-%m-%d').date() or len(ExpirationDate) == 0:
#                        #print(KeyofExpirationDates)    
#                        #print(len(dNamedDictionaries[KeyOfSymbols][KeyofExpirationDates]))
#                        for KeyofOptionTypes in dNamedDictionaries[KeyOfSymbols][KeyofExpirationDates].keys():
#                            #print(KeyofOptionTypes+' ssssssssssssssssssssssssssssss')
#                            if KeyofOptionTypes == OptionType or len(OptionType) == 0:
#                                #print(KeyofOptionTypes)
#                                for KeyOfStrikes in dNamedDictionaries[KeyOfSymbols][KeyofExpirationDates][KeyofOptionTypes].keys():
#                    #                print('            ' + str(KeyOfStrikes) + ' ' + KeyofOptionTypes) 
#                                    if len(Strike) == 0 or float(KeyOfStrikes) == float(Strike):
#                                            for KeyOfQuoteDateTimes,ValueOfOptionInstances in dNamedDictionaries[KeyOfSymbols][KeyofExpirationDates][KeyofOptionTypes][KeyOfStrikes].items():
#                                                #print(KeyOfQuoteDateTimes)
#                                                dResult[len(dResult)] = ValueOfOptionInstances #str(ValueOfOptionInstances.bucketquotedatetime)+ ' ' + str(ValueOfOptionInstances.quotedatetime)+ ' ' +ValueOfOptionInstances.optionsymbol + ' ' + ValueOfOptionInstances.bid
#                                                #print(str(ValueOfOptionInstances.bucketquotedatetime)+ ' ' + ValueOfOptionInstances.optionsymbol + ' ' + ValueOfOptionInstances.bid)
#                        #                    print('                    Bid=' + str(ValueOfOptionInstances.bid))
#                        #                    print('                    Ask=' + str(ValueOfOptionInstances.ask))
#                                                
#        self.DictionaryOfFilteredInstances = dResult
#class filter(read):
#    def __init__(self,Symbol='',ExpirationDate='',OptionType='',Strike='',QuoteDatetime=''):
#        self.NamedDictionaries = read.NamedDictionaries
#        return self.execute_filtering(Symbol,ExpirationDate,OptionType,Strike,QuoteDatetime)
#
#
#    def set_NamedDictionaries(self,NamedDictionaries):
#        self._NamedDictionaries = NamedDictionaries
#    def get_NamedDictionaries(self):
#        return self._NamedDictionaries
#    NamedDictionaries = property(get_NamedDictionaries, set_NamedDictionaries)
#    
#    def set_DictionaryOfFilteredInstances(self,DictionaryOfFilteredInstances):
#        self._DictionaryOfFilteredInstances = DictionaryOfFilteredInstances
#    def get_DictionaryOfFilteredInstances(self):
#        return self._DictionaryOfFilteredInstances
#    DictionaryOfFilteredInstances = property(get_DictionaryOfFilteredInstances, set_DictionaryOfFilteredInstances)
#    
#    def execute_filtering(self,Symbol,ExpirationDate,OptionType,Strike,QuoteDatetime):
#        dNamedDictionaries = self.NamedDictionaries
#        #from datetime import datetime
#        dResult = {}
#        for KeyOfSymbols in dNamedDictionaries.keys():
#            if KeyOfSymbols == Symbol or len(Symbol) == 0:
#                #print(KeyOfSymbols)
#                for KeyofExpirationDates in dNamedDictionaries[KeyOfSymbols].keys():
#                    
##                    cdate = read.convertdate(ExpirationDate)
##                    #print(str(datetime.date(1900,1,1)))
##                    
##                    date_object = cdate
##                    if not date_object == datetime.date(1900,1,1):
##                        date_object = datetime.strptime(ExpirationDate, '%Y-%m-%d')
#                    import datetime
##                    cdate = datetime.datetime.strptime(ExpirationDate, '%Y-%m-%d').date()
##                    print(cdate)
#                    if KeyofExpirationDates.date() == datetime.datetime.strptime(ExpirationDate, '%Y-%m-%d').date() or len(ExpirationDate) == 0:
#                        #print(KeyofExpirationDates)    
#                        #print(len(dNamedDictionaries[KeyOfSymbols][KeyofExpirationDates]))
#                        for KeyofOptionTypes in dNamedDictionaries[KeyOfSymbols][KeyofExpirationDates].keys():
#                            #print(KeyofOptionTypes+' ssssssssssssssssssssssssssssss')
#                            if KeyofOptionTypes == OptionType or len(OptionType) == 0:
#                                #print(KeyofOptionTypes)
#                                for KeyOfStrikes in dNamedDictionaries[KeyOfSymbols][KeyofExpirationDates][KeyofOptionTypes].keys():
#                    #                print('            ' + str(KeyOfStrikes) + ' ' + KeyofOptionTypes) 
#                                    if len(Strike) == 0 or float(KeyOfStrikes) == float(Strike):
#                                            for KeyOfQuoteDateTimes,ValueOfOptionInstances in dNamedDictionaries[KeyOfSymbols][KeyofExpirationDates][KeyofOptionTypes][KeyOfStrikes].items():
#                                                #print(KeyOfQuoteDateTimes)
#                                                dResult[len(dResult)] = ValueOfOptionInstances #str(ValueOfOptionInstances.bucketquotedatetime)+ ' ' + str(ValueOfOptionInstances.quotedatetime)+ ' ' +ValueOfOptionInstances.optionsymbol + ' ' + ValueOfOptionInstances.bid
#                                                #print(str(ValueOfOptionInstances.bucketquotedatetime)+ ' ' + ValueOfOptionInstances.optionsymbol + ' ' + ValueOfOptionInstances.bid)
#                        #                    print('                    Bid=' + str(ValueOfOptionInstances.bid))
#                        #                    print('                    Ask=' + str(ValueOfOptionInstances.ask))
#                                                
#        self.DictionaryOfFilteredInstances = dResult
#        return self.DictionaryOfFilteredInstances