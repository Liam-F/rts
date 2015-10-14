"""

readintomemorycreateoptioninstancesfromfilelocal.py

showresults = 1
"""


import sys
import os

#def Print(my_dict):
#    for k1,v1 in my_dict.items():
#        print(k1,v1)
#        
class switch(object):
    value = None
    def __new__(class_, value):
        class_.value = value
        return True

def case(*args):
    return any((arg == switch.value for arg in args))


def modification_date(filelocal):
    import datetime
    t = os.path.getmtime(filelocal)
    return datetime.datetime.fromtimestamp(t)        

class D(object):
        def __init__(self, f):
            self.f = f
        def __get__(self, *args):
             return self.f

class get_from_filelocal():
#    def __init__(self, f):
#        print('oooooooooooooooooooooooooooooooooooooooooooooo')
#        self.f = f
#    def __get__(self, *args):
#         return self.f
         
    def symbol(self,filelocal):
        
        filelocalstring = os.path.basename(filelocal)
        filelocalbase = os.path.splitext(os.path.basename(filelocalstring))[0]
        return filelocalbase.split(' ',4)[1]

    def expirationdate(self,filelocal):
        
        filelocalstring = os.path.basename(filelocal)
        filelocalbase = os.path.splitext(os.path.basename(filelocalstring))[0]

        s1 = filelocalbase.split(' ',4)[2]
        from datetime import datetime
        d = datetime.strptime(s1, '%Y-%m-%d')
        return d        
        
    def quotedatetime(self,filelocal):
       # print('kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
        filelocalstring = os.path.basename(filelocal)
        filelocalbase = os.path.splitext(os.path.basename(filelocalstring))[0]
        longdate_from_filelocalbase = filelocalbase.split(' ',4)[3]
        from datetime import datetime
        d = datetime.strptime(longdate_from_filelocalbase, '%Y%m%d%H%M%S')
        return d

    def bucketquotedatetime(self,filelocal):
       # print('a-ccccccccccccccccccccccccccccccccccccccccc')
        filelocalstring = os.path.basename(filelocal)
        filelocalbase = os.path.splitext(os.path.basename(filelocalstring))[0]
        longdate_from_filelocalbase = filelocalbase.split(' ',4)[3]
        #print(longdate_from_filelocalbase)
        import datetime
        ##print('a-dddddddddddddddddddddddddddddddddddddddddddd')
        d = datetime.datetime.strptime(longdate_from_filelocalbase, '%Y%m%d%H%M%S')
        #print(str(d))
        ##print('a-eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
        m = d.minute
        ##print('a-fffffffffffffffffffffffffffffffffffffffffffffff')        
        x = 0
        if m < 15:
            x = 0
        if (m >= 15) and (m < 30):
            x = 15
        if (m >= 30) and (m < 45):
            x = 30
        if (m >= 45):
            x = 45
        #return x
        ##print('a-ggggggggggggggggggggggggggggggggggggggggggggggg')        
        d1 = datetime.date(d.year,d.month,d.day)    
        ##print('a-hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')  
        #return x
        t1 = datetime.time(d.hour, x, 0)
            
        return datetime.datetime.combine(d1, t1)


###################################################################
#class get_from_filelocal(object):
#    def __init__(self):
#        self._name = None
# 
#    def set_name(self, name):
#        self._name = name
#    def get_name(self):
#        return self._name
#        
#    def symbol(self,filelocal):
#        return filelocal.split(' ',4)[0]
#        
#    def quotedatetime(self,filelocal):
#        print('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
#        filelocalstring = os.path.basename(filelocal)
#        filelocalbase = os.path.splitext(os.path.basename(filelocalstring))[0]
#        longdate_from_filelocalbase = filelocalbase.split(' ',4)[3]
#        from datetime import datetime
#        d = datetime.strptime(longdate_from_filelocalbase, '%Y%m%d%H%M%S')
#        return d
#
#    def bucketquotedatetime(self,filelocal):
#        import datetime
#        d = self.quotedatetime(self,filelocal)
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
class build_option_symbol:
    #optionsymbol = 'QQQ141122C00086500'
    def build(symbol,expirationdate,optiontype,strikeprice):
        return symbol + expirationdate.strftime('%y%m%d')         
        
class get_from_optionsymbol: 
    def expirationdate(self,optionsymbol):
        #print(optionsymbol)
        ##print('a-bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
        s1 = optionsymbol[-15:-9]
        #s2 = s1[:-9]
        #print(s1)
        from datetime import datetime
        d1 = datetime.strptime(s1, '%y%m%d')
        return d1
    def strike(self,optionsymbol):
        s1 = optionsymbol[-8:]
        s2 = s1[:5] + '.' + s1[5:]
        ##print('a-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        return float(s2)
    def optiontype(self,optionsymbol):
        optiontype_1 = optionsymbol[-9]
        return optiontype_1
    def symbol(self,optionsymbol):
        #s1 = len(optionsymbol)
        s2 = optionsymbol[:-15]
        return s2


class read:
    
    def __init__(self, filelocal,showresults=0):
        #showresults = 1
        if showresults == 1:
            print('initialized class readintomemorycreateoptioninstancesfromfilelocal')
        self.HasError = 0
        # Force showresults
        #showresults = 0
        self.populate_dictionaries(filelocal,showresults)

    def set_filelocal(self,filelocal):
        self._filelocal = filelocal
    def get_filelocal(self):
        return self._filelocal
    filelocal = property(get_filelocal, set_filelocal)

    def set_HasError(self,HasError):
        self._HasError = HasError
    def get_HasError(self):
        return self._HasError
    HasError = property(get_HasError, set_HasError)

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

    def set_DictionaryOfOptionInstances(self,DictionaryOfOptionInstances):
        self._DictionaryOfOptionInstances = DictionaryOfOptionInstances
    def get_DictionaryOfOptionInstances(self):
        return self._DictionaryOfOptionInstances
    DictionaryOfOptionInstances = property(get_DictionaryOfOptionInstances, set_DictionaryOfOptionInstances)

    def populate_dictionaries(self, filelocal,showresults):
        if showresults==1:
            print('111111 readintomemorycreateoptioninstancesfromfilelocal.populate_dictionaries 111111')
        import structureforoptioninstance
       
        try:
    #        AAPL141122P00117000 

    #        filelocalstring = os.path.basename(filelocal)
    #        filelocalbase = os.path.splitext(os.path.basename(filelocalstring))[0]
    #        longdate_from_filelocalbase = filelocalbase.split(' ',4)[3]
    #        from datetime import datetime
    #        quotedatetime = datetime.strptime(longdate_from_filelocalbase, '%Y%m%d%H%M%S')
           # print(filelocal)
            
            #print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
            #quotedatetime = get_from_filelocal.quotedatetime(filelocal)
            f0 = get_from_filelocal()
            if showresults==1:
                print('222222 readintomemorycreateoptioninstancesfromfilelocal.populate_dictionaries 222222')
            v_quotedatetime = f0.quotedatetime(filelocal)
            if showresults==1:
                print('33333 readintomemorycreateoptioninstancesfromfilelocal.populate_dictionaries 333333')
                print(filelocal)
            bucketquotedatetime = f0.bucketquotedatetime(filelocal)
            
            if showresults==1:
                
                print('44444 readintomemorycreateoptioninstancesfromfilelocal.populate_dictionaries 44444')

            symbol = f0.symbol(filelocal)
            expirationdate = f0.expirationdate(filelocal)
            

            lines_dictonary={}        
            dData={}
            dDataSelect={}
            dDataClass={}
            dStrikes={}
            dOptionSymbols={}
            dDataCategories={}
            dCallStrikes={}
            dPutStrikes={}
            dContents={}
            
            
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
            dDataCategories[len(dDataCategories)] = "StockPrice"
    
            fileobject = open(filelocal, 'r')
            #print('a-11111111111111111111111111111111111111111111111111111111111')

            iRows = 0

            for line in fileobject:            
                if showresults==1:
                    print('rowloop readintomemorycreateoptioninstancesfromfilelocal.populate_dictionaries 00000' + str(iRows))

                line = line.strip()
                line = line.replace('"','')
                lines_dictonary[iRows] = line
                    
                jCols = 0
    
                ls = line.split(',')
                #print(ls)
                
                #print(len(ls))
                
                for x in ls:
                    
                    x = x.strip()
                    
                    dData[iRows,jCols] = x
                    #print('a-' + x)
                    while switch(iRows):                    
                        if case(0):
                            dStrikes[jCols] = x.strip()
                        if case(1):
                            dOptionSymbols[jCols] = x.strip()
                            dDataSelect[dOptionSymbols[jCols],dDataCategories[0]] = dStrikes[jCols]
                        break
                    if iRows >= 1:
                        if iRows <= 10:
                           #print(str(iRows) + ' ' + x)
                            dDataSelect[dOptionSymbols[jCols],dDataCategories[iRows]] = x.strip()                    
                    jCols = jCols  + 1
                    
                iRows = iRows + 1
            #print(iRows)
            if showresults==1:
                print('Lines in optionfile='+str(iRows))
            if not iRows == 11:
                print(filelocal)
                raise ValueError('Lines in file not = 11')
            #print('a-4444444444444444444444444444444444444444444444444')    
            
            if showresults==1:
                print(str(len(dOptionSymbols)) + ' number of option symbols found')            
                
            import datetime
            
            for k1,v1 in dOptionSymbols.items():
                c = structureforoptioninstance.Framework()       
                c.quotedatetime = v_quotedatetime
                c.bucketquotedatetime = bucketquotedatetime
                if showresults == 1:
                    print('--', 'looping within class readintomemorycreateoptioninstancesfromfilelocal.py')
                for k2,v2 in dDataCategories.items():

                    #JCols = j + 1
                    #print("OptionSymbol=" + v1 + " " + v2 + "=" + dDataSelect[v1,v2])
                    ###########################
                    while switch(v2):
                        if showresults == 1:
                            #mytime = time.strftime("%H:%M:%S:%MS", time.localtime())
                            #print(time.strftime("%H:%M:%S:%MS", time.localtime()))
                            print(datetime.datetime.now().isoformat())
                        if case("Strike"):                    
                            c.strike = dDataSelect[v1,v2]   
                        if case("OptionSymbol"):                    
                            c.optionsymbol = dDataSelect[v1,v2]
                            if showresults==1:
                                ###########################
                                print('-- --',dDataSelect[v1,v2])            
                                ###########################
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
                        if case("StockPrice"):
                            c.stockprice = dDataSelect[v1,v2]
                            
                            
                        break

                #print('a-33333333333333333333333333333333333333333333333333333')            
                get0 = get_from_optionsymbol()
                c.expirationdate = get0.expirationdate(c.optionsymbol)
                c.optiontype = get0.optiontype(c.optionsymbol)
                c.symbol = get0.symbol(c.optionsymbol)
                #print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                #############################################
                c.inthemoney = 0
                if c.optionsymbol == 'C':
                    if c.stockprice > c.strike:
                        c.inthemoney = 1
                if c.optionsymbol == 'P':
                    if c.stockprice < c.strike:
                        c.inthemoney = 1
                #############################################
                if c.optiontype == 'C':
                    if not c.strike in dCallStrikes.values():
                        dCallStrikes[len(dCallStrikes)] = c.strike
                if c.optiontype == 'P':
                    if not c.strike in dPutStrikes.values():
                        dPutStrikes[len(dPutStrikes)] = c.strike
                #print('********************************************')
                #if all (c.strike in dContents for c.strike in (c.strike, c.optiontype)):
                #if set((c.strike, c.optiontype)) <= dContents.keys():
                #if not c.strike, c.optiontype in dContents.keys():
                if not all([key in dContents for key in [c.strike,c.optiontype]]):
                    dContents[c.strike,c.optiontype] = c
                    #print('********************************************')
                    #print(len(dContents))
                    #print('********************************************')
                    
                dDataClass[c.optionsymbol] = c

###############################
            self.filelocal = filelocal
            self.Symbol = symbol
            self.ExpirationDate = expirationdate
            
            self.QuoteDatetime = v_quotedatetime            
            self.BucketQuoteDatetime = bucketquotedatetime
            
            self.DictionaryOfOptionSymbols = dOptionSymbols
            self.DictionaryOfCallStrikes = dCallStrikes
            self.DictionaryOfPutStrikes = dPutStrikes
            self.DictionaryOfPriceClassInstances = dDataClass
            self.DictionaryOfOptionInstances = dContents
            
        except ValueError as e:
            self.HasError = 1
            print('errorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerrorerror..readintomemorycreateoptioninstancesfromfilelocal')
            print(str(e))
            print('The options file is not formatted properly' )
            print(filelocal)
            pass
        except Exception as e:
            self.HasError = 1
            print("filevalues: There was an error in this module.....................................readintomemorycreateoptioninstancesfromfilelocal")
            print("filevalues: ",str(e))
            print("error:")
            pass
        else:
            err1 = 0
            if err1 == 1:
                print("filevalues: Success")
        finally:
            final1 = 0
            if final1 == 2:
                print("Completed: " + filelocal)

            #print(modification_date(filelocal))
#            print(dDataClass['AAPL141122P00085000'].openinterest)
#            print(dDataClass['AAPL141122P00085000'].expirationdate)
#            print(dDataClass['AAPL141122P00085000'].optiontype)
    #        print(filelocalstring)
    #        print(longdate_from_filelocalbase)
            #print(quotedatetime)
            #print(bucketquotedatetime_from_quotedatetime(quotedatetime))

    #################################
  
#if __name__=='__main__':
#    #my_dict
#    my_dict1=read.DictionaryOfPriceClassInstances(sys.argv[1])
#    #print(my_dict1)

