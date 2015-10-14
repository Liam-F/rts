# -*- coding: utf-8 -*-
"""
Created on Wed Oct 07 15:26:51 2015

@author: justin.malinchak
"""

def say_hello(value, callback,name):
    print value
    callback(name)

def say_name(name):
     print name

say_hello('ciao', say_name,'Honny')
