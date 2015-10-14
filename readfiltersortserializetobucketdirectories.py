# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 07:20:16 2014

@author: jmalinchak
"""

class read:
    
    def __init__(self, downloaddirectory,
                         minpairspreadpercent = 0.5,
                         maxvalueatrisk = 2.4,
                         maxbidaskspreadpercentagesell = 0.5,
                         maxbidaskspreadpercentagebuy = 0.5,
                         minopeninterest = 5,
                         sortbymeasure = 'spreadpercentageopen', # options: spreadpercentageopen | valueatriskopen
                         showresults=0):
        print('initialized class readfiltersortserializetobucketdirectories.py')
        if showresults == 1:
            print('showresults=' + str(showresults) + ' readintomemoryprocessallfilesindirectorylocal')
        #self.loop_through_optionsfiles(pathfilename)
        
        self.processfiles(downloaddirectory,
                          minpairspreadpercent,
                          maxvalueatrisk,
                          maxbidaskspreadpercentagesell,
                          maxbidaskspreadpercentagebuy,
                          minopeninterest,
                          sortbymeasure,
                          showresults)
    
    def set_DictionaryOfSerializedFileObjects(self,DictionaryOfSerializedFileObjects):
        self._DictionaryOfSerializedFileObjects = DictionaryOfSerializedFileObjects
    def get_DictionaryOfSerializedFileObjects(self):
        return self._DictionaryOfSerializedFileObjects
    DictionaryOfSerializedFileObjects = property(get_DictionaryOfSerializedFileObjects, set_DictionaryOfSerializedFileObjects)   


    def set_DictionaryOfSerializedPathFileNames(self,DictionaryOfSerializedPathFileNames):
        self._DictionaryOfSerializedPathFileNames = DictionaryOfSerializedPathFileNames
    def get_DictionaryOfSerializedPathFileNames(self):
        return self._DictionaryOfSerializedPathFileNames
    DictionaryOfSerializedPathFileNames = property(get_DictionaryOfSerializedPathFileNames, set_DictionaryOfSerializedPathFileNames)   

    def processfiles(self,downloaddirectory,
                         criteria_for_minpairspreadpercent ,
                         criteria_for_maxvalueatrisk ,
                         criteria_for_maxbidaskspreadpercentagesell ,
                         criteria_for_maxbidaskspreadpercentagebuy ,
                         criteria_for_minopeninterest ,
                         criteria_for_sortbymeasure , 
                         showresults):
                         
        # C:\Documents and Settings\jmalinchak\My Documents\My Python\Active\py\downloads\2015-01-14
        dDownloadDirectories = {}
        dDownloadDirectories[len(dDownloadDirectories)] = downloaddirectory
        #dDownloadDirectories[len(dDownloadDirectories)] = 'downloads\\2014-12-27\\15\\45\\TWTR'
#        showresults = 0
#        criteria_for_minpairspreadpercent = 0.5
#        criteria_for_maxvalueatrisk = 0.7
#        criteria_for_sortbymeasure = 'spreadpercentageopening' # # spreadpercentageopening | valueatrisk
        
        print('--------------------------------')
        print('-- criteria for')
        print('--   minpairspreadpercent = ',criteria_for_minpairspreadpercent)
        print('--   maxvalueatrisk = ',criteria_for_maxvalueatrisk)
        print('--   sortbymeasure = ',criteria_for_sortbymeasure)
        print('--------------------------------')
        dOutputFiles = {}
        dSerializedFileObjects = {}
        
        import buildpairsdictionarywithcriteriafromdirectoryofpulledfiles
        import convertpairsdictionarytosortable
        #import concatonatesortablepairdictionaries
        import sortasortablepairsdictionary
        
        dSortableDictionaries = {}
        print('---','readfiltersortserializetobucketdirectories.py')
        print('---',downloaddirectory)
        
        
        # loop dictionary of paths --------------------------------------------------------------------
        for k0,v0 in dDownloadDirectories.items():
            
            downloadsdir_check=v0            
            
            print('--- --', 'checking for files in dir tree')
            print('--- --',downloadsdir_check)
            print('--- -- --',str(k0+1) + ' of ' + str(len(dDownloadDirectories)) + ' directories')
            
                        
            
            c = buildpairsdictionarywithcriteriafromdirectoryofpulledfiles.build(rootlocalforfilespulled=v0 
                                                                                ,  minpairspreadpercent=criteria_for_minpairspreadpercent
                                                                                ,  maxvalueatrisk=criteria_for_maxvalueatrisk
                                                                                ,  maxbidaskspreadpercentagesell = criteria_for_maxbidaskspreadpercentagesell 
                                                                                ,  maxbidaskspreadpercentagebuy = criteria_for_maxbidaskspreadpercentagebuy 
                                                                                ,  minopeninterest = criteria_for_minopeninterest
                                                                                ,  showresults=showresults) 
                                                                                 
            o = convertpairsdictionarytosortable.convert(c.DictionaryOfFilteredCalendarPairs,criteria_for_sortbymeasure)
            
            dSortableDictionaries = o.DictionaryOfSortablePairsOutput
            
            s = sortasortablepairsdictionary.sort(dSortableDictionaries,1) #  <-- 1 means to show results.  it will print it out
        
            dSortedPairsOutput = s.DictionaryOfSortedPairsOutput
            
            # ################
            # Prints to screen
            for k3,v3 in dSortedPairsOutput.items():
                sortbymeasurename = v3['sortbymeasurename']
                sortbymeasurevalue = round(v3['sortbymeasurevalue'],3)
                earlier = v3['earlier']
                later = v3['later']
                if showresults == 1:
                    print(k3,
                            sortbymeasurename,
                            sortbymeasurevalue,
                            earlier.bid,later.ask,
                            earlier.optionsymbol,
                            later.optionsymbol)
            
            # ################################
            # Serializes dictionary
            import serializesortedpairdictionarytoxmlbucketdirectory
            print('-- --------------------------')
            print('--','pairs serializing...')
            oSerialize = serializesortedpairdictionarytoxmlbucketdirectory.serialize(dSortedPairsOutput)
                
            dSerializedFileObjects[len(dSerializedFileObjects)] = oSerialize        
            dOutputFiles[len(dOutputFiles)] = oSerialize.XMLFilenameOutput
            #print(oserialize.)
        self.DictionaryOfSerializedFileObjects = dSerializedFileObjects
        self.DictionaryOfSerializedPathFileNames = dOutputFiles