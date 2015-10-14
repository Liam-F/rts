# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 07:15:27 2015

@author: jmalinchak
"""
#This works

import serializeallcsvfilesindownloadsdirectorywithparameters
#serializeallcsvfilesindownloadsdirectorywithparameters.read('downloads',['\\downloads\\','\\downloadsprocessed\\'],1)
serializeallcsvfilesindownloadsdirectorywithparameters.read(downloadsdirectory = 'downloads',
                                 replacelistforcreatingdestinationpath = ['\\downloads\\','\\downloadsprocessed\\'],
                                 minpairspreadpercent = -1, #0.6
                                 maxvalueatrisk = 100, #2.4,
                                 maxbidaskspreadpercentagesell = 100, #= .25,
                                 maxbidaskspreadpercentagebuy = 100, #= .25,
                                 showresults=1
                                 )