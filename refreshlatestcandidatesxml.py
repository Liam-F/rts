# -*- coding: utf-8 -*-
"""
Created on Sun Feb  8 09:55:15 2015

@author: jmalinchak
"""
print('started')
import builddictionaryoflatestdeserializedcalendarspreadcandidates
topdirectory = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\\output\\calendarspreadcandidates'
numberofbucketquotedatetimesbacktouse = 4
d_excludesymbols = {}
d_excludesymbols[len(d_excludesymbols)] = 'DXJ'
d_excludesymbols[len(d_excludesymbols)] = 'HFC'
d_excludesymbols[len(d_excludesymbols)] = 'VIPS'
d_excludesymbols[len(d_excludesymbols)] = 'WYNN'

o1 = builddictionaryoflatestdeserializedcalendarspreadcandidates.build(topdirectory,numberofbucketquotedatetimesbacktouse,d_excludesymbols,1)
import serializedictionaryofcalendarspreadcandidates
o2 = serializedictionaryofcalendarspreadcandidates.serialize(o1.DictionaryOfDeserializedCalendarSpreadCandidates,500,0)
print('DictionaryOfExcludedSymbols','=',o1.DictionaryOfExcludedSymbols)
print('XMLFilenameOutput','=',o2.XMLFilenameOutput)

########################
# Copy file to webserver
import shutil

naspathwebfile='X:\\www\\rtstock\\calendarspread\candidates.xml'
shutil.copy2(o2.XMLFilenameOutput, naspathwebfile)
print('Copied candidate file to',naspathwebfile)

fullpathwebfile='C:\\Inetpub\\wwwroot\\rtstock\\calendarspread\\candidates.xml'
shutil.copy2(o2.XMLFilenameOutput, fullpathwebfile)
print('Copied candidate file to',fullpathwebfile)

import mytools
mydate14 = mytools.mystrings.ConvertDatetime14()
mydate10 = mydate14[:10]

import mytools
mydate14 = mytools.mystrings.ConvertDatetime14()
mydate10 = mydate14[:10]
import os
archivepathwebfile=os.path.join('c:','\Inetpub','wwwroot','rtstock','calendarspread','archive',mydate10+'.xml')
mytools.general.make_sure_filepath_exists(archivepathwebfile)
shutil.copy2(o2.XMLFilenameOutput, archivepathwebfile)
print('Copied candidate file to',archivepathwebfile)
