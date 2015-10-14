# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 05:35:22 2015

@author: jmalinchak
"""


def countfiles(path,extension = ''):
  list_dir = []
  list_dir = os.listdir(path)
  count = 0
  for file in list_dir:
    if file.endswith(extension): # eg: '.txt'
      count += 1
  return count
  


## ########################
## How to get top directory
import os
downloadsdir_root = os.path.join(os.getcwd(),'downloads')
import mytools
downloadsdir_bucketdatetime = mytools.mystrings.appendnormaldateddirectorybasedoncurrenttime15(downloadsdir_root)
print(downloadsdir_bucketdatetime)
downloadsdir_hour = os.path.dirname(downloadsdir_bucketdatetime)
print('downloadsdir_hour','=',downloadsdir_hour)
downloadsdir_day = os.path.dirname(downloadsdir_hour)

## #############################
## directory for processed files
replacedirectory = ['\\downloads\\','\\downloadsprocessed\\']

## ####################
## Process downloads directories
import readfiltersortserializetobucketdirectories
iCount = 0
for root, dirs, files in os.walk(downloadsdir_root):
    for name in dirs:
        downloadsdir_check = os.path.join(root, name)
        iCount = countfiles(downloadsdir_check,'.csv')
        print(iCount,downloadsdir_check)
#        ## ###################################
        if iCount > 0:
            sourcedirectoryfull = downloadsdir_check
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
                    destinationdirectoryfull = sourcedirectoryfull.replace(replacedirectory[0],replacedirectory[1])
                    import mytools
                    mytools.general.make_sure_path_exists(destinationdirectoryfull)
                    print('Destination',destinationdirectoryfull)
                    import shutil
                    # Move src to dst (mv src dst)
                    shutil.rmtree(destinationdirectoryfull,ignore_errors=True, onerror=None)
                    shutil.move(sourcedirectoryfull, destinationdirectoryfull)
        
    
             