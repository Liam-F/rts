# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 20:12:27 2014

@author: jmalinchak
"""

import xml.etree.cElementTree as ET

root = ET.Element("root")

doc = ET.SubElement(root, "doc")

field1 = ET.SubElement(doc, "field1")
field1.set("name", "blah")
field1.text = "some value1"

field2 = ET.SubElement(doc, "field2")
field2.set("name", "asdfasd")
field2.text = "some vlaue2"

tree = ET.ElementTree(root)
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