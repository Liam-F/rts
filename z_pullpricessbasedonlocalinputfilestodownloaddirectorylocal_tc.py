# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 00:17:18 2014

@author: jmalinchak
"""


class pull:
    def __init__(self,
                 pathinputfilelocalsymbols='inputs\\SymbolsTest.txt',
                 pathinputfilelocalexpirations='inputs\\ExpirationsTest.txt',
                 rootlocalforfilespulled='downloads',
                 showresults=1):
                     
        self.execute_results(pathinputfilelocalsymbols,pathinputfilelocalexpirations,rootlocalforfilespulled,showresults)
    
    def set_DownloadDirectoryLocal(self,DownloadDirectoryLocal):
        self._DownloadDirectoryLocal = DownloadDirectoryLocal
    def get_DownloadDirectoryLocal(self):
        return self._DownloadDirectoryLocal
    DownloadDirectoryLocal = property(get_DownloadDirectoryLocal, set_DownloadDirectoryLocal)    
    
    def execute_results(self,pathinputfilelocalsymbols,pathinputfilelocalexpirations,rootlocalforfilespulled,showresults):
        ################################################    
        #
        # Returns downloaddirectorylocal
        #
        ################################################    
        import mytools
        downloaddirectorylocal = mytools.mystrings.appendnormaldateddirectorybasedoncurrenttime15(rootlocalforfilespulled)
        print('downloaddirectorylocal=' + downloaddirectorylocal)
        ################################################    
        # This would remove the entire tree from the date\hour\bucket
        #   removal should be done at the file level so that multiple process can run concurrently
#        import shutil
#        shutil.rmtree(downloaddirectorylocal, ignore_errors=True)
        
        ################################################    
        import pullpricesallfromdirectorylocalroot
        pullpricesallfromdirectorylocalroot.pull(downloaddirectorylocal,
                                                  pathinputfilelocalsymbols,
                                                  pathinputfilelocalexpirations)
        ################################################
        print('return value: DownloadDirectoryLocal= ' + downloaddirectorylocal)
        self.DownloadDirectoryLocal=downloaddirectorylocal