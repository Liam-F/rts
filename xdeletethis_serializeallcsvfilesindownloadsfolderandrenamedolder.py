# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 05:35:22 2015

@author: jmalinchak
"""

class read:
    
    def __init__(self,
                 downloadsfolder = 'downloads',
                 replacelistforcreatingdestinationpath = ['\\downloads\\','\\downloadsprocessed\\'],
                 showresults=0):
        print('initialized class serializeallcsvfilesindownloadsfolder')
        if showresults == 1:
            print('showresults=' + str(showresults) + ' readintomemoryprocessallfilesindirectorylocal')
        
        self.serialize(downloadsfolder,replacelistforcreatingdestinationpath,showresults)
    
#    def set_DictionaryOfSerializedFileObjects(self,DictionaryOfSerializedFileObjects):
#        self._DictionaryOfSerializedFileObjects = DictionaryOfSerializedFileObjects
#    def get_DictionaryOfSerializedFileObjects(self):
#        return self._DictionaryOfSerializedFileObjects
#    DictionaryOfSerializedFileObjects = property(get_DictionaryOfSerializedFileObjects, set_DictionaryOfSerializedFileObjects)   

    def countfiles(self,path,extension = ''):
        import os
        list_dir = []
        list_dir = os.listdir(path)
        count = 0
        for file in list_dir:
            if file.endswith(extension): # eg: '.txt'
                count += 1
        return count
  

    def serialize(self,downloadsfolder,replacelistforcreatingdestinationpath,showresults):
        from os.path import normpath, basename
        ## ########################
        ## How to get top directory
        import os
        downloadsdir_root = os.path.join(os.getcwd(),downloadsfolder)
    #    import mytools
    #    downloadsdir_bucketdatetime = mytools.mystrings.appendnormaldateddirectorybasedoncurrenttime15(downloadsdir_root)
    #    print(downloadsdir_bucketdatetime)
    #    downloadsdir_hour = os.path.dirname(downloadsdir_bucketdatetime)
    #    print('downloadsdir_hour','=',downloadsdir_hour)
    #    downloadsdir_day = os.path.dirname(downloadsdir_hour)
    #    
        ## #############################
        ## directory for processed files
        #replacedirectory = ['\\downloads\\','\\downloadsprocessed\\']
        
        ## ####################
        ## Process downloads directories
        import readfiltersortserializetobucketdirectories
        iCount = 0
        for root, dirs, files in os.walk(downloadsdir_root):
            for name in dirs:
                downloadsdir_check = os.path.join(root, name)
                iCount = self.countfiles(downloadsdir_check,'.csv')
                print(iCount,downloadsdir_check)
        #        ## ###################################
                if iCount > 0:
                    sourcedirectoryfull = downloadsdir_check
                    sourcebasename = basename(normpath(sourcedirectoryfull))
                    if sourcebasename[:2] !=  'x-':
                        o = readfiltersortserializetobucketdirectories.read(sourcedirectoryfull,
                             minpairspreadpercent = 0.6,
                             maxvalueatrisk = 2.4,
                             maxbidaskspreadpercentagesell = 0.25,
                             maxbidaskspreadpercentagebuy = 0.25,
                             sortbymeasure = 'spreadpercentageopen') # spreadpercentageopen | valueatriskopen
                                     
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
                                
                                basename = basename(normpath(sourcedirectoryfull))
                                
                                destinationdirectoryfull = os.path.join(os.path.dirname(sourcedirectoryfull),'x-' + basename)
                                #os.rename(sourcedirectoryfull,destinationdirectoryfull)
    #                            destinationdirectoryfull = sourcedirectoryfull.replace(replacedirectory[0],replacedirectory[1])
    #                            import mytools
    #                            mytools.general.make_sure_path_exists(destinationdirectoryfull)
    #                            print('Destination',destinationdirectoryfull)
    #                            import shutil
    #                            # Move src to dst (mv src dst)
    #                            shutil.rmtree(destinationdirectoryfull,ignore_errors=True, onerror=None)
    #                            shutil.move(sourcedirectoryfull, destinationdirectoryfull)
                    
                
                         