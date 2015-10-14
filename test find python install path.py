# -*- coding: utf-8 -*-
"""
Created on Wed Jul 01 15:57:08 2015

@author: Justin.Malinchak
"""

import os
try:
    user_paths = os.environ['PYTHONPATH'].split(os.pathsep)
except KeyError:
    user_paths = []

print user_paths

import sys
print sys.path
