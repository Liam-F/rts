# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 15:52:33 2015

@author: jmalinchak
"""

# testfile = C:\Documents and Settings\jmalinchak\My Documents\My Python\Active\py\output\xml\calendarspreads 20150117154646.xml

# How to read xml file into memory

class deserialize:
    
    def __init__(self, pathfilename,showresults=0):
        print('initialized class deserializecandidatesxml')
        if showresults == 1:
            print('showresults=' + str(showresults) + ' readintomemoryprocessallfilesindirectorylocal')
        #self.loop_through_optionsfiles(pathfilename)
        self.DictionaryOfCandidatesFromXML = {}
        self.CandidateSourcePathFileName = ''
        self.processxmlfile(pathfilename,showresults)

    def set_CandidateSourcePathFileName(self,CandidateSourcePathFileName):
        self._CandidateSourcePathFileName = CandidateSourcePathFileName
    def get_CandidateSourcePathFileName(self):
        return self._CandidateSourcePathFileName
    CandidateSourcePathFileName = property(get_CandidateSourcePathFileName, set_CandidateSourcePathFileName)   

    def set_DictionaryOfCandidatesFromXML(self,DictionaryOfCandidatesFromXML):
        self._DictionaryOfCandidatesFromXML = DictionaryOfCandidatesFromXML
    def get_DictionaryOfCandidatesFromXML(self):
        return self._DictionaryOfCandidatesFromXML
    DictionaryOfCandidatesFromXML = property(get_DictionaryOfCandidatesFromXML, set_DictionaryOfCandidatesFromXML)   

    def processxmlfile(self,pathfilename,showresults):
        
        self.CandidateSourcePathFileName = pathfilename
        
        print('***********', pathfilename)
        
        import os
        if len(pathfilename) > 0 and os.path.exists(pathfilename):
        
            import xml.etree.ElementTree as ET
            tree = ET.ElementTree(file=pathfilename)
            dCandidates = {}
    
    
            
            for keyid in tree.iter(tag='keyid'):
    
                d_specifications = {}
                d_calculations = {}
                d_earlier = {}
                d_later = {}
    
                for specifications in keyid.iter(tag='specifications'):
                    for e in specifications.iter():
                        d_specifications[e.tag] = e.text
                        #print('---','specifications',keyid.attrib['value'],e.tag,e.text)
                for calculations in keyid.iter(tag='calculations'):
                    for e in calculations.iter():
                        d_calculations[e.tag] = e.text
                        #print('---','calculations',keyid.attrib['value'],e.tag,e.text)
                for earlier in keyid.iter(tag='earlier'):
                    for e in earlier.iter():
                        d_earlier[e.tag] = e.text
                        #print('---','earlier',keyid.attrib['value'],e.tag,e.text)
                for later in keyid.iter(tag='later'):
                    for e in later.iter():
                        d_later[e.tag] = e.text
                        #print('---','later',keyid.attrib['value'],e.tag,e.text)
                
                #dCandidates[len(dCandidates)] = keyid.attrib['value'], d_specifications, d_calculations, d_earlier, d_later
                dCandidates[len(dCandidates)] = { 'keyid' : keyid.attrib['value'], 'specifications' : d_specifications, 'calculations' : d_calculations, 'earlier' : d_earlier, 'later' : d_later }
                
            self.DictionaryOfCandidatesFromXML = dCandidates