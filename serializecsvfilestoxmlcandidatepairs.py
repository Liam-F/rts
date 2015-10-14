# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 05:35:22 2015

@author: jmalinchak
"""

class read:
    
    def __init__(self,
                 downloadsdirectory = 'downloads',
                 replacelistforcreatingdestinationpath = ['\\downloads\\','\\downloadsprocessed\\'],
                 minpairspreadpercent = .6,
                 maxvalueatrisk = 2.4,
                 maxbidaskspreadpercentagesell = .25,
                 maxbidaskspreadpercentagebuy = .25,
                 showresults=0):
        print('initialized class serializeallcsvfilesindownloadsdirectorywithparameters')
        if showresults == 1:
            print('showresults=' + str(showresults) + ' serializeallcsvfilesindownloadsdirectorywithparameters')
        
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
    #    import mytools
    #    downloadsdir_bucketdatetime = mytools.mystrings.appendnormaldateddirectorybasedoncurrenttime15(downloadsdir_root)
    #    print(downloadsdir_bucketdatetime)
    #    downloadsdir_hour = os.path.dirname(downloadsdir_bucketdatetime)
    #    print('downloadsdir_hour','=',downloadsdir_hour)
    #    downloadsdir_day = os.path.dirname(downloadsdir_hour)
    #    
        ## #############################
        ## directory for processed files
        #replacedirectory = replacelistforcreatingdestinationpath #['\\downloads\\','\\downloadsprocessed\\']
        
        ## ####################
        ## Process downloads directories
        import readfiltersortserializetobucketdirectories
        iCount = 0
#        for root, dirs, files in os.walk(downloadsdir_root):
#            if len(dirs) == 0:
#                for name in files:
        iCount = 0
        for root, dirs, files in os.walk(downloadsdir_root):
            for name in dirs:
                downloadsdir_check = os.path.join(root, name)
                iCount = self.countfiles(downloadsdir_check,'.csv')
                print('Count of Csv files:',iCount,downloadsdir_check)
#        for root, dirs, files in os.walk(downloadsdir_root):
#            for name in dirs:
#                    downloadsdir_check = os.path.join(root, name)
#                    iCount = len(files) #self.countfiles(downloadsdir_check,'.csv')
#                    print('Count of Csv files:',iCount,downloadsdir_check)
#            #        ## ###################################
                if iCount > 0:
                    sourcedirectoryfull = downloadsdir_check
                    o = readfiltersortserializetobucketdirectories.read(sourcedirectoryfull,
                         minpairspreadpercent = minpairspreadpercent,
                         maxvalueatrisk = maxvalueatrisk,
                         maxbidaskspreadpercentagesell = maxbidaskspreadpercentagesell,
                         maxbidaskspreadpercentagebuy = maxbidaskspreadpercentagebuy,
                         sortbymeasure = 'spreadpercentageopen') # spreadpercentageopen | valueatriskopen
                    
                    self.DictionaryOfSerializedFileObjects = o.DictionaryOfSerializedFileObjects
                    dSerialized = o.DictionaryOfSerializedFileObjects
                    
                    print('------------------------------')
                    print('-- Count of DictionaryOfSerializedFileObjects')
                    print('--  ',len(dSerialized))
                    for k,v in dSerialized.items():
                        oSerialized = v            
                        print('--------------')
                        print('-- XMLFilenameOutput')
                        print('--    ',oSerialized.XMLFilenameOutput)
                        if oSerialized.Complete == 1:
                            print('Count',sourcedirectoryfull,iCount)
                            #destinationdirectoryfull = sourcedirectoryfull
                            
                            destinationdirectoryfull = sourcedirectoryfull.replace(replacelistforcreatingdestinationpath[0],replacelistforcreatingdestinationpath[1])
                            import mytools
                            mytools.general.make_sure_path_exists(destinationdirectoryfull)
                            print('Destination',destinationdirectoryfull)
                            import shutil
                            # Move src to dst (mv src dst)
                            shutil.rmtree(destinationdirectoryfull,ignore_errors=True, onerror=None)
                            shutil.move(sourcedirectoryfull, destinationdirectoryfull)
                
                
                         