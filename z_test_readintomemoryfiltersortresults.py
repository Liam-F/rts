# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 00:17:18 2014

@author: jmalinchak
"""
class readandfilter:
    def execute(directorylocal,symbol,expirationdate,optiontype,strike,bucketquotedatetime)
        import readintomemoryfilterresults

        dFull = readintomemoryfilterresults.read('C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\Active\\downloads\\20141130b') #\\a20141130
        dFiltered = dFull.filterresults('KMI','2014-12-20','C','','')
        for KeyOfOptionInstances,ValueOfOptionInstances in dFiltered.items():
            ValueOfOptionInstances.printdelim(' ')