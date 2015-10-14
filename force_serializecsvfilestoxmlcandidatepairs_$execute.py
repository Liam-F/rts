# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 03:28:47 2015

@author: jmalinchak
"""

import serializecsvfilestoxmlcandidatepairs
o = serializecsvfilestoxmlcandidatepairs.read(downloadsdirectory = '$execute',
                                             replacelistforcreatingdestinationpath = ['\\$execute\\','\\$executeprocessed\\'],
                                             minpairspreadpercent = 0.1,
                                             maxvalueatrisk = 10,
                                             maxbidaskspreadpercentagesell = 1,
                                             maxbidaskspreadpercentagebuy = 1,
                                             showresults=1)