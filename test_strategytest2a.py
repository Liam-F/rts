# -*- coding: utf-8 -*-
"""
Created on Sun Dec 14 11:52:03 2014

@author: jmalinchak
"""

import strategytest
o = strategytest.calendarspreadslive()
fn = o.OutputFilePathString
import os
print('heres your file: ' + os.getcwd() + '\\' + fn)