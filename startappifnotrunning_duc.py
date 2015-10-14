# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 07:19:36 2014

@author: jmalinchak
"""

import checkifprogramisrunning as c
tf = c.check.wildcard("DUC")
print(tf)
if not(tf is None):
    print('program is already running')
if tf is None:
#    import os
#    os.system('start "C:\\Program Files\\No-IP\\DUC40.exe"')
    import win32api # if active state python is installed or install pywin32 package seperately
    try: win32api.WinExec('"C:\\Program Files\\No-IP\\DUC40.exe"') # Works seamlessly
    except: pass