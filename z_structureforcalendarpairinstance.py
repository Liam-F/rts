# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 13:35:59 2014

@author: justin.malinchak
"""


class Framework(object):
 
    def __init__(self):
        self._name = None
 
    def printdelim(self,delimiter):
        print(    self.symbol + delimiter 
                + str(self.quotedatetime) + delimiter 
                + str(self.bucketquotedatetime) + delimiter 
                + str(self.expirationdate) + delimiter 
                + self.strike + delimiter 
                + self.optiontype + delimiter 
                + self.bid + delimiter 
                + self.ask + delimiter 
                + self.impliedvolatility)
 
    def set_name(self, name):
        self._name = name
    def get_name(self):
        return self._name

        #dDataCategories['1'] = "StrikePrice"
        #dDataCategories['2'] = "OptionSymbol"
        #dDataCategories['3'] = "Last"
        #dDataCategories['4'] = "Bid"
        #dDataCategories['5'] = "Ask"
        #dDataCategories['6'] = "Change"
        #dDataCategories['7'] = "PctChange"
        #dDataCategories['8'] = "Volume"
        #dDataCategories['9'] = "OpenInterest"
        #dDataCategories['10'] = "ImpliedVolatility"

    def set_quotedatetime(self,quotedatetime):
        self._quotedatetime = quotedatetime
    def get_quotedatetime(self):
        return self._quotedatetime
    quotedatetime = property(get_quotedatetime, set_quotedatetime)

    def set_bucketquotedatetime(self,bucketquotedatetime):
        self._bucketquotedatetime = bucketquotedatetime
    def get_bucketquotedatetime(self):
        return self._bucketquotedatetime
    bucketquotedatetime = property(get_bucketquotedatetime, set_bucketquotedatetime)

    def set_optiontype(self,optiontype):
        self._optiontype = optiontype
    def get_optiontype(self):
        return self._optiontype
    optiontype = property(get_optiontype, set_optiontype)
    
    def set_strike(self,strike):
        self._strike = strike
    def get_strike(self):
        return self._strike
    strike = property(get_strike, set_strike)

    def set_symbol(self,symbol):
        self._symbol = symbol
    def get_symbol(self):
        return self._symbol
    symbol = property(get_symbol, set_symbol)


    def set_earlier_optionsymbol(self,optionsymbol):
        self._optionsymbol = optionsymbol
    def get_earlier_optionsymbol(self):
        return self._optionsymbol
    earlier_optionsymbol = property(get_earlier_optionsymbol, set_earlier_optionsymbol)

    def set_earlier_expirationdate(self,expirationdate):
        self._expirationdate = expirationdate
    def get_earlier_expirationdate(self):
        return self._expirationdate
    earlier_expirationdate = property(get_earlier_expirationdate, set_earlier_expirationdate)
        
    def set_earlier_last(self,last):
        self._last = last
    def get_earlier_last(self):
        return self._last
    earlier_last = property(get_earlier_last, set_earlier_last)

    def set_earlier_bid(self,bid):
        self._bid = bid
    def get_earlier_bid(self):
        return self._bid
    earlier_bid = property(get_earlier_bid, set_earlier_bid)
    
    def set_earlier_ask(self,ask):
        self._ask = ask
    def get_earlier_ask(self):
        return self._ask
    earlier_ask = property(get_earlier_ask, set_earlier_ask)

    def set_earlier_change(self,change):
        self._change = change
    def get_earlier_change(self):
        return self._change
    earlier_change = property(get_earlier_change, set_earlier_change)

    def set_earlier_pctchange(self,pctchange):
        self._pctchange = pctchange
    def get_earlier_pctchange(self):
        return self._pctchange
    earlier_pctchange = property(get_earlier_pctchange, set_earlier_pctchange)

    def set_earlier_volume(self,volume):
        self._volume = volume
    def get_earlier_volume(self):
        return self._volume
    earlier_volume = property(get_earlier_volume, set_earlier_volume)

    def set_earlier_openinterest(self,openinterest):
        self._openinterest = openinterest
    def get_earlier_openinterest(self):
        return self._openinterest
    earlier_openinterest = property(get_earlier_openinterest, set_earlier_openinterest)    

    def set_earlier_impliedvolatility(self,impliedvolatility):
        self._impliedvolatility = impliedvolatility
    def get_earlier_impliedvolatility(self):
        return self._impliedvolatility
    earlier_impliedvolatility = property(get_earlier_impliedvolatility, set_earlier_impliedvolatility)

##############################################################################

    def set_later_optionsymbol(self,optionsymbol):
        self._optionsymbol = optionsymbol
    def get_later_optionsymbol(self):
        return self._optionsymbol
    later_optionsymbol = property(get_later_optionsymbol, set_later_optionsymbol)

    def set_later_expirationdate(self,expirationdate):
        self._expirationdate = expirationdate
    def get_later_expirationdate(self):
        return self._expirationdate
    later_expirationdate = property(get_later_expirationdate, set_later_expirationdate)
        
    def set_later_last(self,last):
        self._last = last
    def get_later_last(self):
        return self._last
    later_last = property(get_later_last, set_later_last)

    def set_later_bid(self,bid):
        self._bid = bid
    def get_later_bid(self):
        return self._bid
    later_bid = property(get_later_bid, set_later_bid)
    
    def set_later_ask(self,ask):
        self._ask = ask
    def get_later_ask(self):
        return self._ask
    later_ask = property(get_later_ask, set_later_ask)

    def set_later_change(self,change):
        self._change = change
    def get_later_change(self):
        return self._change
    later_change = property(get_later_change, set_later_change)

    def set_later_pctchange(self,pctchange):
        self._pctchange = pctchange
    def get_later_pctchange(self):
        return self._pctchange
    later_pctchange = property(get_later_pctchange, set_later_pctchange)

    def set_later_volume(self,volume):
        self._volume = volume
    def get_later_volume(self):
        return self._volume
    later_volume = property(get_later_volume, set_later_volume)

    def set_later_openinterest(self,openinterest):
        self._openinterest = openinterest
    def get_later_openinterest(self):
        return self._openinterest
    later_openinterest = property(get_later_openinterest, set_later_openinterest)    

    def set_later_impliedvolatility(self,impliedvolatility):
        self._impliedvolatility = impliedvolatility
    def get_later_impliedvolatility(self):
        return self._impliedvolatility
    later_impliedvolatility = property(get_later_impliedvolatility, set_later_impliedvolatility)
