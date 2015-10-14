# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 20:28:08 2015

@author: jmalinchak
"""
myticker = 'TWTR'
import os
topdirectory = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\\output\\calendarspreadcandidates'

d_terminaldirectories = {}
mydictionary = {}

for dirName, subdirList, fileList in os.walk(topdirectory):
    if len(subdirList) == 0:
        d_terminaldirectories[len(d_terminaldirectories)] = {'fullpath' : dirName}

from collections import OrderedDict
dOrderedDesc = OrderedDict(sorted(d_terminaldirectories.items(), key=lambda t: t[1]['fullpath'],reverse=True))

iCounter = 0

for d1, v1 in dOrderedDesc.items():
    for dirName, subdirList, fileList in os.walk(v1['fullpath']):
        if len(subdirList) == 0:
            for file in fileList:
                ls_file = file.split(' ', 4 )
                if len(ls_file) == 4:
                    #print(len(ls_file),file)
                    lastelement = file.split(' ', 4 )[3]
                    v_symbol = lastelement.split('.')[0]
                    if v_symbol == myticker:
                        print(file)
