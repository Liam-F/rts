# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 11:42:37 2015

@author: justin.malinchak
"""
import builddataframeofrefdateminusd2tod1stockpricechanges as bdf
mybdf = bdf.perform('SPY',100,0,5,0).DataFrameResult
print mybdf

