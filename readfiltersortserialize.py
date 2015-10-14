# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 07:20:16 2014

@author: jmalinchak
"""

class read:
    
    def __init__(self, downloaddirectory,showresults=0):
        print('initialized class readintomemoryprocessallfilesindirectorylocal')
        if showresults == 1:
            print('showresults=' + str(showresults) + ' readintomemoryprocessallfilesindirectorylocal')
        #self.loop_through_optionsfiles(pathfilename)
        
        self.processfiles(downloaddirectory,showresults)


    def set_DictionaryOfSerializedPathFileNames(self,DictionaryOfSerializedPathFileNames):
        self._DictionaryOfSerializedPathFileNames = DictionaryOfSerializedPathFileNames
    def get_DictionaryOfSerializedPathFileNames(self):
        return self._DictionaryOfSerializedPathFileNames
    DictionaryOfSerializedPathFileNames = property(get_DictionaryOfSerializedPathFileNames, set_DictionaryOfSerializedPathFileNames)   

    def processfiles(self,downloaddirectory,showresults):


        # C:\Documents and Settings\jmalinchak\My Documents\My Python\Active\py\downloads\2015-01-14
        dDownloadDirectories = {}
        dDownloadDirectories[len(dDownloadDirectories)] = downloaddirectory
        #dDownloadDirectories[len(dDownloadDirectories)] = 'downloads\\2014-12-27\\15\\45\\TWTR'
        criteria_for_showresults = 0
        criteria_for_minspreadpercent = 0.5
        criteria_for_maxvalueatrisk = 2.4
        criteria_for_sortbymeasure = 'spreadpercentageopening' # # spreadpercentageopening | valueatrisk
        
        dOutputFiles = {}
        
        import buildpairsdictionarywithcriteriafromdirectoryofpulledfiles
        import convertpairsdictionaryfromqualifiedtosortable
        #import concatonatesortablepairdictionaries
        import sortasortabledictionary
        
        dSortableDictionaries = {}
        
        # loop dictionary of paths --------------------------------------------------------------------
        for k0,v0 in dDownloadDirectories.items():
            print(k0,v0)
            
            c = buildpairsdictionarywithcriteriafromdirectoryofpulledfiles.build(rootlocalforfilespulled=v0, 
                                                                                #criteria_for_minspreadpercent
                                                                                 maxvalueatrisk=criteria_for_maxvalueatrisk,
                                                                                 showresults=criteria_for_showresults) 
                                                                                 
            o = convertpairsdictionaryfromqualifiedtosortable.convert(c.DictionaryOfFilteredCalendarPairs,criteria_for_sortbymeasure)
            
            dSortableDictionaries = o.DictionaryOfSortablePairsOutput
            
            s = sortasortabledictionary.sort(dSortableDictionaries,1) #  <-- 1 means to show results.  it will print it out
        
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
            import serializesortedpairdictionarytoxml
            oSerialize = serializesortedpairdictionarytoxml.serialize(dSortedPairsOutput)
            dOutputFiles[len(dOutputFiles)] = oSerialize.XMLFilenameOutput
            #print(oserialize.)
        self.DictionaryOfSerializedPathFileNames = dOutputFiles