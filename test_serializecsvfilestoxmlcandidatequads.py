# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 07:15:27 2015

@author: jmalinchak
"""
#This works

import serializecsvfilestoxmlcandidatequads

serializecsvfilestoxmlcandidatequads.read(downloadsdirectory = 'downloadsquad',
                 replacelistforcreatingdestinationpath = ['\\downloadsquad\\','\\downloadsquadprocessed\\'],
                 minpairspreadpercent = .64,
                 maxvalueatrisk = 1.5,
                 maxbidaskspreadpercentagesell = .25,
                 maxbidaskspreadpercentagebuy = .25,
                 showresults=1)                   