# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 07:20:16 2014

@author: jmalinchak
"""
class read:
    def __init__(self,
                 rootlocalforfilespulled='downloads\2014-12-27\15\45\EWZ',
                 showresults=1):
                     
        self.execute_results(rootlocalforfilespulled,showresults)

    def set_DictionaryOfSortablePairs(self,DictionaryOfSortablePairs):
        self._DictionaryOfSortablePairs = DictionaryOfSortablePairs
    def get_DictionaryOfSortablePairs(self):
        return self._DictionaryOfSortablePairs
    DictionaryOfSortablePairs = property(get_DictionaryOfSortablePairs, set_DictionaryOfSortablePairs)   
    
    def set_DownloadDirectoryLocal(self,DownloadDirectoryLocal):
        self._DownloadDirectoryLocal = DownloadDirectoryLocal
    def get_DownloadDirectoryLocal(self):
        return self._DownloadDirectoryLocal
    DownloadDirectoryLocal = property(get_DownloadDirectoryLocal, set_DownloadDirectoryLocal)    
    
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
            spreadpercentage = float(earlier.bid)/float(later.ask)
            valueatrisk = -float(earlier.bid)+float(later.ask)
            dSortableDictionary[len(dSortableDictionary)] = [spreadpercentage,earlier,later,downloadedfilespathsymbol,k1]
        #######################################################################
            
            
