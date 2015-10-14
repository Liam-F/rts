# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 22:07:12 2014

@author: jmalinchak
"""

#from pandas.io.data import DataReader
#from datetime import datetime
#msft = DataReader("MSFT",  "yahoo")
#print(msft.bid)

import pandas.io.data as pd 

df = pd.get_quote_yahoo('HPQ')
#print(df)

cols = ['PE', 'change_pct', 'last', 'short_ratio', 'time']
result = pd.DataFrame(df, columns=cols)
print(result.iloc[0]['last'])
#data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
#        'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions', 'Lions', 'Lions'],
#        'wins': [11, 8, 10, 15, 11, 6, 10, 4],
#        'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
#        
#football = pd.DataFrame(data, columns=['year', 'team', 'wins', 'losses'])
#print(football)
#
#from_csv = pd.read_csv('C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\inputs\\Options AAPL 2015-01-17 20141203221727.csv')
#from_csv.head()
#print(from_csv)
#
#cols = ['num', 'game', 'date', 'team', 'home_away', 'opponent',
#        'result', 'quarter', 'distance', 'receiver', 'score_before',
#        'score_after']
#        
#from_csv = pd.read_csv('C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\inputs\\Options AAPL 2015-01-17 20141203221727.csv', sep=',', header=None,
#                         names=cols)
#print(from_csv)