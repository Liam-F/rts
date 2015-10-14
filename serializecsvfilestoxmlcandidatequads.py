# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 05:35:22 2015

@author: jmalinchak
"""

class read:
    
    def __init__(self,
                 downloadsdirectory = '$execute',
                 replacelistforcreatingdestinationpath = ['\\$execute\\','\\$executeprocessed\\'],
                 minpairspreadpercent = .6,
                 maxvalueatrisk = 2.4,
                 maxbidaskspreadpercentagesell = .25,
                 maxbidaskspreadpercentagebuy = .25,
                 showresults=0):
        print('initialized class serializecsvfilestoxmlcandidatequads')
        if showresults == 1:
            print('showresults=' + str(showresults) + ' serializecsvfilestoxmlcandidatequads')
        
        self.serialize(downloadsdirectory ,
                     replacelistforcreatingdestinationpath ,
                     minpairspreadpercent ,
                     maxvalueatrisk ,
                     maxbidaskspreadpercentagesell ,
                     maxbidaskspreadpercentagebuy ,
                     showresults)
    
#    def set_DictionaryOfSerializedFileObjects(self,DictionaryOfSerializedFileObjects):
#        self._DictionaryOfSerializedFileObjects = DictionaryOfSerializedFileObjects
#    def get_DictionaryOfSerializedFileObjects(self):
#        return self._DictionaryOfSerializedFileObjects
#    DictionaryOfSerializedFileObjects = property(get_DictionaryOfSerializedFileObjects, set_DictionaryOfSerializedFileObjects)   

    #DictionaryOfSerializedFileObjects
    def set_DictionaryOfSerializedFileObjects(self,DictionaryOfSerializedFileObjects):
        self._DictionaryOfSerializedFileObjects = DictionaryOfSerializedFileObjects
    def get_DictionaryOfSerializedFileObjects(self):
        return self._DictionaryOfSerializedFileObjects
    DictionaryOfSerializedFileObjects = property(get_DictionaryOfSerializedFileObjects, set_DictionaryOfSerializedFileObjects)

    #DictionaryOfSerializedQuadCandidateXMLPathNames
    def set_DictionaryOfSerializedQuadCandidateXMLPathNames(self,DictionaryOfSerializedQuadCandidateXMLPathNames):
        self._DictionaryOfSerializedQuadCandidateXMLPathNames = DictionaryOfSerializedQuadCandidateXMLPathNames
    def get_DictionaryOfSerializedQuadCandidateXMLPathNames(self):
        return self._DictionaryOfSerializedQuadCandidateXMLPathNames
    DictionaryOfSerializedQuadCandidateXMLPathNames = property(get_DictionaryOfSerializedQuadCandidateXMLPathNames, set_DictionaryOfSerializedQuadCandidateXMLPathNames)

    
    def countfiles(self,path,extension = ''):
        import os
        list_dir = []
        list_dir = os.listdir(path)
        count = 0
        for file in list_dir:
            if file.endswith(extension): # eg: '.txt'
                count += 1
        return count
  

    def serialize(self,
                     downloadsdirectory ,
                     replacelistforcreatingdestinationpath ,
                     minpairspreadpercent ,
                     maxvalueatrisk ,
                     maxbidaskspreadpercentagesell ,
                     maxbidaskspreadpercentagebuy ,
                     showresults
                 ):
        ## ########################
        ## How to get top directory
        import os
        downloadsdir_root = os.path.join(os.getcwd(),downloadsdirectory)
        if showresults == 1:
            print(downloadsdir_root)

        
        ## ####################
        ## Process downloads directories
        import readfiltersortserializetobucketdirectories

        dSerializedQuadCandidateXMLPathNames = {}
        
        iCount = 0
        for root, dirs, files in os.walk(downloadsdir_root):
            for name in dirs:
                downloadsdir_check = os.path.join(root, name)
                iCount = self.countfiles(downloadsdir_check,'.csv')
                print('Count of Csv files:',iCount,downloadsdir_check)
                #        ## ###################################
                if iCount > 0:
                    sourcedirectoryfull = downloadsdir_check
                    print(sourcedirectoryfull)
                    o = readfiltersortserializetobucketdirectories.read(sourcedirectoryfull,
                         minpairspreadpercent = minpairspreadpercent,
                         maxvalueatrisk = maxvalueatrisk,
                         maxbidaskspreadpercentagesell = maxbidaskspreadpercentagesell,
                         maxbidaskspreadpercentagebuy = maxbidaskspreadpercentagebuy,
                         sortbymeasure = 'spreadpercentageopen') # spreadpercentageopen | valueatriskopen
                    
                    self.DictionaryOfSerializedFileObjects = o.DictionaryOfSerializedFileObjects

                    d1 = o.DictionaryOfSerializedFileObjects
                    print('-- --','Looping DictionaryOfSerializedFileObjects in runquadbysymbol')
                    for k1,v1 in d1.items():
                        print('-- --','XMLFilenameOutput',v1.XMLFilenameOutput)
                        import deserializecandidatesxml
                        o1 = deserializecandidatesxml.deserialize(v1.XMLFilenameOutput)
                        d1 = o1.DictionaryOfCandidatesFromXML
                    
                        #minpairspreadpercent = 0.4
                        dSortableDictionary = {}
                    
                        import mytools
                        mysymbol = '---'
                        for k1,v1 in d1.items():
                            optiontype1 = mytools.get_from_optionsymbol.optiontype(v1['earlier']['optionsymbol'])
                            if optiontype1 == 'C':
                                for k2,v2 in d1.items():
                                    if v1['specifications']['bucketquotedatetime'] == v2['specifications']['bucketquotedatetime']:
                                        if v1['specifications']['symbol'] == v2['specifications']['symbol']:
                                            mysymbol = v1['specifications']['symbol']
                                            optiontype2 = mytools.get_from_optionsymbol.optiontype(v2['earlier']['optionsymbol'])
                                            if optiontype2 == 'P':
                                                if float(v1['calculations']['spreadpercentageopen']) > minpairspreadpercent and float(v2['calculations']['spreadpercentageopen']) > minpairspreadpercent:
                                                    EarlierStrike1 = mytools.get_from_optionsymbol.strike(v1['earlier']['optionsymbol'])
                                                    LaterStrike1 = mytools.get_from_optionsymbol.strike(v1['later']['optionsymbol'])
                                                    EarlierStrike2 = mytools.get_from_optionsymbol.strike(v2['earlier']['optionsymbol'])
                                                    LaterStrike2 = mytools.get_from_optionsymbol.strike(v2['later']['optionsymbol'])
                                                    if float(EarlierStrike1) > float(v1['specifications']['stockprice']) and float(LaterStrike1) > float(v1['specifications']['stockprice']):
                                                        if float(EarlierStrike2) < float(v1['specifications']['stockprice']) and float(LaterStrike2) < float(v1['specifications']['stockprice']):
                                                            if k1 != k2:
                                                                sumofvalueatrisk = float(v1['calculations']['valueatriskopen']) + float(v2['calculations']['valueatriskopen'])
                                                                dSortableDictionary[len(dSortableDictionary)] = {'sortbymeasurevalue' : sumofvalueatrisk, 'callcalendarspread' : v1, 'putcalendarspread' : v2, 'sortbymeasurename' : 'valueatrisk'}
                            
                        from collections import OrderedDict
                        dOrdered = OrderedDict(sorted(dSortableDictionary.items(), key=lambda t: t[1]['sortbymeasurevalue']))
                        import serializedictionaryofcalendarspreadquadstoxml
                        oquads = serializedictionaryofcalendarspreadquadstoxml.serialize(sourcedirectoryfull,mysymbol,dOrdered,1000,0)

                        #print('got to here 2212')
                                                
                        if oquads.Complete == 1 and len(oquads.XMLFilenameOutput)>0:
                            
                            print("oquads.XMLFilenameOutput=",oquads.XMLFilenameOutput)
                            dSerializedQuadCandidateXMLPathNames[len(dSerializedQuadCandidateXMLPathNames)] = oquads.XMLFilenameOutput
                            
                            #print('Count',sourcedirectoryfull,iCount)
                            #destinationdirectoryfull = sourcedirectoryfull
                            
                            destinationdirectoryfull = sourcedirectoryfull.replace(replacelistforcreatingdestinationpath[0],replacelistforcreatingdestinationpath[1])
                            import mytools
                            mytools.general.make_sure_path_exists(destinationdirectoryfull)
                            print('Destination',destinationdirectoryfull)
                            import shutil
                            # Move src to dst (mv src dst)
                            shutil.rmtree(destinationdirectoryfull,ignore_errors=True, onerror=None)
                            shutil.move(sourcedirectoryfull, destinationdirectoryfull)
                            
        print('got here 8181',len(dSerializedQuadCandidateXMLPathNames))                
        
        self.DictionaryOfSerializedQuadCandidateXMLPathNames = dSerializedQuadCandidateXMLPathNames
                                             