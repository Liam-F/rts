# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 00:17:18 2014

@author: jmalinchak
"""

import readintomemoryfilterresults

dFull = readintomemoryfilterresults.read('C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\Active\\downloads\\20141130a') #\\a20141130
dFiltered = dFull.filterresults('FB','2014-12-20','C','80','')
for KeyOfOptionInstances,ValueOfOptionInstances in dFiltered.items():
    print(ValueOfOptionInstances.quotedatetime)