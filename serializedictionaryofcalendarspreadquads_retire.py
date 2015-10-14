# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 20:12:27 2014

@author: jmalinchak
"""

class serialize:
    def __init__(self,
                 dictionaryofcalendarspreadquads,
                 maxnumberofcandidates = 1000,
                 showresults=0):
        print('initialized class serializedictionaryofcalendarspreadquadstoxml.py ')
        self.execute_serialize(dictionaryofcalendarspreadquads,maxnumberofcandidates,showresults)

#    def set_DictionaryOfQualifiedPairsInput(self,DictionaryOfQualifiedPairsInput):
#        self._DictionaryOfQualifiedPairsInput = DictionaryOfQualifiedPairsInput
#    def get_DictionaryOfQualifiedPairsInput(self):
#        return self._DictionaryOfQualifiedPairsInput
#    DictionaryOfQualifiedPairsInput = property(get_DictionaryOfQualifiedPairsInput, set_DictionaryOfQualifiedPairsInput)   
    
    def set_XMLFilenameOutput(self,XMLFilenameOutput):
        self._XMLFilenameOutput = XMLFilenameOutput
    def get_XMLFilenameOutput(self):
        return self._XMLFilenameOutput
    XMLFilenameOutput = property(get_XMLFilenameOutput, set_XMLFilenameOutput)   
    
#    def set_DownloadDirectoryLocalInput(self,DownloadDirectoryLocalInput):
#        self._DownloadDirectoryLocalInput = DownloadDirectoryLocalInput
#    def get_DownloadDirectoryLocalInput(self):
#        return self._DownloadDirectoryLocalInput
#    DownloadDirectoryLocalInput = property(get_DownloadDirectoryLocalInput, set_DownloadDirectoryLocalInput)    

#    def set_SortbyMeasure(self,SortbyMeasure):
#        self._SortbyMeasure = SortbyMeasure
#    def get_SortbyMeasure(self):
#        return self._SortbyMeasure
#    SortbyMeasure = property(get_SortbyMeasure, set_SortbyMeasure)    

    
    def execute_serialize(self,dictionaryofcalendarspreadquads,maxnumberofcandidates,showresults):
        print('------')
        import mytools
        datetimestring = mytools.mystrings.datetimenormal()
        
        import xml.etree.cElementTree as ET
        
        root = ET.Element("rtstock")
        
        doc = ET.SubElement(root, "calendarspreads")
        doc.set("latest", datetimestring)
        
        #totalnumberofcandidates = len(dictionaryofcalendarspreadquads)
        icandidate = 0
        for k,v in dictionaryofcalendarspreadquads.items():
            icandidate = icandidate + 1
            #if icandidate > totalnumberofcandidates - maxnumberofcandidates:
            if icandidate <= maxnumberofcandidates:
                #earlier = v['earlier']
                #later = v['later']
                node_keyid = ET.SubElement(doc,"keyid")
                node_keyid.set("value", str(k))
                #node_keyid.text = str(k)
    
                ######################################################################
                node_specifications = ET.SubElement(node_keyid,"specifications")
                node_specifications_symbol = ET.SubElement(node_specifications,"symbol")
                #node_specifications_symbol.text = str(earlier.symbol)
                node_specifications_symbol.text = v['specifications']['symbol']
                #,v['calculations']['sortbymeasurename'],v['calculations']['sortbymeasurevalue']
                
                node_specifications_stockprice = ET.SubElement(node_specifications,"stockprice")
                node_specifications_stockprice.text = str(v['specifications']['stockprice'])
                node_specifications_bucketquotedatetime = ET.SubElement(node_specifications,"bucketquotedatetime")
                node_specifications_bucketquotedatetime.text = str(v['specifications']['bucketquotedatetime'])
                
                ######################################################################
                node_calculations = ET.SubElement(node_keyid,"calculations")
                
                node_calculations_sortbymeasurevalue = ET.SubElement(node_calculations,'sortbymeasurevalue')
                node_calculations_sortbymeasurevalue.text = v['calculations']['sortbymeasurevalue']
    
                node_calculations_sortbymeasurename = ET.SubElement(node_calculations,"sortbymeasurename")
                node_calculations_sortbymeasurename.text = v['calculations']['sortbymeasurename']
    
    
    
                node_calculations_spreadpercentageopen = ET.SubElement(node_calculations,"spreadpercentageopen")
                node_calculations_spreadpercentageopen.text = v['calculations']['spreadpercentageopen'] # str(round(float(earlier.bid)/float(later.ask),3))
    
                node_calculations_valueatriskopen = ET.SubElement(node_calculations,"valueatriskopen")
                node_calculations_valueatriskopen.text = v['calculations']['valueatriskopen']
                
                ######################################################################
                node_earlier = ET.SubElement(node_keyid ,"earlier")
    
                node_earlier_optionsymbol = ET.SubElement(node_earlier,"optionsymbol")
                node_earlier_optionsymbol.text = v['earlier']['optionsymbol']
    
                node_earlier_bucketquotedatetime = ET.SubElement(node_earlier,"bucketquotedatetime")
                node_earlier_bucketquotedatetime.text = str(v['earlier']['bucketquotedatetime'])
    
    
                node_earlier_quotedatetime = ET.SubElement(node_earlier,"quotedatetime")
                node_earlier_quotedatetime.text = str(v['earlier']['quotedatetime'])
                
                
                node_earlier_bid = ET.SubElement(node_earlier,"bid")
                node_earlier_bid.text = str(v['earlier']['bid'])
    
                node_earlier_ask = ET.SubElement(node_earlier,"ask")
                node_earlier_ask.text = str(v['earlier']['ask'])
    
                node_earlier_impliedvolatility = ET.SubElement(node_earlier,"impliedvolatility")
                node_earlier_impliedvolatility.text =str(v['earlier']['impliedvolatility'])
                
                ######################################################################
                node_later = ET.SubElement(node_keyid ,"later")
    
                node_later_optionsymbol = ET.SubElement(node_later,"optionsymbol")
                node_later_optionsymbol.text = v['later']['optionsymbol']
    
                node_later_bucketquotedatetime = ET.SubElement(node_later,"bucketquotedatetime")
                node_later_bucketquotedatetime.text = str(v['later']['bucketquotedatetime'])
    
    
                node_later_quotedatetime = ET.SubElement(node_later,"quotedatetime")
                node_later_quotedatetime.text = str(v['later']['quotedatetime'])
                
                
                node_later_bid = ET.SubElement(node_later,"bid")
                node_later_bid.text = str(v['later']['bid'])
    
                node_later_ask = ET.SubElement(node_later,"ask")
                node_later_ask.text = str(v['later']['ask'])
    
                node_later_impliedvolatility = ET.SubElement(node_later,"impliedvolatility")
                node_later_impliedvolatility.text =str(v['later']['impliedvolatility'])
                
                ###################################################################### 
        
        tree = ET.ElementTree(root)
        
        #------------------------------------------------------
        import os
        directorylocaloutput = os.path.join(os.getcwd(), 'output','xml latest')
        import mytools
        mytools.general.make_sure_path_exists(directorylocaloutput)
        
        datetime14 = mytools.mystrings.ConvertDatetime14()
        print(datetime14)
        outputfilepath = directorylocaloutput + '\\latest calendarspreads ' + datetime14 + '.xml'
        #if showresults == 1:
        print('printing results to ' + outputfilepath)
        tree.write(outputfilepath)
        self.XMLFilenameOutput = outputfilepath
            
"""
        for k1,v1 in d5.items():
            v = v1['candidate']
            d_candidates[len(d_candidates)] = v
            #earlieroptionsymbol = v['earlier']['optionsymbol']
            #expirationdate = mytools.get_from_optionsymbol.expirationdate(earlieroptionsymbol).date()
            #vdate = mytools.mystrings.ConvertStringToDate('2015-02-14')
            
            #if expirationdate <= vdate:
            
            ##################################################################
            #showresults = 0
            if showresults == 1:
                print(
                     'k'
                     ,  str(k1+1)
             #        ,  v['keyid']
                     ,  v['specifications']['symbol']
                     , '='
                     ,  v['specifications']['stockprice']
                     ,  v['calculations']['sortbymeasurename']
                     ,  v['calculations']['sortbymeasurevalue']
                     ,  'VAR'
                     ,  v['calculations']['valueatriskopen']
                     , 'earlierbid='
                     ,  v['earlier']['bid']
                     , 'laterask='
                     ,  v['later']['ask']
                     ,  v['earlier']['optionsymbol']
                     ,  v['later']['optionsymbol']
            
                     ,  v['earlier']['bucketquotedatetime']
                    )
"""