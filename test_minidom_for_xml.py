# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 19:52:04 2014

@author: jmalinchak
"""

#!/usr/bin/python
import lxml.etree
import lxml.builder    

E = lxml.builder.ElementMaker()
ROOT = E.root
DOC = E.doc
FIELD1 = E.field1
FIELD2 = E.field2

the_doc = ROOT(
        DOC(
            FIELD1('some value1', name='blah'),
            FIELD2('some value2', name='asdfasd'),
            )   
        )   

fullxml = lxml.etree.tostring(the_doc, pretty_print=True)
import os
directorylocaloutput = os.path.join(os.getcwd(), 'output','xml')
import mytools
mytools.general.make_sure_path_exists(directorylocaloutput)

datetime14 = mytools.mystrings.ConvertDatetime14()
print(datetime14)
outputfilepath = directorylocaloutput + '\\calendarspreads ' + datetime14 + '.xml'
#if showresults == 1:
print('printing results to ' + outputfilepath)

with open(outputfilepath, 'w') as f:
    f.write(fullxml)

#with open(outputfilepath, 'w') as f:
#    for outputline in the_doc.values():
#        f.write(outputline+'\n')

#if showresults == 1:
print('Finished executing calendarspreadslive...')
#self.OutputFilePathString = outputfilepath