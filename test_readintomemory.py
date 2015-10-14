# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 00:17:18 2014

@author: jmalinchak
"""

import readintomemory

oMemoryObject = readintomemory.read(directorylocal='C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\Active\\downloads\\20141130b',symbol='KMI',expirationdate='2014-12-20',optiontype='C')
d = oMemoryObject.DictionaryOfFilteredInstances
for KeyOfOptionInstances,ValueOfOptionInstances in d.items():
    ValueOfOptionInstances.printdelim('|')