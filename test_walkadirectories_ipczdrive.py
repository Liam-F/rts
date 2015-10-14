# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 18:32:16 2015

@author: jmalinchak
"""
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

#import os, time
#filepathnames_list = []
#for (dirpath, dirnames, filenames) in os.walk('Z:\\2015\\Q2'):
#    #print dirpath, dirnames, filenames
#    #for dirname in dirnames:
#    for filename in filenames:
#        if filename.endswith('.pdf'): 
#            #list_of_files[filename] = os.sep.join([dirpath, filename])
#            #list_of_files[filename] = os.sep.join([dirpath, filename])
#            fullpath = os.sep.join([dirpath, filename])
#            (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(fullpath)
#            print(fullpath,time.ctime(mtime))
#            #date_in_filename = datetime.datetime.strptime(filename.split()[1],'%Y-%m-%d').date()
#            filepathnames_list.append(fullpath)


import os
filepathnames_list = []
dirpath = 'Z:\\2015\\Q2'
for filename in os.listdir(dirpath):
    
    if filename.endswith(".pdf"): 
        fullpath = os.sep.join([dirpath, filename])        
        (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(fullpath)
        filetime = time.ctime(mtime)
        velement = filename.split('.')[1]
        if velement.isdigit():
            try:
                os.remove(fullpath)
                print 'removed',fullpath,'because it has numeric in the 2nd element'
            except:
                print 'there was some problem with',fullpath
            
        
        
        

