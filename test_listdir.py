# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 12:43:56 2015

@author: justin.malinchak
"""
import ntpath
def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)
def path_base(path):
    head, tail = ntpath.split(path)
    return head or ntpath.basename(head)    
    
import config
import os
myselectedcandidatesfolder = config.myselectedcandidatesfolder #'C:\\Batches\\rts\\output\\condor\\selected'
filenames_list = []
for filename in os.listdir(myselectedcandidatesfolder):
    if filename.endswith(".csv") and filename.startswith('selectedcandidate'): 
        print(filename)
        filenames_list.append(filename)
        continue
    else:
        continue
print(myselectedcandidatesfolder)

list_of_files = {}
for (dirpath, dirnames, filenames) in os.walk(myselectedcandidatesfolder):
    #print dirpath, dirnames, filenames
    #for dirname in dirnames:
    for filename in filenames:
        if filename.endswith('.csv'): 
            #list_of_files[filename] = os.sep.join([dirpath, filename])
            #list_of_files[filename] = os.sep.join([dirpath, filename])
            filepathname = os.sep.join([dirpath, filename])
            print path_base(filepathname)
print '--------------'

#print list_of_files