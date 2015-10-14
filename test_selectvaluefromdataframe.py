# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 12:16:45 2015

@author: jmalinchak
"""

import pullprices as pp
df = pp.options_to_dataframe('SPY','2015-07-17',0)
df['optiontype'] = 'X'

import mytools


for index, row in df.iterrows():
    optionsymbol = row['optionsymbol']
    df['optiontype'][index] = mytools.get_from_optionsymbol().optiontype(optionsymbol)
    #print(optionsymbol)
    strike_at_sell_price = float(row['strike'])
    strike_at_sell_price_formatted = "%.2f" % strike_at_sell_price
    dummy_ask_at_sell_price = row['ask']
    
    optiontype = mytools.get_from_optionsymbol().optiontype(row['optionsymbol'])
    if optiontype == 'C':
        strike_at_buy_price = float(strike_at_sell_price) + float(1)
        
        #Decimal('3.214').quantize(TWOPLACES)        
    else:
        strike_at_buy_price = float(strike_at_sell_price) - float(1)

    df['optiontype'][index] = mytools.get_from_optionsymbol().optiontype(row['optionsymbol'])
    
    strike_at_buy_price_formatted = "%.2f" % strike_at_buy_price
    df_of_ask_of_buy_option = df[(df['strike']==str(strike_at_buy_price_formatted)) & (df['optiontype']==optiontype)]
    print(optiontype,row['strike'],strike_at_sell_price_formatted,strike_at_buy_price_formatted,len(df_of_ask_of_buy_option))
    
    
    #print(df_of_ask_of_buy_option)
    #ask_price_of_buy_option = float('Nan')
    #print(df_of_ask_of_buy_option)


    #if len(df_of_ask_of_buy_option) > 0:
    #    ask_price_of_buy_option = df_of_ask_of_buy_option.iloc[0])
    #    print(ask_price_of_buy_option)
    
print(df)
d2 = df[(df['strike']=='227.00') & (df['optiontype']=='P')]
#d2 = df[(df['strike']==l_ext) & (df['item']==item) & (df['wn']==wn) & (df['wd']==1)]
ask = d2['ask'].iloc[0]
#print(ask)