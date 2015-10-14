# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 02:54:07 2015

@author: jmalinchak
"""

# Import the os module, for the os.walk function
import os
import datetime
import time
def SubDirPath (d):
    return filter(os.path.isdir, [os.path.join(d,f) for f in os.listdir(d)])
    
# Set the directory you want to start from
rootDir = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\\output\\calendarspreadcandidates'
currentDir = 'xxx'
datefound = '1980-01-01'
dummy = 0
newpath = 'xxx'
for dirName, subdirList, fileList in os.walk(rootDir):
    currentDir = dirName
    #print('Found directory: %s' % currentDir)
    dirname1 = os.path.basename(currentDir) 
    try:
        date = time.strptime(dirname1, '%Y-%m-%d')
        datefound = dirname1
    except ValueError:
        dummy = 0
if datefound != '1980-01-01':
    newPath = os.path.join(rootDir,datefound)
    
    ls = list(filter(os.path.isdir, [os.path.join(newPath,f) for f in os.listdir(newPath)]))
    
    latestcandidatexmldirectory = ls[len(ls)-1]
    print(latestcandidatexmldirectory)
    import deserializedirectoryofcandidatexml
    deserializedirectoryofcandidatexml.deserialize(latestcandidatexmldirectory)
#        dirname1 = os.path.basename(currentDir) 
#        try:
#            date = time.strptime(dirname1, '%Y-%m-%d')
#            datefound = dirname1
#        except ValueError:
#            dummy = 0

    #for fname in fileList:
    #    print('\t%s' % fname)