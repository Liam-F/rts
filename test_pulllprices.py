import readintodictionarysinglecolumlistfromfilelocal
import pullprices
pathtoexportto="C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\downloads\\20141204\\1600test"
#pathtoexportto='C:\\Batches\\AutomationProjects\\My Python\\downloads\\20141204end1'
symbols=readintodictionarysinglecolumlistfromfilelocal.Dictionary('C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\inputs\\SymbolsShort.txt')
#symbols=readintodictionarysinglecolumlistfromfilelocal.Dictionary('C:\\Batches\\AutomationProjects\\My Python\\inputs\\Symbols.txt')

for SymbolKey,SymbolValue in symbols.items():
    print(pullprices.stock(SymbolValue))
    expirations=readintodictionarysinglecolumlistfromfilelocal.Dictionary('C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\inputs\\ExpirationsShort.txt')
    #expirations=readintodictionarysinglecolumlistfromfilelocal.Dictionary('C:\\Batches\AutomationProjects\\My Python\\inputs\\Expirations.txt')
    for ExpirationKey,ExpirationValue in expirations.items():
        pullprices.options(SymbolValue,ExpirationValue,pathtoexportto)        
        print('completed...', SymbolValue, ExpirationValue)

