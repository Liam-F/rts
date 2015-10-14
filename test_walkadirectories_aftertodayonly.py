# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 18:32:16 2015

@author: jmalinchak
"""

import config
# Parameters
showresults = 0
mystatusofcandidatesfolder = config.mystatusofcandidatesfolder

# ##########
# Date setup
import datetime
today_datetime = datetime.datetime.today()
today_datestringforcsv = today_datetime.strftime('%Y-%m-%d %H:%M:%S.%f')
import time
millis = int(round(time.time() * 1000))
today_datestringforfilename = today_datetime.strftime('%Y-%m-%d %H.%M.%S ') + str(millis)
#yesterday_datetime = datetime.datetime.now() - timedelta(hours=24)
yesterday_datetime = datetime.date.fromordinal(datetime.date.today().toordinal()-1)

def optiontype(optionsymbol):
    import mytools
    ot = mytools.get_from_optionsymbol().optiontype(optionsymbol)
    return ot

def strike(optionsymbol):
    import mytools
    rstrike = mytools.get_from_optionsymbol().strike(optionsymbol)
    return rstrike

def make_strikelegsstring(openshortopenlongoptsym):
    #make_strikelegsstring('SPY150717C00212500-SPY150717C00213500-SPY150717P00206000-SPY150717P00205000')
    import mytools
    #openshortopenlongoptsym = 'SPY150717C00212500-SPY150717C00213500-SPY150717P00206000-SPY150717P00205000'
    optionsymbol_list = openshortopenlongoptsym.split('-')
    print optionsymbol_list
    strikelegsstring = ''
    for optionsymbol in optionsymbol_list:
        #print strikeleg
        strikeleg = mytools.get_from_optionsymbol().strike(optionsymbol)
        strikelegsstring = strikelegsstring + str(strikeleg) +'-'
    if len(strikelegsstring ) > 0:
        strikelegsstring = strikelegsstring[:-1]
    return strikelegsstring

import ntpath
def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def path_base(path):
    head, tail = ntpath.split(path)
    return head or ntpath.basename(head)    
#def getdictitem(thedict,key):

import config
import os
import pandas as pd
#import datetime
import numpy as np

myselectedcandidatesfolder = config.myselectedcandidatesfolder #'C:\\Batches\\rts\\output\\condor\\selected'
print 'myselectedcandidatesfolder: ' + myselectedcandidatesfolder
#filepathnames_list = []
#for filename in os.listdir(myselectedcandidatesfolder):
#    if filename.endswith(".csv") and filename.startswith('selectedcandidate'): 
#        #print(filename)
#        filepathnames_list.append(filename)
#        continue
#    else:
#        continue
#print(myselectedcandidatesfolder)
#from datetime import datetime
filepathnames_list = []
for (dirpath, dirnames, filenames) in os.walk(myselectedcandidatesfolder):
    #print dirpath, dirnames, filenames
    #for dirname in dirnames:
    for filename in filenames:
        if filename.endswith('.csv'): 
            #list_of_files[filename] = os.sep.join([dirpath, filename])
            #list_of_files[filename] = os.sep.join([dirpath, filename])
            print(os.sep.join([dirpath, filename]))
            date_in_filename = datetime.datetime.strptime(filename.split()[1],'%Y-%m-%d').date()
            print date_in_filename,yesterday_datetime ,date_in_filename>=yesterday_datetime
            if date_in_filename >= yesterday_datetime:
                filepathnames_list.append(os.sep.join([dirpath, filename]))

