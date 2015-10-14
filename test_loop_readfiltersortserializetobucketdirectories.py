# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 07:24:59 2015

@author: jmalinchak
"""
import readfiltersortserializetobucketdirectories
#import deserializecandidatesxml

d1 = {}
d2 = {}

def countfiles(path,extension = ''):
  list_dir = []
  list_dir = os.listdir(path)
  count = 0
  for file in list_dir:
    if file.endswith(extension): # eg: '.txt'
      count += 1
  return count
  
iCount = 0

## ########################
## How to get top directory
import os
downloadsroot = os.path.join(os.getcwd(),'downloads')
import mytools
downloadsdir_bucketdatetime = mytools.mystrings.appendnormaldateddirectorybasedoncurrenttime15(downloadsroot)
print(downloadsdir_bucketdatetime)
downloadsdir_hour = os.path.dirname(downloadsdir_bucketdatetime)
print('downloadsdir_hour','=',downloadsdir_hour)
downloadsdir_day = os.path.dirname(downloadsdir_hour)

topdirectory = downloadsdir_day
print('topdirectory','=',topdirectory)

## #############################
## directory for processed files
replacedirectory = ['\\downloads\\','\\downloadsprocessed\\']
processeddirectory = topdirectory.replace(replacedirectory[0],replacedirectory[1])
print('processeddirectory','=',processeddirectory)

#topdirectory = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\\downloads\\TEST\\01\\15'
#topdirectory = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\\downloads\\2015-01-21\\00\\30'
#topdirectory = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\\downloads\\2015-01-14\\22\\30'
#topdirectory = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\\downloads\\2015-01-25\\22\\15'
#topdirectory = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\downloads\\2015-01-27\\23\\30'
#for subdir, dirs, files in os.walk(rootdir):
#    runningsumofxmlfiles = runningsumofxmlfiles + len(files)
#    for file in files:        
#        pathfilenamecandidatexml = os.path.join(subdir, file)
        
for (topdirectory, dirs, files) in os.walk(topdirectory):
    print('looping '+topdirectory)
    for sourcedirectoryname in dirs:
        sourcedirectoryfull = os.path.join(topdirectory,sourcedirectoryname)
        iCount = countfiles(sourcedirectoryfull,'.csv')
        #print('loop',sourcedirectoryfull)
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
                mytools.general.make_sure_path_exists(processeddirectory)
                print('Destination',destinationdirectoryfull)
                import shutil
                # Move src to dst (mv src dst)
                shutil.rmtree(destinationdirectoryfull,ignore_errors=True, onerror=None)
                shutil.move(sourcedirectoryfull, destinationdirectoryfull)
                # Copy src to dst. (cp src dst)
                #shutil.copy(src, dst)
                
                # Copy files, but preserve metadata (cp -p src dst)
                #shutil.copy2(src, dst)
                
                # Copy directory tree (cp -R src dst)
                #shutil.copytree(src, dst)

#for root, dirs, files in os.walk(os.getcwd()):
#    for name in dirs:
#        try:
#            os.rmdir(os.path.join(root, name))
#        except WindowsError:
#            print('Cannot delete (not empty)', os.path.join(root, name))


    