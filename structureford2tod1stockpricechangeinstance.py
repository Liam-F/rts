# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 13:35:59 2014

@author: justin.malinchak
"""


class Framework(object):
 
    #@classmethod 
        
    def __init__(self,key):
        self._name = None

    def set_symbol(self,symbol):
        self._symbol = symbol
    def get_symbol(self):
        return self._symbol
    symbol = property(get_symbol, set_symbol)
 
    def set_dateref(self,dateref):
        self._dateref = dateref
    def get_dateref(self):
        return self._dateref
    dateref = property(get_dateref, set_dateref)
    
    def set_datemaxback(self,datemaxback):
        self._datemaxback = datemaxback
    def get_datemaxback(self):
        return self._datemaxback
    datemaxback = property(get_datemaxback, set_datemaxback)

    def set_datemidback(self,datemidback):
        self._datemidback = datemidback
    def get_datemidback(self):
        return self._datemidback
    datemidback = property(get_datemidback, set_datemidback)



    def set_priceref(self,priceref):
        self._priceref = priceref
    def get_priceref(self):
        return self._priceref
    priceref = property(get_priceref, set_priceref)
    
    def set_pricemaxback(self,pricemaxback):
        self._pricemaxback = pricemaxback
    def get_pricemaxback(self):
        return self._pricemaxback
    pricemaxback = property(get_pricemaxback, set_pricemaxback)

    def set_pricemidback(self,pricemidback):
        self._pricemidback = pricemidback
    def get_pricemidback(self):
        return self._pricemidback
    pricemidback = property(get_pricemidback, set_pricemidback)

    def set_pricedeltamaxdatebacktomiddateback(self,pricedeltamaxdatebacktomiddateback):
        self._pricedeltamaxdatebacktomiddateback = pricedeltamaxdatebacktomiddateback
    def get_pricedeltamaxdatebacktomiddateback(self):
        return self._pricedeltamaxdatebacktomiddateback
    pricedeltamaxdatebacktomiddateback = property(get_pricedeltamaxdatebacktomiddateback, set_pricedeltamaxdatebacktomiddateback)

    def set_pricedrawdownmax(self,pricedrawdownmax):
        self._pricedrawdownmax = pricedrawdownmax
    def get_pricedrawdownmax(self):
        return self._pricedrawdownmax
    pricedrawdownmax = property(get_pricedrawdownmax, set_pricedrawdownmax)
    
    def set_pricedrawupmax(self,pricedrawupmax):
        self._pricedrawupmax = pricedrawupmax
    def get_pricedrawupmax(self):
        return self._pricedrawupmax
    pricedrawupmax = property(get_pricedrawupmax, set_pricedrawupmax)

    
    def set_percentpricedrawdownmax(self,percentpricedrawdownmax):
        self._percentpricedrawdownmax = percentpricedrawdownmax
    def get_percentpricedrawdownmax(self):
        return self._percentpricedrawdownmax
    percentpricedrawdownmax = property(get_percentpricedrawdownmax, set_percentpricedrawdownmax)
    
    def set_percentpricedrawupmax(self,percentpricedrawupmax):
        self._percentpricedrawupmax = percentpricedrawupmax
    def get_percentpricedrawupmax(self):
        return self._percentpricedrawupmax
    percentpricedrawupmax = property(get_percentpricedrawupmax, set_percentpricedrawupmax)
    
    