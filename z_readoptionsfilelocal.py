import sys
import os

def Print(my_dict):
    for k1,v1 in my_dict.items():
        print(k1,v1)
        
class switch(object):
    value = None
    def __new__(class_, value):
        class_.value = value
        return True

def case(*args):
    return any((arg == switch.value for arg in args))


def modification_date(filename):
    import datetime
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)        


class get_from_pathname():

    def symbol(pathtofile):
        filenamestring = os.path.basename(pathtofile)
        filenamebase = os.path.splitext(os.path.basename(filenamestring))[0]
        return filenamebase.split(' ',4)[1]

    def expirationdate(pathtofile):
        filenamestring = os.path.basename(pathtofile)
        filenamebase = os.path.splitext(os.path.basename(filenamestring))[0]

        s1 = filenamebase.split(' ',4)[2]
        from datetime import datetime
        d = datetime.strptime(s1, '%Y-%m-%d')
        return d        
        
    def quotedatetime(pathtofile):
        #print('a-bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
        filenamestring = os.path.basename(pathtofile)
        filenamebase = os.path.splitext(os.path.basename(filenamestring))[0]
        longdate_from_filenamebase = filenamebase.split(' ',4)[3]
        from datetime import datetime
        d = datetime.strptime(longdate_from_filenamebase, '%Y%m%d%H%M%S')
        return d

    def bucketquotedatetime(pathtofile):
        #print('a-ccccccccccccccccccccccccccccccccccccccccc')
        filenamestring = os.path.basename(pathtofile)
        filenamebase = os.path.splitext(os.path.basename(filenamestring))[0]
        longdate_from_filenamebase = filenamebase.split(' ',4)[3]
        import datetime
        #print('a-dddddddddddddddddddddddddddddddddddddddddddd')
        d = datetime.datetime.strptime(longdate_from_filenamebase, '%Y%m%d%H%M%S')
        #print('a-eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
        m = d.minute
        #print('a-fffffffffffffffffffffffffffffffffffffffffffffff')        
        x = 0
        if m <= 15:
            x = 15
        if (m > 15) and (m <= 30):
            x = 30
        if (m > 30) and (m <= 45):
            x = 45
        if (m > 45):
            x = 60
        #return x
        #print('a-ggggggggggggggggggggggggggggggggggggggggggggggg')        
        d1 = datetime.date(d.year,d.month,d.day)    
        #print('a-hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')  
        #return x
        t1 = datetime.time(d.hour, x, 0)
            
        return datetime.datetime.combine(d1, t1)


###################################################################
#class get_from_pathname(object):
#    def __init__(self):
#        self._name = None
# 
#    def set_name(self, name):
#        self._name = name
#    def get_name(self):
#        return self._name
#        
#    def symbol(self,pathtofile):
#        return pathtofile.split(' ',4)[0]
#        
#    def quotedatetime(self,pathtofile):
#        print('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
#        filenamestring = os.path.basename(pathtofile)
#        filenamebase = os.path.splitext(os.path.basename(filenamestring))[0]
#        longdate_from_filenamebase = filenamebase.split(' ',4)[3]
#        from datetime import datetime
#        d = datetime.strptime(longdate_from_filenamebase, '%Y%m%d%H%M%S')
#        return d
#
#    def bucketquotedatetime(self,pathtofile):
#        import datetime
#        d = self.quotedatetime(self,pathtofile)
#        m = d.minute
#        x = 0
#        if m <= 15:
#            x = 15
#        if (m > 15) and (m <= 30):
#            x = 30
#        if (m > 30) and (m <= 45):
#            x = 45
#        if (m > 45):
#            x = 60
#    #    from datetime import timedelta
#    #    EndDate = Date + timedelta(mins=10)
#        #return x
#        d1 = datetime.date(d.year,d.month,d.day)    
#        #return x
#        t1 = datetime.time(d.hour, x, 0)
#            
#        return datetime.datetime.combine(d1, t1)
#######################################################################
class get_from_optionsymbol: 
    def expirationdate(optionsymbol):
        #print(optionsymbol)
        #print('a-bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
        s1 = optionsymbol[-15:-9]
        #s2 = s1[:-9]
        #print(s1)
        from datetime import datetime
        d1 = datetime.strptime(s1, '%y%m%d')
        return d1
    def strike(optionsymbol):
        s1 = optionsymbol[-8:]
        s2 = s1[:5] + '.' + s1[5:]
        #print('a-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        return float(s2)
    def optiontype(optionsymbol):
        optiontype_1 = optionsymbol[-9]
        return optiontype_1

class read:
    
    def __init__(self, pathtofile):
        self.populate_dictionaries(pathtofile)

    def set_PathToFile(self,PathToFile):
        self._PathToFile = PathToFile
    def get_PathToFile(self):
        return self._PathToFile
    PathToFile = property(get_PathToFile, set_PathToFile)

    def set_Symbol(self,Symbol):
        self._Symbol = Symbol
    def get_Symbol(self):
        return self._Symbol
    Symbol = property(get_Symbol, set_Symbol)

    def set_QuoteDatetime(self,QuoteDatetime):
        self._QuoteDatetime = QuoteDatetime
    def get_QuoteDatetime(self):
        return self._QuoteDatetime
    QuoteDatetime = property(get_QuoteDatetime, set_QuoteDatetime)

    def set_ExpirationDate(self,ExpirationDate):
        self._ExpirationDate = ExpirationDate
    def get_ExpirationDate(self):
        return self._ExpirationDate
    ExpirationDate = property(get_ExpirationDate, set_ExpirationDate)

        
    def set_BucketQuoteDatetime(self,BucketQuoteDatetime):
        self._BucketQuoteDatetime = BucketQuoteDatetime
    def get_BucketQuoteDatetime(self):
        return self._BucketQuoteDatetime
    BucketQuoteDatetime = property(get_BucketQuoteDatetime, set_BucketQuoteDatetime)
        
    def set_DictionaryOfPriceClassInstances(self,DictionaryOfPriceClassInstances):
        self._DictionaryOfPriceClassInstances = DictionaryOfPriceClassInstances
    def get_DictionaryOfPriceClassInstances(self):
        return self._DictionaryOfPriceClassInstances
    DictionaryOfPriceClassInstances = property(get_DictionaryOfPriceClassInstances, set_DictionaryOfPriceClassInstances)

    def set_DictionaryOfPutStrikes(self,DictionaryOfPutStrikes):
        self._DictionaryOfPutStrikes = DictionaryOfPutStrikes
    def get_DictionaryOfPutStrikes(self):
        return self._DictionaryOfPutStrikes
    DictionaryOfPutStrikes = property(get_DictionaryOfPutStrikes, set_DictionaryOfPutStrikes)
    
    def set_DictionaryOfCallStrikes(self,DictionaryOfCallStrikes):
        self._DictionaryOfCallStrikes = DictionaryOfCallStrikes
    def get_DictionaryOfCallStrikes(self):
        return self._DictionaryOfCallStrikes
    DictionaryOfCallStrikes = property(get_DictionaryOfCallStrikes, set_DictionaryOfCallStrikes)

    def set_DictionaryOfOptionSymbols(self,DictionaryOfOptionSymbols):
        self._DictionaryOfOptionSymbols = DictionaryOfOptionSymbols
    def get_DictionaryOfOptionSymbols(self):
        return self._DictionaryOfOptionSymbols
    DictionaryOfOptionSymbols = property(get_DictionaryOfOptionSymbols, set_DictionaryOfOptionSymbols)


    def populate_dictionaries(self, pathtofile):
        
        import c_option
        try:
    #        AAPL141122P00117000 

    #        filenamestring = os.path.basename(pathtofile)
    #        filenamebase = os.path.splitext(os.path.basename(filenamestring))[0]
    #        longdate_from_filenamebase = filenamebase.split(' ',4)[3]
    #        from datetime import datetime
    #        quotedatetime = datetime.strptime(longdate_from_filenamebase, '%Y%m%d%H%M%S')
            #print('a-11111111111111111111111111111111111111111111111111111111111')
            quotedatetime = get_from_pathname.quotedatetime(pathtofile)
            #print('a-222222222222222222222222222222222222222222222222222222222222')
            bucketquotedatetime = get_from_pathname.bucketquotedatetime(pathtofile)
            #print('a-33333333333333333333333333333333333333333333333333333')            
            symbol = get_from_pathname.symbol(pathtofile)
            expirationdate = get_from_pathname.expirationdate(pathtofile)
            
            #print(quotedatetime)
            
            lines_dictonary={}        
            dData={}
            dDataSelect={}
            dDataClass={}
            dStrikes={}
            dOptionSymbols={}
            dDataCategories={}
            dCallStrikes={}
            dPutStrikes={}
            
            dDataCategories[len(dDataCategories)] = "Strike"
            dDataCategories[len(dDataCategories)] = "OptionSymbol"
            dDataCategories[len(dDataCategories)] = "Last"
            dDataCategories[len(dDataCategories)] = "Bid"
            dDataCategories[len(dDataCategories)] = "Ask"
            dDataCategories[len(dDataCategories)] = "Change"
            dDataCategories[len(dDataCategories)] = "PctChange"
            dDataCategories[len(dDataCategories)] = "Volume"
            dDataCategories[len(dDataCategories)] = "OpenInterest"
            dDataCategories[len(dDataCategories)] = "ImpliedVolatility"
    
            fileobject = open(pathtofile, 'r')
            iRows = 0
            for line in fileobject:            
    
                line = line.strip()
                lines_dictonary[iRows] = line
                    
                jCols = 0
    
                ls = line.split(',')
                #print(ls)
                for x in ls:
                    x = x.strip()                    
                    dData[iRows,jCols] = x
                    while switch(iRows):                    
                        if case(0):
                            dStrikes[jCols] = x.strip()
                        if case(1):
                            dOptionSymbols[jCols] = x.strip()
                            dDataSelect[dOptionSymbols[jCols],dDataCategories[0]] = dStrikes[jCols]
                        break
                    if iRows >= 1:
                        dDataSelect[dOptionSymbols[jCols],dDataCategories[iRows]] = x.strip()
                    jCols = jCols  + 1
                iRows = iRows + 1
            
            for k1,v1 in dOptionSymbols.items():
                c = c_option.Framework()       
                c.quotedatetime = quotedatetime
                c.bucketquotedatetime = bucketquotedatetime
                
                for k2,v2 in dDataCategories.items():
                    #JCols = j + 1
                    #print("OptionSymbol=" + v1 + " " + v2 + "=" + dDataSelect[v1,v2])
  ###########################
                    while switch(v2):
                        if case("Strike"):                    
                            c.strike = dDataSelect[v1,v2]   
                        if case("OptionSymbol"):                    
                            c.optionsymbol = dDataSelect[v1,v2]
                        if case("Last"):
                            c.last = dDataSelect[v1,v2]
                        if case("Bid"):
                            c.bid = dDataSelect[v1,v2]
                        if case("Ask"):
                            c.ask = dDataSelect[v1,v2]
                        if case("Change"):
                            c.change = dDataSelect[v1,v2]
                        if case("PctChange"):
                            c.pctchange = dDataSelect[v1,v2]
                        if case("Volume"):
                            c.volume = dDataSelect[v1,v2]
                        if case("OpenInterest"):
                            c.openinterest = dDataSelect[v1,v2]
                        if case("ImpliedVolatility"):
                            c.impliedvolatility = dDataSelect[v1,v2]
                        break

                c.expirationdate = get_from_optionsymbol.expirationdate(c.optionsymbol)
                c.optiontype = get_from_optionsymbol.optiontype(c.optionsymbol)
                #print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                
                if c.optiontype == 'C':
                    if not c.strike in dCallStrikes.values():
                        dCallStrikes[len(dCallStrikes)] = c.strike
                if c.optiontype == 'P':
                    if not c.strike in dPutStrikes.values():
                        dPutStrikes[len(dPutStrikes)] = c.strike
                dDataClass[c.optionsymbol] = c

###############################
            self.PathToFile = pathtofile
            self.Symbol = symbol
            self.ExpirationDate = expirationdate

            self.QuoteDatetime = quotedatetime            
            self.BucketQuoteDatetime = bucketquotedatetime
            
            self.DictionaryOfOptionSymbols = dOptionSymbols
            self.DictionaryOfCallStrikes = dCallStrikes
            self.DictionaryOfPutStrikes = dPutStrikes
            self.DictionaryOfPriceClassInstances = dDataClass

            
        except Exception as e:
            print("filevalues: There was a problem with this one.....................................X")
            print("filevalues: ",str(e))
            
        else:
            err1 = 0
            if err1 == 1:
                print("filevalues: Success")
        finally:
            final1 = 0
            if final1 == 2:
                print("Completed: " + pathtofile)

            #print(modification_date(pathtofile))
#            print(dDataClass['AAPL141122P00085000'].openinterest)
#            print(dDataClass['AAPL141122P00085000'].expirationdate)
#            print(dDataClass['AAPL141122P00085000'].optiontype)
    #        print(filenamestring)
    #        print(longdate_from_filenamebase)
            #print(quotedatetime)
            #print(bucketquotedatetime_from_quotedatetime(quotedatetime))

    #################################
  
if __name__=='__main__':
    #my_dict
    my_dict1=read.DictionaryOfPriceClassInstances(sys.argv[1])
    #print(my_dict1)

