# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 07:20:16 2014

@author: jmalinchak
"""
class read:
    def __init__(self,
                 rootlocalforfilespulled='downloads\2014-12-27\15\45\EWZ',
                 sortby='spreadpercentageopening', #either spreadpercentageopening or valueatrisk
                 showresults=1):
                     
        self.execute_results(rootlocalforfilespulled,showresults)

    def set_DictionaryOfSortablePairsOutput(self,DictionaryOfSortablePairsOutput):
        self._DictionaryOfSortablePairsOutput = DictionaryOfSortablePairsOutput
    def get_DictionaryOfSortablePairsOutput(self):
        return self._DictionaryOfSortablePairsOutput
    DictionaryOfSortablePairsOutput = property(get_DictionaryOfSortablePairsOutput, set_DictionaryOfSortablePairsOutput)   
    
#    def set_DownloadDirectoryLocal(self,DownloadDirectoryLocal):
#        self._DownloadDirectoryLocal = DownloadDirectoryLocal
#    def get_DownloadDirectoryLocal(self):
#        return self._DownloadDirectoryLocal
#    DownloadDirectoryLocal = property(get_DownloadDirectoryLocal, set_DownloadDirectoryLocal)    
    
    def execute_results(self,rootlocalforfilespulled,showresults):
        ################################################    
        #
        # Returns downloaddirectorylocal
        #
        ################################################  
    
        #import os
        #import pullpricessbasedonlocalinputfilestodownloaddirectorylocal
             
        dSortableDictionary = {}
                
        #downloadedfilespath = os.path.join(os.getcwd(),'downloads','2014-12-27','15','45')
        #downloadedfilespathsymbol= os.path.join(rootlocalforfilespulled,'EWZ')
        import buildpairsdictionarywithcriteriafromdirectoryofpulledfiles
        c = buildpairsdictionarywithcriteriafromdirectoryofpulledfiles.build(rootlocalforfilespulled, 0.4)
                                                        
        for k1,v1 in c.DictionaryOfFilteredCalendarPairs.items():
            #print(k1)
            earlier = v1[0]
            later = v1[1]
            spreadpercentageopening = float(earlier.bid)/float(later.ask)
            valueatrisk = -float(earlier.bid)+float(later.ask)
            if sortby = 'valueatrisk'
                dSortableDictionary[len(dSortableDictionary)] = [valueatrisk,earlier,later,downloadedfilespathsymbol,k1,'valueatrisk']
            else
                dSortableDictionary[len(dSortableDictionary)] = [spreadpercentageopening,earlier,later,downloadedfilespathsymbol,k1]
        #######################################################################
        self.DictionaryOfSortablePairsOutput = dSortableDictionary
            
