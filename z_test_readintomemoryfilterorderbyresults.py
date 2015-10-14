# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 00:17:18 2014

@author: jmalinchak
"""
class read:
    def filterandsortresults(directorylocal,symbol,expirationdate,optiontype,strike,bucketquotedatetime,orderby)
        import readintomemoryfilterresults

        dFull = readintomemoryfilterresults.read('C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\Active\\downloads\\20141130b') #\\a20141130
        dFiltered = dFull.filterresults(symbol,expirationdate,optiontype,strike,bucketquotedatetime)
        for KeyOfOptionInstances,ValueOfOptionInstances in dFiltered.items():
            ValueOfOptionInstances.printdelim(' ')