# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 20:12:27 2014

@author: jmalinchak
"""

class serialize:
    def __init__(self,
                 sourcedirectoryfull,
                 symbol,
                 dictionaryofcalendarspreadquads,
                 maxnumberofcandidates = 1000,
                 showresults=0):
        print('initialized class serializedictionaryofcalendarspreadquadstoxml.py ')
        self.Complete = 0
        self.execute_serialize(sourcedirectoryfull,
                                   symbol,
                                   dictionaryofcalendarspreadquads,
                                   maxnumberofcandidates,
                                   showresults)

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


    def set_Complete(self,Complete):
        self._Complete = Complete
    def get_Complete(self):
        return self._Complete
    Complete = property(get_Complete, set_Complete)   
    
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

    
    def execute_serialize(self,sourcedirectoryfull,symbol,dictionaryofcalendarspreadquads,maxnumberofcandidates,showresults):
        print('------')
        import mytools
        datetimestring = mytools.mystrings.datetimenormal()
        
        import xml.etree.cElementTree as ET
        
        root = ET.Element("rtstock")
        
        doc = ET.SubElement(root, "quadcalendarspreads")
        
        doc.set("latest", datetimestring)
        
        #totalnumberofcandidates = len(dictionaryofcalendarspreadquads)
        
        icandidate = 0
        for k,v in dictionaryofcalendarspreadquads.items():
            icandidate = icandidate + 1
            #v3['putcalendarspread']['later']['optionsymbol'])
            #if icandidate > totalnumberofcandidates - maxnumberofcandidates:
            if icandidate <= maxnumberofcandidates:
                #earlier = v['earlier']
                #later = v['later']
                node_keyid = ET.SubElement(doc,"keyid")
                node_keyid.set("value", str(icandidate))
                #node_keyid.text = str(k)
                
                #@node_putcalendarspread_specifications = ET.SubElement(node_keyid,"specifications")

                ######################################################################
                node_quadcalendarspread = ET.SubElement(node_keyid,"quadcalendarspread")
                
                node_quadcalendarspread_specifications = ET.SubElement(node_quadcalendarspread,"specifications")

                node_quadcalendarspread_specifications_symbol = ET.SubElement(node_quadcalendarspread_specifications,"symbol")
                node_quadcalendarspread_specifications_symbol.text = v['callcalendarspread']['specifications']['symbol']
                #,v['calculations']['sortbymeasurename'],v['calculations']['sortbymeasurevalue']
                
                node_quadcalendarspread_specifications_stockprice = ET.SubElement(node_quadcalendarspread_specifications,"stockprice")
                node_quadcalendarspread_specifications_stockprice.text = str(v['callcalendarspread']['specifications']['stockprice'])
                node_quadcalendarspread_specifications_bucketquotedatetime = ET.SubElement(node_quadcalendarspread_specifications,"bucketquotedatetime")
                node_quadcalendarspread_specifications_bucketquotedatetime.text = str(v['callcalendarspread']['specifications']['bucketquotedatetime'])
                
                node_quadcalendarspread_calculations = ET.SubElement(node_quadcalendarspread,"calculations")
                
                node_quadcalendarspread_calculations_sortbymeasurevalue = ET.SubElement(node_quadcalendarspread_calculations,'sortbymeasurevalue')
                node_quadcalendarspread_calculations_sortbymeasurevalue.text = str(v['sortbymeasurevalue'])

                node_quadcalendarspread_calculations_valueatriskopenquad = ET.SubElement(node_quadcalendarspread_calculations,"valueatriskopenquad")
                node_quadcalendarspread_calculations_valueatriskopenquad.text = str(float(v['callcalendarspread']['calculations']['valueatriskopen']) + float(v['putcalendarspread']['calculations']['valueatriskopen']))  
                
                ######################################################################
                node_callcalendarspread = ET.SubElement(node_keyid,"callcalendarspread")
                
                node_callcalendarspread_specifications = ET.SubElement(node_callcalendarspread,"specifications")

                node_callcalendarspread_specifications_symbol = ET.SubElement(node_callcalendarspread_specifications,"symbol")
                node_callcalendarspread_specifications_symbol.text = v['callcalendarspread']['specifications']['symbol']
                #,v['calculations']['sortbymeasurename'],v['calculations']['sortbymeasurevalue']
                
                node_callcalendarspread_specifications_stockprice = ET.SubElement(node_callcalendarspread_specifications,"stockprice")
                node_callcalendarspread_specifications_stockprice.text = str(v['callcalendarspread']['specifications']['stockprice'])
                node_callcalendarspread_specifications_bucketquotedatetime = ET.SubElement(node_callcalendarspread_specifications,"bucketquotedatetime")
                node_callcalendarspread_specifications_bucketquotedatetime.text = str(v['callcalendarspread']['specifications']['bucketquotedatetime'])
                
                node_callcalendarspread_calculations = ET.SubElement(node_callcalendarspread,"calculations")
                
                node_callcalendarspread_calculations_sortbymeasurevalue = ET.SubElement(node_callcalendarspread_calculations,'sortbymeasurevalue')
                node_callcalendarspread_calculations_sortbymeasurevalue.text = v['callcalendarspread']['calculations']['sortbymeasurevalue']
    
                node_callcalendarspread_calculations_sortbymeasurename = ET.SubElement(node_callcalendarspread_calculations,"sortbymeasurename")
                node_callcalendarspread_calculations_sortbymeasurename.text = v['callcalendarspread']['calculations']['sortbymeasurename']
    
    
    
                node_callcalendarspread_calculations_spreadpercentageopen = ET.SubElement(node_callcalendarspread_calculations,"spreadpercentageopen")
                node_callcalendarspread_calculations_spreadpercentageopen.text = v['callcalendarspread']['calculations']['spreadpercentageopen'] # str(round(float(earlier.bid)/float(later.ask),3))
    
                node_callcalendarspread_calculations_valueatriskopen = ET.SubElement(node_callcalendarspread_calculations,"valueatriskopen")
                node_callcalendarspread_calculations_valueatriskopen.text = v['callcalendarspread']['calculations']['valueatriskopen']

                node_callcalendarspread_calculations_valueatriskclose = ET.SubElement(node_callcalendarspread_calculations,"valueatriskclose")
                node_callcalendarspread_calculations_valueatriskclose.text = str(-999)
                
                node_callcalendarspread_earlier = ET.SubElement(node_callcalendarspread,"earlier")
    
                node_callcalendarspread_earlier_optionsymbol = ET.SubElement(node_callcalendarspread_earlier,"optionsymbol")
                node_callcalendarspread_earlier_optionsymbol.text = v['callcalendarspread']['earlier']['optionsymbol']
    
                node_callcalendarspread_earlier_bucketquotedatetime = ET.SubElement(node_callcalendarspread_earlier,"bucketquotedatetime")
                node_callcalendarspread_earlier_bucketquotedatetime.text = str(v['callcalendarspread']['earlier']['bucketquotedatetime'])
    
    
                node_callcalendarspread_earlier_quotedatetime = ET.SubElement(node_callcalendarspread_earlier,"quotedatetime")
                node_callcalendarspread_earlier_quotedatetime.text = str(v['callcalendarspread']['earlier']['quotedatetime'])
                
                
                node_callcalendarspread_earlier_bid = ET.SubElement(node_callcalendarspread_earlier,"bid")
                node_callcalendarspread_earlier_bid.text = str(v['callcalendarspread']['earlier']['bid'])
    
                node_callcalendarspread_earlier_ask = ET.SubElement(node_callcalendarspread_earlier,"ask")
                node_callcalendarspread_earlier_ask.text = str(v['callcalendarspread']['earlier']['ask'])
    
                node_callcalendarspread_earlier_impliedvolatility = ET.SubElement(node_callcalendarspread_earlier,"impliedvolatility")
                node_callcalendarspread_earlier_impliedvolatility.text =str(v['callcalendarspread']['earlier']['impliedvolatility'])
                
                node_callcalendarspread_later = ET.SubElement(node_callcalendarspread,"later")
    
                node_callcalendarspread_later_optionsymbol = ET.SubElement(node_callcalendarspread_later,"optionsymbol")
                node_callcalendarspread_later_optionsymbol.text = v['callcalendarspread']['later']['optionsymbol']
    
                node_callcalendarspread_later_bucketquotedatetime = ET.SubElement(node_callcalendarspread_later,"bucketquotedatetime")
                node_callcalendarspread_later_bucketquotedatetime.text = str(v['callcalendarspread']['later']['bucketquotedatetime'])
    
    
                node_callcalendarspread_later_quotedatetime = ET.SubElement(node_callcalendarspread_later,"quotedatetime")
                node_callcalendarspread_later_quotedatetime.text = str(v['callcalendarspread']['later']['quotedatetime'])
                
                
                node_callcalendarspread_later_bid = ET.SubElement(node_callcalendarspread_later,"bid")
                node_callcalendarspread_later_bid.text = str(v['callcalendarspread']['later']['bid'])
    
                node_callcalendarspread_later_ask = ET.SubElement(node_callcalendarspread_later,"ask")
                node_callcalendarspread_later_ask.text = str(v['callcalendarspread']['later']['ask'])
    
                node_callcalendarspread_later_impliedvolatility = ET.SubElement(node_callcalendarspread_later,"impliedvolatility")
                node_callcalendarspread_later_impliedvolatility.text =str(v['callcalendarspread']['later']['impliedvolatility'])
                
                ###################################################################### 
                ######################################################################
                node_putcalendarspread = ET.SubElement(node_keyid,"putcalendarspread")

                node_putcalendarspread_specifications = ET.SubElement(node_putcalendarspread,"specifications")

                node_putcalendarspread_specifications_symbol = ET.SubElement(node_putcalendarspread_specifications,"symbol")
                node_putcalendarspread_specifications_symbol.text = v['putcalendarspread']['specifications']['symbol']
                #,v['calculations']['sortbymeasurename'],v['calculations']['sortbymeasurevalue']
                
                node_putcalendarspread_specifications_stockprice = ET.SubElement(node_putcalendarspread_specifications,"stockprice")
                node_putcalendarspread_specifications_stockprice.text = str(v['putcalendarspread']['specifications']['stockprice'])
                node_putcalendarspread_specifications_bucketquotedatetime = ET.SubElement(node_putcalendarspread_specifications,"bucketquotedatetime")
                node_putcalendarspread_specifications_bucketquotedatetime.text = str(v['putcalendarspread']['specifications']['bucketquotedatetime'])
                
                node_putcalendarspread_calculations = ET.SubElement(node_putcalendarspread,"calculations")
                
                node_putcalendarspread_calculations_sortbymeasurevalue = ET.SubElement(node_putcalendarspread_calculations,'sortbymeasurevalue')
                node_putcalendarspread_calculations_sortbymeasurevalue.text = v['putcalendarspread']['calculations']['sortbymeasurevalue']
    
                node_putcalendarspread_calculations_sortbymeasurename = ET.SubElement(node_putcalendarspread_calculations,"sortbymeasurename")
                node_putcalendarspread_calculations_sortbymeasurename.text = v['putcalendarspread']['calculations']['sortbymeasurename']
    
    
    
                node_putcalendarspread_calculations_spreadpercentageopen = ET.SubElement(node_putcalendarspread_calculations,"spreadpercentageopen")
                node_putcalendarspread_calculations_spreadpercentageopen.text = v['putcalendarspread']['calculations']['spreadpercentageopen'] # str(round(float(earlier.bid)/float(later.ask),3))
    
                node_putcalendarspread_calculations_valueatriskopen = ET.SubElement(node_putcalendarspread_calculations,"valueatriskopen")
                node_putcalendarspread_calculations_valueatriskopen.text = v['putcalendarspread']['calculations']['valueatriskopen']

                node_putcalendarspread_calculations_valueatriskclose = ET.SubElement(node_putcalendarspread_calculations,"valueatriskclose")
                node_putcalendarspread_calculations_valueatriskclose.text = str(-999)

                node_putcalendarspread_earlier = ET.SubElement(node_putcalendarspread,"earlier")
    
                node_putcalendarspread_earlier_optionsymbol = ET.SubElement(node_putcalendarspread_earlier,"optionsymbol")
                node_putcalendarspread_earlier_optionsymbol.text = v['putcalendarspread']['earlier']['optionsymbol']
    
                node_putcalendarspread_earlier_bucketquotedatetime = ET.SubElement(node_putcalendarspread_earlier,"bucketquotedatetime")
                node_putcalendarspread_earlier_bucketquotedatetime.text = str(v['putcalendarspread']['earlier']['bucketquotedatetime'])
    
    
                node_putcalendarspread_earlier_quotedatetime = ET.SubElement(node_putcalendarspread_earlier,"quotedatetime")
                node_putcalendarspread_earlier_quotedatetime.text = str(v['putcalendarspread']['earlier']['quotedatetime'])
                
                
                node_putcalendarspread_earlier_bid = ET.SubElement(node_putcalendarspread_earlier,"bid")
                node_putcalendarspread_earlier_bid.text = str(v['putcalendarspread']['earlier']['bid'])
    
                node_putcalendarspread_earlier_ask = ET.SubElement(node_putcalendarspread_earlier,"ask")
                node_putcalendarspread_earlier_ask.text = str(v['putcalendarspread']['earlier']['ask'])
    
                node_putcalendarspread_earlier_impliedvolatility = ET.SubElement(node_putcalendarspread_earlier,"impliedvolatility")
                node_putcalendarspread_earlier_impliedvolatility.text =str(v['putcalendarspread']['earlier']['impliedvolatility'])
                
                node_putcalendarspread_later = ET.SubElement(node_putcalendarspread,"later")
    
                node_putcalendarspread_later_optionsymbol = ET.SubElement(node_putcalendarspread_later,"optionsymbol")
                node_putcalendarspread_later_optionsymbol.text = v['putcalendarspread']['later']['optionsymbol']
    
                node_putcalendarspread_later_bucketquotedatetime = ET.SubElement(node_putcalendarspread_later,"bucketquotedatetime")
                node_putcalendarspread_later_bucketquotedatetime.text = str(v['putcalendarspread']['later']['bucketquotedatetime'])
    
    
                node_putcalendarspread_later_quotedatetime = ET.SubElement(node_putcalendarspread_later,"quotedatetime")
                node_putcalendarspread_later_quotedatetime.text = str(v['putcalendarspread']['later']['quotedatetime'])
                
                
                node_putcalendarspread_later_bid = ET.SubElement(node_putcalendarspread_later,"bid")
                node_putcalendarspread_later_bid.text = str(v['putcalendarspread']['later']['bid'])
    
                node_putcalendarspread_later_ask = ET.SubElement(node_putcalendarspread_later,"ask")
                node_putcalendarspread_later_ask.text = str(v['putcalendarspread']['later']['ask'])
    
                node_putcalendarspread_later_impliedvolatility = ET.SubElement(node_putcalendarspread_later,"impliedvolatility")
                node_putcalendarspread_later_impliedvolatility.text =str(v['putcalendarspread']['later']['impliedvolatility'])
                
                ###################################################################### 
        
        tree = ET.ElementTree(root)
        
        #------------------------------------------------------
        import os
        directorylocaloutput = os.path.join(os.getcwd(), "output",'calendarspreadquads',symbol)
        import mytools
        mytools.general.make_sure_path_exists(directorylocaloutput)
        
        datetime14 = mytools.mystrings.ConvertDatetime14()
        print(datetime14)
        outputfilepath = directorylocaloutput + '\\calendarspreadquads '+ symbol + ' ' + datetime14 + '.xml'
        #if showresults == 1:
        print('printing results to ' + outputfilepath)
        tree.write(outputfilepath)
        self.XMLFilenameOutput = outputfilepath
        self.Complete = 1
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