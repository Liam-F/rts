# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 20:12:27 2014

@author: jmalinchak
"""

class serialize:
    def __init__(self,
                 sortedpairdictionary,
                 showresults=0):
        print('initialized class serializesortedpairdictionarytoxml_tc.py ')
        self.execute_serialize(sortedpairdictionary,showresults)

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

    
    def execute_serialize(self,sortedpairdictionary,showresults):
        print('------')
        import xml.etree.cElementTree as ET
        
        root = ET.Element("root")
        
        doc = ET.SubElement(root, "doc")
        for k,v in sortedpairdictionary.items():
            
            earlier = v['earlier']
            later = v['later']
            node_keyid = ET.SubElement(doc,"keyid")
            node_keyid.set("value", str(k))
            #node_keyid.text = str(k)

            node_specifications = ET.SubElement(node_keyid,"specifications")
            node_specifications_symbol = ET.SubElement(node_specifications,"symbol")
            node_specifications_symbol.text = str(earlier.symbol)
            node_specifications_stockprice = ET.SubElement(node_specifications,"stockprice")
            node_specifications_stockprice.text = str(earlier.stockprice)
            node_specifications_bucketquotedatetime = ET.SubElement(node_specifications,"bucketquotedatetime")
            node_specifications_bucketquotedatetime.text = str(earlier.bucketquotedatetime)

            node_calculations = ET.SubElement(node_keyid,"calculations")
            #sortbymeasurevalue = round(v3['sortbymeasurevalue'],3)
            node_calculations_sortbymeasurevalue = ET.SubElement(node_calculations,"sortbymeasurevalue")
            node_calculations_sortbymeasurevalue.text = str(round(v["sortbymeasurevalue"],3))

            node_calculations_spreadpercentageopen = ET.SubElement(node_calculations,"spreadpercentageopen")
            node_calculations_spreadpercentageopen.text = str(round(float(earlier.bid)/float(later.ask),3))

            node_calculations_valueatriskopen = ET.SubElement(node_calculations,"valueatriskopen")
            node_calculations_valueatriskopen.text = str(round(-float(earlier.bid)+float(later.ask),3))
            
            ######################################################################
            node_earlier = ET.SubElement(node_keyid ,"earlier")

            node_optionsymbol = ET.SubElement(node_earlier,"optionsymbol")
            #node_optionsymbol.set("name", 'optionsymbol')
            node_optionsymbol.text = earlier.optionsymbol
 
            node_bid = ET.SubElement(node_earlier,"bid")
            node_bid.text = earlier.bid             

            node_ask = ET.SubElement(node_earlier,"ask")
            node_ask.text = earlier.ask             
            
            ######################################################################
            node_later = ET.SubElement(node_keyid ,"later")
            
            node_optionsymbol = ET.SubElement(node_later,"optionsymbol")
            #node_optionsymbol.set("name", 'optionsymbol')
            node_optionsymbol.text = later.optionsymbol
 
            node_bid = ET.SubElement(node_later,"bid")
            node_bid.text = later.bid             

            node_ask = ET.SubElement(node_later,"ask")
            node_ask.text = later.ask     
            
#           ###################################################################### 
#        keyid = ET.SubElement(doc, "keyid")
#        keyid.set("name", "blah")
#        keyid.text = "some value1"
#        
#        field2 = ET.SubElement(doc, "field2")
#        field2.set("name", "asdfasd")
#        field2.text = "some vlaue2"
#        
        tree = ET.ElementTree(root)
        
        #------------------------------------------------------
        import os
        directorylocaloutput = os.path.join(os.getcwd(), 'output','xml')
        import mytools
        mytools.general.make_sure_path_exists(directorylocaloutput)
        
        datetime14 = mytools.mystrings.ConvertDatetime14()
        print(datetime14)
        outputfilepath = directorylocaloutput + '\\calendarspreads ' + datetime14 + '.xml'
        #if showresults == 1:
        print('printing results to ' + outputfilepath)
        tree.write(outputfilepath)
        self.XMLFilenameOutput = outputfilepath