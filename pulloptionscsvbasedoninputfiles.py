# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 00:17:18 2014

@author: jmalinchak
"""


class pull:
    def __init__(self,
                 pathfilelocalsymbols='inputs\\SymbolsTest.txt',
                 pathfilelocalexpirations='inputs\\ExpirationsTest.txt',
                 rootlocalforfilespulled='downloads',
                 showresults=1):
        
        print('initialized pulloptionscsvbasedoninputfiles.py ')
        self.optionprices(pathfilelocalsymbols,pathfilelocalexpirations,rootlocalforfilespulled,showresults)
    
    def set_OutputPathString(self,OutputPathString):
        self._OutputPathString = OutputPathString
    def get_OutputPathString(self):
        return self._OutputPathString
    OutputPathString = property(get_OutputPathString, set_OutputPathString)    
    
    def optionprices(self,pathfilelocalsymbols,pathfilelocalexpirations,rootlocalforfilespulled,showresults):
        ################################################    
        #
        # Returns file name of output
        #
        ################################################    
        import mytools
        downloaddirectorylocal = mytools.mystrings.appendnormaldateddirectorybasedoncurrenttime15(rootlocalforfilespulled)
        print('downloaddirectorylocal=' + downloaddirectorylocal)
        ################################################    
        import shutil
        shutil.rmtree(downloaddirectorylocal, ignore_errors=True)
        
        ################################################    
        import pullpricesallfromdirectorylocalroot
        pullpricesallfromdirectorylocalroot.pull(downloaddirectorylocal,
                                                  pathfilelocalsymbols,
                                                  pathfilelocalexpirations)
        
        self.OutputPathString = downloaddirectorylocal
        ################################################
