# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 07:24:59 2015

@author: jmalinchak
"""

from datetime import datetime
starttime = datetime.now()

#datetime.strptime(t1, TIME_FORMAT2) - datetime.strptime(t2, TIME_FORMAT2)
#_.total_seconds()
#-9.254

showresults = 0
import os

#topdirectory = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\\output\\calendarspreadcandidates\\2015-01-21\\00\\45'
#topdirectory = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\\output\\calendarspreadcandidates\\2015-01-21\\00'
#topdirectory = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\\output\\calendarspreadcandidates\\2015-01-21\\00 archive'
topdirectory = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\\output\\calendarspreadcandidates'
fulldictionary = {}
mydictionary = {}

for dirName, subdirList, fileList in os.walk(topdirectory):
    if len(subdirList) == 0:
        fulldictionary[len(fulldictionary)] = dirName

for x in range(1, 4):
    mydictionary[len(mydictionary)] = fulldictionary[len(fulldictionary) - x]
    print(mydictionary[len(mydictionary)-1])