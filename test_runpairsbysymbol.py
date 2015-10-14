# -*- coding: utf-8 -*-
"""
Created on Sun Feb  8 09:55:15 2015

@author: jmalinchak
"""

file = open("inputs\\quad\\SymbolsTest.txt", "w")
file.write("ANF\n")
#file.write("NKE\n")
file.close()

file = open("inputs\\quad\\ExpirationsTest.txt", "w")
file.write("2015-03-13\n")
file.write("2015-03-20\n")
file.write("2015-03-27\n")
file.write("2015-04-02\n")
file.close()


############################

SymbolsFile = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\inputs\\quad\\SymbolsTest.txt'
ExpirationsFile = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\inputs\\quad\\ExpirationsTest.txt'
import pulloptionscsvbasedoninputfiles
opulled = pulloptionscsvbasedoninputfiles.pull(SymbolsFile,
                                 ExpirationsFile,
                                 '$execute',
                                 0)
                                 
pulledcsvfilepath = opulled.OutputPathString
print(pulledcsvfilepath)
#
#import os
#print(os.path.realpath(pulledcsvfilepath))    
#
#executepath = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\$execute'
#import mytools
#mytools.general.make_sure_path_exists(executepath)
#
#import shutil 
##shutil.move(pulledcsvfilepath, executepath)
#
#for dirName, subdirList, fileList in os.walk(pulledcsvfilepath):
#    if len(subdirList) == 0:
#        for file in fileList:
#            if file.split(' ')[1] == 'EWZ':
#                foundfiles = os.path.join(dirName, file)
#                shutil.move(foundfiles, executepath)

##############################
import serializecsvfilestoxmlcandidatepairs
o = serializecsvfilestoxmlcandidatepairs.read(downloadsdirectory = '$execute',
                                             replacelistforcreatingdestinationpath = ['\\$execute\\','\\$executeprocessed\\'],
                                             minpairspreadpercent = 0.1,
                                             maxvalueatrisk = 7.4,
                                             maxbidaskspreadpercentagesell = 0.25,
                                             maxbidaskspreadpercentagebuy = 0.25,
                                             showresults=1)
                                             
d1 = o.DictionaryOfSerializedFileObjects
print('-- --','Looping DictionaryOfSerializedFileObjects in runquadbysymbol')
for k1,v1 in d1.items():
    print('-- --','XMLFilenameOutput',v1.XMLFilenameOutput)
    import deserializecandidatesxml
    o1 = deserializecandidatesxml.deserialize(v1.XMLFilenameOutput)
    d1 = o1.DictionaryOfCandidatesFromXML

    minpairspreadpercent = 0.4
    dSortableDictionary = {}

    import mytools
    
    for k1,v1 in d1.items():
        optiontype1 = mytools.get_from_optionsymbol.optiontype(v1['earlier']['optionsymbol'])
        if optiontype1 == 'C':
            for k2,v2 in d1.items():
                if v1['specifications']['bucketquotedatetime'] == v2['specifications']['bucketquotedatetime']:
                    if v1['specifications']['symbol'] == v2['specifications']['symbol']:
                        optiontype2 = mytools.get_from_optionsymbol.optiontype(v2['earlier']['optionsymbol'])
                        if optiontype2 == 'P':
                            if float(v1['calculations']['spreadpercentageopen']) > minpairspreadpercent and float(v2['calculations']['spreadpercentageopen']) > minpairspreadpercent:
                                EarlierStrike1 = mytools.get_from_optionsymbol.strike(v1['earlier']['optionsymbol'])
                                LaterStrike1 = mytools.get_from_optionsymbol.strike(v1['later']['optionsymbol'])
                                EarlierStrike2 = mytools.get_from_optionsymbol.strike(v2['earlier']['optionsymbol'])
                                LaterStrike2 = mytools.get_from_optionsymbol.strike(v2['later']['optionsymbol'])
                                if float(EarlierStrike1) > float(v1['specifications']['stockprice']) and float(LaterStrike1) > float(v1['specifications']['stockprice']):
                                    if float(EarlierStrike2) < float(v1['specifications']['stockprice']) and float(LaterStrike2) < float(v1['specifications']['stockprice']):
                                        if k1 != k2:
                                            sumofvalueatrisk = float(v1['calculations']['valueatriskopen']) + float(v2['calculations']['valueatriskopen'])
                                            dSortableDictionary[len(dSortableDictionary)] = {'sortbymeasurevalue' : sumofvalueatrisk, 'callcalendarspread' : v1, 'putcalendarspread' : v2, 'sortbymeasurename' : 'valueatrisk'}
        
    from collections import OrderedDict
    dOrdered = OrderedDict(sorted(dSortableDictionary.items(), key=lambda t: t[1]['sortbymeasurevalue']))
    print('printing quads sortbymeasurevalue:')
    for k3,v3 in dOrdered.items():
        print('  --',  round(v3['sortbymeasurevalue'],2)
                    , '||'
                    ,  v3['callcalendarspread']['specifications']['stockprice']
                    , '||'
                    ,  v3['callcalendarspread']['earlier']['optionsymbol'],v3['callcalendarspread']['earlier']['bid'],v3['callcalendarspread']['later']['ask']
                    ,  v3['callcalendarspread']['later']['optionsymbol']
                    ,  '- -'
                    ,  v3['putcalendarspread']['earlier']['optionsymbol'],v3['putcalendarspread']['earlier']['bid'],v3['putcalendarspread']['later']['ask']
                    ,  v3['putcalendarspread']['later']['optionsymbol'])
