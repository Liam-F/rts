# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 11:35:00 2014

@author: jmalinchak
"""
class print:
    def __init__(self,
                     orderedpairdictionary,
                     directorylocaloutput = 'downloads',
                     showresults=0):
        self.execute_results(   orderedpairdictionary,
                                directorylocaloutput,
                                showresults)

    def set_OutputFilePathString(self,OutputFilePathString):
        self._OutputFilePathString = OutputFilePathString
    def get_OutputFilePathString(self):
        return self._OutputFilePathString
    OutputFilePathString = property(get_OutputFilePathString, set_OutputFilePathString)    
    
    def execute_results(self,
                        d_orderedpairdictionary,
                        d_directorylocaloutput,
                        d_showresults):
        
        import mytools
        dOrdered = d_orderedpairdictionary
        
        print('Within printorderedpairdictionary, here is the length of dOrdered...')
        print(len(dOrdered))
        
        outputlines = {}
        outputlines[len(outputlines)]='earlier.optionsymbol' + ',' + \
                'later.optionsymbol' + ',' + \
                'earlier.strike' + '/' + 'later.strike' + ',' + \
                'later.optiontype' + ',' + \
                'earlier.expirationdate-datetime.today()' + ',' + 'remainder' + ',' + \
                'later.expirationdate-earlier.expirationdate' + ',' + 'remainder' + ',' + \
                'earlier.strike - later.strike' + ',' + \
                'later.stockprice' + ',' + \
                'earlier.bid' + ',' + \
                'later.ask' + ',' + 'percent earlier.bid/later.ask' + ',' + \
                'later.ask-earlier.bid' + ',' + \
                'later.inthemoney'
        #if showresults == 1:
        #print('putting results into printable dictionary ' + str(len(dOrdered)) + ' lines')
        from datetime import datetime 
        for k1,v1 in dOrdered.items():

            #this is a ls an idea on how to get values from dictionary= dOrdered.get(k1)
            #ls = v1[1]
            earlier = v1[1][0]
            later = v1[1][1]
            outputlines[len(outputlines)]=earlier.optionsymbol + ',' + \
                later.optionsymbol + ',' + \
                "'" + str(earlier.strike) + '/' + str(later.strike) + ',' + \
                later.optiontype + ',' + \
                str(earlier.expirationdate-datetime.today()) + ',' + \
                str(later.expirationdate-earlier.expirationdate) + ',' + \
                str(float(earlier.strike) - float(later.strike)) + ',' + \
                str(later.stockprice) + ',' + \
                str(earlier.bid) + ',' + \
                str(later.ask) + ',' + '{percent:.0%}'.format(percent=float(earlier.bid)/float(later.ask)) + ',' + \
                str(float(later.ask)-float(earlier.bid)) + ',' + \
                str(later.inthemoney)
            
        mytools.general.make_sure_path_exists(directorylocaloutput)
        
        datetime14 = mytools.mystrings.ConvertDatetime14()
        print(datetime14)
        outputfilepath = directorylocaloutput + '\\calendarspreads ' + datetime14 + '.csv'
        #if showresults == 1:
        print('printing results to ' + outputfilepath)
            
        with open(outputfilepath, 'w') as f:
            for outputline in outputlines.values():
                f.write(outputline+'\n')

        #if showresults == 1:
        print('Finished executing calendarspreadslive...')
        self.OutputFilePathString = outputfilepath
 