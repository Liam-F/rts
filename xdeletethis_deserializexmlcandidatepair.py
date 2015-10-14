# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 00:17:18 2014

@author: jmalinchak
""" 
#'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\Active\\downloads\\a20141129'

class deserialize:
    
    def __init__(self, pathfilenamecandidatexml,showresults=0):
        print('initialized class nameddictionary.py')
        self.executeprocess(pathfilenamecandidatexml,showresults)
        
#    def set_pathfilenamecandidatexml(self,pathfilenamecandidatexml):
#        self._pathfilenamecandidatexml = pathfilenamecandidatexml
#    def get_pathfilenamecandidatexml(self):
#        return self._pathfilenamecandidatexml
#    pathfilenamecandidatexml = property(get_pathfilenamecandidatexml, set_pathfilenamecandidatexml)
#        
#    def set_MainDictionariesObject(self,MainDictionariesObject):
#        self._MainDictionariesObject = MainDictionariesObject
#    def get_MainDictionariesObject(self):
#        return self._MainDictionariesObject
#    MainDictionariesObject = property(get_MainDictionariesObject, set_MainDictionariesObject)
#
#    def set_DictionaryOfFilteredInstances(self,DictionaryOfFilteredInstances):
#        self._DictionaryOfFilteredInstances = DictionaryOfFilteredInstances
#    def get_DictionaryOfFilteredInstances(self):
#        return self._DictionaryOfFilteredInstances
#    DictionaryOfFilteredInstances = property(get_DictionaryOfFilteredInstances, set_DictionaryOfFilteredInstances)
#
#    def set_NamedDictionaries(self,NamedDictionaries):
#        self._NamedDictionaries = NamedDictionaries
#    def get_NamedDictionaries(self):
#        return self._NamedDictionaries
#    NamedDictionaries = property(get_NamedDictionaries, set_NamedDictionaries)
#
#
##    def set_NamedDictionaries(self,NamedDictionaries):
##        self._NamedDictionaries = NamedDictionaries
##    def get_NamedDictionaries(self):
##        return self._NamedDictionaries
##    NamedDictionaries = property(get_NamedDictionaries, set_NamedDictionaries)
#
#    def convertdate(MyString):
#        import datetime
#
#        minyear = 1900
#        maxyear = 2060
#        
#        mydate = MyString
#        
#        dateparts = mydate.split('-')
##        print(dateparts[0])
##        print(dateparts[1])
##        print(dateparts[2])
#        try:
#            if len(dateparts) != 3:
#               raise ValueError("Invalid date format")
#            if int(dateparts[0]) > maxyear or int(dateparts[0]) <= minyear:
#               raise ValueError("Year out of range")
#            
#            dateobj = datetime.date(int(dateparts[0]),int(dateparts[1]),int(dateparts[2]))
#            #print(str(dateobj)) #str(dateobj
#            return dateobj
#        except:
#            return datetime.date(1900,1,1)
#            
    
    def initialize(self,pathfilenamecandidatexml,showresults):
            import deserializecandidatesxml
            o1 = deserializecandidatesxml.deserialize(pathfilenamecandidatexml)
            d1 = o1.DictionaryOfCandidatesFromXML
            
            totalcandidatepairs = totalcandidatepairs + len(d1)
            
            #print('   --',len(d1),'candidate pairs found')
            
            for k,v in d1.items():
                if v['specifications']['symbol'] in excludesymbols.values():
                    if not v['specifications']['symbol'] in d_exclude.values():
                        d_exclude[len(d_exclude)] = v['specifications']['symbol']
                        
                if not v['specifications']['symbol'] in excludesymbols.values():
                    d3[len(d3)] = v 
                
            print('   --',len(d1),'candidate pairs in',v['specifications']['symbol'])
            
            print('  ','--',pathfilenamecandidatexml)