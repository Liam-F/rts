# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 19:14:22 2015

@author: jmalinchak
"""
def optiontype(optionsymbol):
    import mytools
    ot = mytools.get_from_optionsymbol().optiontype(optionsymbol)
    return ot

symbol = 'VIX'
expirationdate_string = '2015-07-24'
import pullprices as pp
df_optionpricescurrent = pp.options_to_dataframe(symbol,expirationdate_string,0)
df_optionpricescurrent['optiontype'] = df_optionpricescurrent['optionsymbol'].to_frame(name='optionsymbol').applymap(optiontype)
print(df_optionpricescurrent)



#print(df_optionpricescurrent[(df_optionpricescurrent.strike == '250.00')])
#print(df_optionpricescurrent[(df_optionpricescurrent.strike == '250.00') & (df_optionpricescurrent.optiontype =='P')].bid.iloc[0])
#print(df_optionpricescurrent[(df_optionpricescurrent.optionsymbol == 'SPY150724P00230000')].bid.iloc[0])
 #frame['e'].map(format)
#optionsymbolseries = df_optionpricescurrent['optionsymbol']
#df2 = optionsymbolseries.to_frame(name='optionsymbol')
#print(optiontype('SPY150717P00240000'))
#print(df2)
#print(df2.applymap(optiontype) )