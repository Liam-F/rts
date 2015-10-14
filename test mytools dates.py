# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 12:59:36 2015

@author: jmalinchak
"""

import mytools
mydate14 = mytools.mystrings.ConvertDatetime14()
mydate10 = mydate14[:10]
import os
archivepathwebfile=os.path.join('c:','\Inetpub','wwwroot','rtstock','calendarspread','archive',mydate10+'.xml')
mytools.general.make_sure_filepath_exists(archivepathwebfile)
print(archivepathwebfile)