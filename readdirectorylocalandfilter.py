# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 00:17:18 2014

@author: jmalinchak
"""
class read:
    def execute(directorylocal='',symbol='',expirationdate='',optiontype='',strike='',bucketquotedatetime='',showresults=1):
        import readintomemoryfilterresults

        dFull = readintomemoryfilterresults.read(directorylocal) 
        dFiltered = dFull.filterresults(symbol,expirationdate,optiontype,strike,bucketquotedatetime)
        if showresults == 1:
            for KeyOfOptionInstances,ValueOfOptionInstances in dFiltered.items():
                ValueOfOptionInstances.printdelim(' ')
        return dFiltered