# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 20:12:27 2014

@author: jmalinchak
"""

# 
#  
#        NEEDS WORK
#    
#     
#      
#      

class serialize:
    def __init__(self,
                 sortedcandidatedictionary,
                 showresults=0):
        print('initialized class serializesortedcandidatedictionarytoxml.py ')
        self.execute_serialize(sortedcandidatedictionary,showresults)

#    def set_DictionaryOfQualifiedcandidatesInput(self,DictionaryOfQualifiedcandidatesInput):
#        self._DictionaryOfQualifiedcandidatesInput = DictionaryOfQualifiedcandidatesInput
#    def get_DictionaryOfQualifiedcandidatesInput(self):
#        return self._DictionaryOfQualifiedcandidatesInput
#    DictionaryOfQualifiedcandidatesInput = property(get_DictionaryOfQualifiedcandidatesInput, set_DictionaryOfQualifiedcandidatesInput)   
    
    def set_Complete(self,Complete):
        self._Complete = Complete
    def get_Complete(self):
        return self._Complete
    Complete = property(get_Complete, set_Complete)   

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

    
    def execute_serialize(self,sortedcandidatedictionary,showresults):
        import mytools
        startdate14 = mytools.mystrings.ConvertDatetime14()

        print('------')
        self.XMLFilenameOutput = ''
        self.Complete = 0
        if len(sortedcandidatedictionary.items()) > 0:
            import xml.etree.cElementTree as ET
    #        import mytools
            
            root = ET.Element("root")
            
            doc = ET.SubElement(root, "doc")
            
            
            for k1,v1 in sortedcandidatedictionary.items():
                
                v = v1['candidate']
                
                #earlieroptionsymbol = v['earlier']['optionsymbol']
                #expirationdate = mytools.get_from_optionsymbol.expirationdate(earlieroptionsymbol).date()
                #vdate = mytools.mystrings.ConvertStringToDate('2015-02-14')

                node_keyid = ET.SubElement(doc,"keyid")
                node_keyid.set("value", str(k1))
                
                node_specifications = ET.SubElement(node_keyid,"specifications")

                node_specifications_symbol = ET.SubElement(node_specifications,"symbol")
                node_specifications_symbol.text = v['specifications']['symbol']

                node_specifications_stockprice = ET.SubElement(node_specifications,"stockprice")
                node_specifications_stockprice.text = v['specifications']['stockprice']


                node_calculations = ET.SubElement(node_keyid,"calculations")
                
                node_calculations_sortbymeasurename= ET.SubElement(node_calculations,"sortbymeasurename")
                node_calculations_sortbymeasurename.text = v['calculations']['sortbymeasurename']

                
                node_calculations_spreadpercentageopen = ET.SubElement(node_calculations,"spreadpercentageopen")
                node_calculations_spreadpercentageopen.text = v['calculations']['spreadpercentageopen']

                node_calculations_valueatriskopen = ET.SubElement(node_calculations,"valueatriskopen")
                node_calculations_valueatriskopen.text = v['calculations']['valueatriskopen']

                node_earlier = ET.SubElement(node_keyid,"earlier")
                
                node_earlier_optionsymbol = ET.SubElement(node_earlier,"optionsymbol")
                node_earlier_optionsymbol.text = v['earlier']['optionsymbol']
                
                node_later = ET.SubElement(node_keyid,"later")
                
                node_later_optionsymbol = ET.SubElement(node_later,"optionsymbol")
                node_later_optionsymbol.text = v['later']['optionsymbol']

                
                #if expirationdate <= vdate:
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
                        
#            for k,v in sortedcandidatedictionary.items():
#                
##                earlier = v['earlier']
##                later = v['later']
#                
#                node_keyid = ET.SubElement(doc,"keyid")
#                node_keyid.set("value", str(k))
#                #node_keyid.text = str(k)
#    
#                ######################################################################
#                node_specifications = ET.SubElement(node_keyid,"specifications")
#                node_specifications_symbol = ET.SubElement(node_specifications,"symbol")
#                node_specifications_symbol.text = str(earlier.symbol)
#                node_specifications_stockprice = ET.SubElement(node_specifications,"stockprice")
#                node_specifications_stockprice.text = str(earlier.stockprice)
#                node_specifications_bucketquotedatetime = ET.SubElement(node_specifications,"bucketquotedatetime")
#                node_specifications_bucketquotedatetime.text = str(earlier.bucketquotedatetime)
#                bucketquotedatetimeforserializedfile = earlier.bucketquotedatetime
#                symbolforserializedfile = str(earlier.symbol)
#                ######################################################################
#                node_calculations = ET.SubElement(node_keyid,"calculations")
#                
#                node_calculations_sortbymeasurevalue = ET.SubElement(node_calculations,"sortbymeasurevalue")
#                node_calculations_sortbymeasurevalue.text = str(round(v["sortbymeasurevalue"],3))
#    
#                node_calculations_sortbymeasurename = ET.SubElement(node_calculations,"sortbymeasurename")
#                node_calculations_sortbymeasurename.text = v["sortbymeasurename"]
#    
#    
#    
#                node_calculations_spreadpercentageopen = ET.SubElement(node_calculations,"spreadpercentageopen")
#                node_calculations_spreadpercentageopen.text = str(round(float(earlier.bid)/float(later.ask),3))
#    
#                node_calculations_valueatriskopen = ET.SubElement(node_calculations,"valueatriskopen")
#                node_calculations_valueatriskopen.text = str(round(-float(earlier.bid)+float(later.ask),3))
#                
#                ######################################################################
#                node_earlier = ET.SubElement(node_keyid ,"earlier")
#    
#                node_earlier_optionsymbol = ET.SubElement(node_earlier,"optionsymbol")
#                node_earlier_optionsymbol.text = earlier.optionsymbol
#                
#    #            node_earlier_expirationdate = ET.SubElement(node_earlier,"expirationdate")
#    #            node_earlier_expirationdate.text = str(mytools.get_from_optionsymbol.expirationdate(earlier.optionsymbol))
#                
#                node_earlier_bucketquotedatetime = ET.SubElement(node_earlier,"bucketquotedatetime")
#                node_earlier_bucketquotedatetime.text = str(later.bucketquotedatetime)
#                
#                node_earlier_bid = ET.SubElement(node_earlier,"bid")
#                node_earlier_bid.text = earlier.bid             
#    
#                node_earlier_ask = ET.SubElement(node_earlier,"ask")
#                node_earlier_ask.text = earlier.ask             
#
#                node_earlier_openinterest = ET.SubElement(node_earlier,"openinterest")
#                node_earlier_openinterest.text = earlier.openinterest  
#                
#                ######################################################################
#                node_later = ET.SubElement(node_keyid ,"later")
#                
#                node_later_optionsymbol = ET.SubElement(node_later,"optionsymbol")
#                node_later_optionsymbol.text = later.optionsymbol
#    
#                node_later_bucketquotedatetime = ET.SubElement(node_later,"bucketquotedatetime")
#                node_later_bucketquotedatetime.text = str(later.bucketquotedatetime)
#     
#                node_later_bid = ET.SubElement(node_later,"bid")
#                node_later_bid.text = later.bid             
#    
#                node_later_ask = ET.SubElement(node_later,"ask")
#                node_later_ask.text = later.ask     
#
#                node_later_openinterest = ET.SubElement(node_later,"openinterest")
#                node_later_openinterest.text = later.openinterest    
                
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
            directorylocaloutput = os.path.join(os.getcwd(), 'output','calendarspreadcandidatesconsolidated')
            
            #import mytools
            #directorylocaloutput = mytools.mystrings.appendnormaldateddirectorybasedoncurrenttime15(directorylocaloutput)
            
            print('xml output directory:',directorylocaloutput)        
            
            mytools.general.make_sure_path_exists(directorylocaloutput)
            
            datetime14 = mytools.mystrings.ConvertDatetime14()
            print(datetime14)
            print('-----------')
            print('-- Candidate Path')
            bucketquotedatetimeforserializedfilename = str(bucketquotedatetimeforserializedfile)
            bucketquotedatetimeforserializedfilename = bucketquotedatetimeforserializedfilename.replace(':','-')
            if showresults == 1:
                print('bucketquotedatetimeforserializedfile',str(bucketquotedatetimeforserializedfilename))
            outputfilepath = directorylocaloutput + '\\calendarspreads ' + bucketquotedatetimeforserializedfilename + ' ' + symbolforserializedfile + '.xml'
            #if showresults == 1:
            try:
                os.remove(outputfilepath)
            except OSError:
                print('replacing existing file:',outputfilepath)
                pass
            print('--  ',outputfilepath)
            tree.write(outputfilepath)
            self.XMLFilenameOutput = outputfilepath
        self.Complete = 1    
            