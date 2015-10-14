# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 07:24:59 2015

@author: jmalinchak
"""
import os
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
topdirectory = 'C:\Documents and Settings\jmalinchak\My Documents\My Python\Active\py\downloads\\TEST\\01\\15'
print(topdirectory)
for (topdirectory, dirs, files) in os.walk(topdirectory):
    
    for directoryname in dirs:
        directoryname = os.path.join(topdirectory,directoryname)
        iCount = countfiles(directoryname,'.csv')
        print(str(iCount) + ' ' + directoryname)
        if iCount > 0:
            o = readfiltersortserializetobucketdirectories.read(directoryname)
        
#    for pathfilename in files:
#        pathfilename = os.path.join(topdirectory,pathfilename)
#        print(pathfilename)
#
#        o1 = deserializecandidatesxml.deserialize('C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\\output\\xml\\calendarspreads 20150119053018.xml')
#        d1 = o1.DictionaryOfCandidatesFromXML
#        print(len(d1))
#        for k,v in d1.items():
#            print(k,v['keyid'],v['calculations']['sortbymeasurevalue'],
#                  v['specifications']['symbol'],
#                  v['earlier']['optionsymbol'],
#                  v['earlier']['bucketquotedatetime'],
#                  v['calculations']['sortbymeasurename']
#                  )

