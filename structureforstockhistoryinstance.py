# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 13:35:59 2014

@author: justin.malinchak
"""


class Framework(object):
 
    def __init__(self):
        self._name = None

    def set_symbol(self,symbol):
        self._symbol = symbol
    def get_symbol(self):
        return self._symbol
    symbol = property(get_symbol, set_symbol)
 
    def set_open(self,open):
        self._open = open
    def get_open(self):
        return self._open
    open = property(get_open, set_open)
    
    def set_high(self,high):
        self._high = high
    def get_high(self):
        return self._high
    high = property(get_high, set_high)


    def set_low(self,low):
        self._low = low
    def get_low(self):
        return self._low
    low = property(get_low, set_low)

    def set_close(self,close):
        self._close = close
    def get_close(self):
        return self._close
    close = property(get_close, set_close)
        
    def set_adjclose(self,adjclose):
        self._adjclose = adjclose
    def get_adjclose(self):
        return self._adjclose
    adjclose = property(get_adjclose, set_adjclose)

    def set_volume(self,volume):
        self._volume = volume
    def get_volume(self):
        return self._volume
    volume = property(get_volume, set_volume)

    def set_backfilled(self,backfilled):
        self._backfilled = backfilled
    def get_backfilled(self):
        return self._backfilled
    backfilled = property(get_backfilled, set_backfilled)
