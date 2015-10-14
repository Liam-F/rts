# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 09:05:45 2014

@author: jmalinchak
"""
    def set_PairsCalculated(self,PairsCalculated):
        self._PairsCalculated = PairsCalculated
    def get_PairsCalculated(self):
        return self._PairsCalculated
    PairsCalculated = property(get_PairsCalculated, set_PairsCalculated)
    
            dPairsCalculated = {}
            print('building valid pairs... for ' + symbol)
            #########################################################################################################
            for k,ls in dPairs.items():
                earlier = ls[0]
                later = ls[1]
                #print(earlier.optionsymbol)
                #print(later.optionsymbol)
                if earlier.bid.replace('.','',1).isdigit(): #and float(earlier.bid) >= 0.25:
                    #if float(earlier.bid) <= 4.0:
                        if (earlier.optiontype == 'C' and float(earlier.stockprice) < float(earlier.strike)) or (earlier.optiontype == 'P' and float(earlier.stockprice) > float(earlier.strike)): 
                            
                            #------------------------------------------
                            # Set your Percentage cutoff here
                            ########################################## 
                            if later.ask.replace('.','',1).isdigit() and \
                                float(later.ask) > 0.0 and float(earlier.bid)/float(later.ask) > 0.8:
                            ##########################################                                
                                dPairsCalculated[k] = float(earlier.bid)/float(later.ask)
                                if showresults == 1:
                                    print(str(len(dPairsCalculated)) + ' valid pairs...')
            #########################################################################################################
            self.PairsCalculated = dPairsCalculated
            