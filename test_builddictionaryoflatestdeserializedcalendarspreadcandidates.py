# -*- coding: utf-8 -*-
"""
Created on Sun Feb  8 09:55:15 2015

@author: jmalinchak
"""
import builddictionaryoflatestdeserializedcalendarspreadcandidates
topdirectory = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\\output\\calendarspreadcandidates'
o1 = builddictionaryoflatestdeserializedcalendarspreadcandidates.build(topdirectory,5,['a','b'],1)
import serializedictionaryofcalendarspreadcandidates
o2 = serializedictionaryofcalendarspreadcandidates.serialize(o1.DictionaryOfDeserializedCalendarSpreadCandidates)
########################
# Copy file to webserver
import shutil
shutil.copy2(o2.XMLFilenameOutput, 'C:\\Inetpub\\wwwroot\\rtstock\candidates.xml')

print(o2.XMLFilenameOutput)