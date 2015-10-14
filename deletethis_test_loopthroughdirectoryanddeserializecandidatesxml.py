# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 07:24:59 2015

@author: jmalinchak
"""
import os
import deserializecandidatesxml

d1 = {}
d2 = {}

topdirectory = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\\output\\calendarspreadcandidates\\2015-01-21\\00\\45'
#topdirectory = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\\output\\calendarspreadcandidates\\2015-01-21\\00'

rootdir = topdirectory 

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        pathfilenamecandidatexml = os.path.join(subdir, file)
        print('-----------------------------')
        print('--  ',pathfilenamecandidatexml)
        


        o1 = deserializecandidatesxml.deserialize(pathfilenamecandidatexml)
        d1 = o1.DictionaryOfCandidatesFromXML
        print(len(d1))
        for k,v in d1.items():
            print(
                k
                ,  v['keyid']
                ,  v['calculations']['sortbymeasurevalue']
                ,  v['calculations']['sortbymeasurename']
                ,  v['specifications']['symbol']
                ,  v['earlier']['optionsymbol']
                ,  v['earlier']['bucketquotedatetime']
                )

