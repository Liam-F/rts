# -*- coding: utf-8 -*-
"""
Created on Mon May 25 12:37:06 2015

@author: jmalinchak
"""
#
#print( 
#    (4*1*(1/32.0)) ** (1/3.0)
#    )
#    
#print( 
#    (4+1+(1/32.0)) / 3.0
#    )
#
#import numpy as np
#import matplotlib.pyplot as plt
#import pandas
##matplotlib inline
#
#data = pandas.Series(np.random.normal(size=40))
##print(data)
#full_std = np.std(data)
#expand_std = pandas.expanding_std(data, min_periods=1)
#
#fig, ax = plt.subplots()
#expand_std.plot(ax=ax, color='k', linewidth=1.5, label='Expanded Std. Dev.')
#ax.axhline(y=full_std, color='g', label='Full Value')
#ax.legend()

import pandas as pd

import numpy as np

ser = pd.Series(np.random.normal(size=1000))
print(ser)
ser.hist(cumulative=True, normed=1, bins=100)


plt.show()