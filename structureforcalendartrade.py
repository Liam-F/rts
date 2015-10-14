# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 13:35:59 2014

@author: justin.malinchak
"""


class Framework(object):
 
    def __init__(self,PairDictionary):
        self._name = None
        self.construct(PairDictionary)
        
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

    def set_openingpairspreadmarketprices(self,openingpairspreadmarketprices):
        self._openingpairspreadmarketprices = openingpairspreadmarketprices
    def get_openingpairspreadmarketprices(self):
        return self._openingpairspreadmarketprices
    openingpairspreadmarketprices = property(get_openingpairspreadmarketprices, set_openingpairspreadmarketprices)

    def set_openingpairspreadmidpointprices(self,openingpairspreadmidpointprices):
        self._openingpairspreadmidpointprices = openingpairspreadmidpointprices
    def get_openingpairspreadmidpointprices(self):
        return self._openingpairspreadmidpointprices
    openingpairspreadmidpointprices = property(get_openingpairspreadmidpointprices, set_openingpairspreadmidpointprices)


    def set_closingpairspreadmarketprices(self,closingpairspreadmarketprices):
        self._closingpairspreadmarketprices = closingpairspreadmarketprices
    def get_closingpairspreadmarketprices(self):
        return self._closingpairspreadmarketprices
    closingpairspreadmarketprices = property(get_closingpairspreadmarketprices, set_closingpairspreadmarketprices)

    def set_closingpairspreadmidpointprices(self,closingpairspreadmidpointprices):
        self._closingpairspreadmidpointprices = closingpairspreadmidpointprices
    def get_closingpairspreadmidpointprices(self):
        return self._closingpairspreadmidpointprices
    closingpairspreadmidpointprices = property(get_closingpairspreadmidpointprices, set_closingpairspreadmidpointprices)


    def set_quotedatetime(self,quotedatetime):
        self._quotedatetime = quotedatetime
    def get_quotedatetime(self):
        return self._quotedatetime
    quotedatetime = property(get_quotedatetime, set_quotedatetime)


    def construct(self,PairDictionary):
        pd = PairDictionary
        earlier = pd[0]
        later = pd[1]
        self.openingpairspreadmarketprices = round(float(earlier.bid) - float(later.ask),2)
        self.openingpairspreadmidpointprices = round(((float(earlier.bid) + float(earlier.ask)) / 2.0) - ((float(later.bid) + float(later.ask)) / 2.0),2)
        self.closingpairspreadmarketprices = round(float(later.bid) - float(earlier.ask),2)
        self.closingpairspreadmidpointprices = round(((float(later.bid) + float(later.ask)) / 2.0) - ((float(earlier.bid) + float(earlier.ask)) / 2.0),2)
 