# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 00:05:31 2015

@author: jmalinchak
"""

SymbolsFile = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\inputs\\Symbols.txt'
ExpirationsFile = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\inputs\\Expirations.txt'
import pulloptionscsvbasedoninputfiles
pulloptionscsvbasedoninputfiles.pull(
                                 SymbolsFile,
                                 ExpirationsFile,
                                 'downloads',
                                 0
                                 )