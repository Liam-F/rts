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
                + self.impliedvolatility
                + self.stockprice)
 
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

    def set_optionsymbol(self,optionsymbol):
        self._optionsymbol = optionsymbol
    def get_optionsymbol(self):
        return self._optionsymbol
    optionsymbol = property(get_optionsymbol, set_optionsymbol)

    def set_expirationdate(self,expirationdate):
        self._expirationdate = expirationdate
    def get_expirationdate(self):
        return self._expirationdate
    expirationdate = property(get_expirationdate, set_expirationdate)
        
    def set_last(self,last):
        self._last = last
    def get_last(self):
        return self._last
    last = property(get_last, set_last)

    def set_bid(self,bid):
        self._bid = bid
    def get_bid(self):
        return self._bid
    bid = property(get_bid, set_bid)
    
    def set_ask(self,ask):
        self._ask = ask
    def get_ask(self):
        return self._ask
    ask = property(get_ask, set_ask)

    def set_change(self,change):
        self._change = change
    def get_change(self):
        return self._change
    change = property(get_change, set_change)

    def set_pctchange(self,pctchange):
        self._pctchange = pctchange
    def get_pctchange(self):
        return self._pctchange
    pctchange = property(get_pctchange, set_pctchange)

    def set_volume(self,volume):
        self._volume = volume
    def get_volume(self):
        return self._volume
    volume = property(get_volume, set_volume)

    def set_openinterest(self,openinterest):
        self._openinterest = openinterest
    def get_openinterest(self):
        return self._openinterest
    openinterest = property(get_openinterest, set_openinterest)    

    def set_impliedvolatility(self,impliedvolatility):
        self._impliedvolatility = impliedvolatility
    def get_impliedvolatility(self):
        return self._impliedvolatility
    impliedvolatility = property(get_impliedvolatility, set_impliedvolatility)
    
    #stockprice
    def set_stockprice(self,stockprice):
        self._stockprice = stockprice
    def get_stockprice(self):
        return self._stockprice
    stockprice = property(get_stockprice, set_stockprice)

    #inthemoney
    def set_inthemoney(self,inthemoney):
        self._inthemoney = inthemoney
    def get_inthemoney(self):
        return self._inthemoney
    inthemoney = property(get_inthemoney, set_inthemoney)
 
#    def inthemoney(self):        
#        print(self.optionsymbol,self._stockprice,self._strike)
#        r0 = None
#        if self.optionsymbol == 'C':
#            r0 = 0
#            if self._stockprice > self._strike:
#                r0 = 1
#        if self.optionsymbol == 'P':
#            r0 = 0
#            if self._stockprice < self._strike:
#                r0 = 1
#        return r0
                
    
#class Numbers:
#    def __init__(self, *arg):
#        self._numberList = []
#        for number in arg:
#            self._numberList.append(number)
#
#class Symbols:
#    def __init__(self, *arg):
#        self._symbolList = []
#        for symbol in arg:
#            self._symbolList.append(symbol)
#
#class Expirations:
#    def __init__(self, *arg):
#        self._expirationList = []
#        for expiration in arg:
#            self._expirationList.append(expiration)
#
#class OptionSymbols:
#    def __init__(self, *arg):
#        self._optionsymbolList = []
#        for optionsymbol in arg:
#            self._optionsymbolList.append(optionsymbol)


#symbols=Symbols('AAPL','FB')    # Instance 1
#print(symbols.symbolList)
