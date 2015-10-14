class pull:
    def __init__(self, 
                     destinationdirectorylocal,
                     sourcefilelocalsymbols='inputs\\Symbols.txt',
                     sourcefilelocalexpirationdates='inputs\\Expirations.txt',
                     showresults=1):
        print("initialized pullpricesallfromdestinationdirectorylocalroot...")
        self.execute_results(destinationdirectorylocal,sourcefilelocalsymbols,sourcefilelocalexpirationdates,showresults)
        
#    def set_MainDictionariesObject(self,MainDictionariesObject):
#        self._MainDictionariesObject = MainDictionariesObject
#    def get_MainDictionariesObject(self):
#        return self._MainDictionariesObject
#    MainDictionariesObject = property(get_MainDictionariesObject, set_MainDictionariesObject)
    
    def set_DictionaryOfFilteredInstances(self,DictionaryOfFilteredInstances):
        self._DictionaryOfFilteredInstances = DictionaryOfFilteredInstances
    def get_DictionaryOfFilteredInstances(self):
        return self._DictionaryOfFilteredInstances
    DictionaryOfFilteredInstances = property(get_DictionaryOfFilteredInstances, set_DictionaryOfFilteredInstances)
    
    def set_DictionaryOfAllInstances(self,DictionaryOfAllInstances):
        self._DictionaryOfAllInstances = DictionaryOfAllInstances
    def get_DictionaryOfAllInstances(self):
        return self._DictionaryOfAllInstances
    DictionaryOfAllInstances = property(get_DictionaryOfAllInstances, set_DictionaryOfAllInstances)
    
    def execute_results(self,destinationdirectorylocal,sourcefilelocalsymbols,sourcefilelocalexpirationdates,showresults):
        import readintodictionarysinglecolumlistfromfilelocal
        import pullprices #_tc as pullprices
        #destinationdirectorylocal=destinationdirectorylocal #"C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\downloads\\20141205\\16"
        #destinationdirectorylocal='C:\\Batches\\AutomationProjects\\My Python\\downloads\\20141204end1'
        symbols=readintodictionarysinglecolumlistfromfilelocal.Dictionary(sourcefilelocalsymbols)
        #symbols=readintodictionarysinglecolumlistfromfilelocal.Dictionary('C:\\Batches\\AutomationProjects\\My Python\\inputs\\Symbols.txt')
        print(str(len(symbols)) + " symbols found.")
        expirations=readintodictionarysinglecolumlistfromfilelocal.Dictionary(sourcefilelocalexpirationdates)
        print(str(len(expirations)) + " expirations found.")
        import datetime
        for SymbolKey,SymbolValue in symbols.items():            
            print('=== beginning pull...',SymbolValue,datetime.datetime.now())
            #expirations=readintodictionarysinglecolumlistfromfilelocal.Dictionary('C:\\Batches\AutomationProjects\\My Python\\inputs\\Expirations.txt')
            for ExpirationKey,ExpirationValue in expirations.items():
                opull = pullprices.options(SymbolValue,ExpirationValue,destinationdirectorylocal,0)        
                print('  === completed pull...', SymbolValue, ExpirationValue)
                

