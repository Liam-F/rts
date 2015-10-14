# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 10:57:01 2014

@author: jmalinchak
"""

import pulllpricesallfromdirectorylocalroot
import datetime
sdate = datetime.datetime.now().strftime("%Y-%m-%d")
stime = datetime.datetime.now().strftime("%H:%M:%S")
shour = stime.split(':')[0]
sminute = stime.split(':')[1]
print(int(sminute))
sminutenormal = '0'
if int(sminute) < 15:
    sminutenormal = '15'
if int(sminute) >= 15 and int(sminute) < 30:
    sminutenormal = '30'
if int(sminute) >= 30 and int(sminute) < 45:
    sminutenormal = '45'
if int(sminute) >= 45 and int(sminute) < 60:
    sminutenormal = '60'
print(stime)
print(sminute)
print(sminutenormal)

dest = "C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\downloads\\" + sdate + "\\" + shour + "\\" + sminutenormal

import shutil
shutil.rmtree(dest, ignore_errors=True)

################################################    
pulllpricesallfromdirectorylocalroot.pull(dest,
                                          'inputs\\Symbols.txt',
                                          'inputs\\Expirations.txt')
################################################

#                                          
#                                          
#C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\inputs\\Symbols.txt
#C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\inputs\\Expirations.txt
