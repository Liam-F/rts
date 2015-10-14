# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 09:48:41 2015

@author: justin.malinchak
"""
import mytools
openshortopenlongoptsym = 'SPY150717C00212500-SPY150717C00213500-SPY150717P00206000-SPY150717P00205000'
optionsymbol_list = openshortopenlongoptsym.split('-')
print optionsymbol_list
strikelegs_string = ''
for optionsymbol in optionsymbol_list:
    #print strikeleg
    strikeleg = mytools.get_from_optionsymbol().strike(optionsymbol)
    strikelegs_string = strikelegs_string + str(strikeleg) +'-'
if len(strikelegs_string ) > 0:
    strikelegs_string = strikelegs_string[:-1]
    
print strikelegs_string