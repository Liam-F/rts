# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 07:24:59 2015

@author: jmalinchak
"""

import deserializecandidatesxml
o1 = deserializecandidatesxml.deserialize('C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\\output\\xml\\calendarspreads 20150119053018.xml')
d1 = o1.DictionaryOfCandidatesFromXML
print(len(d1))
for k,v in d1.items():
    print(k,v['keyid'],v['calculations']['sortbymeasurevalue'],
          v['specifications']['symbol'],
          v['earlier']['optionsymbol'],
          v['earlier']['bucketquotedatetime'],
          v['calculations']['sortbymeasurename']
          )

o2 = deserializecandidatesxml.deserialize('C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\\output\\xml\\calendarspreads 20150119172619.xml')
d2 = o2.DictionaryOfCandidatesFromXML
print(len(d2))
for k,v in d2.items():
    print(k,v['keyid'],v['calculations']['sortbymeasurevalue'],
          v['specifications']['symbol'],
          v['earlier']['optionsymbol'],
          v['earlier']['bucketquotedatetime'],
          v['calculations']['sortbymeasurename']
          )

print('Count of Candidates 1:',len(o1.DictionaryOfCandidatesFromXML))
print('Count of Candidates 2:',len(o2.DictionaryOfCandidatesFromXML))