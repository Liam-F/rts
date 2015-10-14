# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 00:17:18 2014

@author: jmalinchak
"""
class verify:
    
    def __init__(self, programname):
        #self.ProgramRunning(programname)
        if self.IsProcessRunning(programname):
            print(programname + " is running, sir.")
        else:
            print(programname + " is running..... not.")
            
#    def ProgramRunning(self,programname):
#        import psutil
#        i = 0
#        programname in [psutil.Process(i).name for i in psutil.get_pid_list()]
#        print(i)
#    
    

    def WindowExists(self,classname):
        import win32ui
        try:
            win32ui.FindWindow(None, classname)
        except win32ui.error as e:
            print(str(e))
            return False
        else:
            return True
    
    def IsProcessRunning(self, process ):
        import re
        import subprocess
        print("x")
        s = subprocess.Popen(process,stdout=subprocess.PIPE)
        print("y")
        for x in s.stdout:
            if re.search(process, x):
                return True

        print('x')        
        return False
#    def ProgramRunning(self,programname):
#        import win32ui
#        # may need FindWindow("iTunes", None) or FindWindow(None, "iTunes")
#        # or something similar
#        if FindWindow(programname, programname):
#            print("Found " + programname + " window")
#            return True