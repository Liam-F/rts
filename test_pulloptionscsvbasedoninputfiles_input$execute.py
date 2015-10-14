
############################
#
SymbolsFile = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\inputs\\Symbols$execute.txt'
ExpirationsFile = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\inputs\\Expirations$execute.txt'

import pulloptionscsvbasedoninputfiles

opulled = pulloptionscsvbasedoninputfiles.pull(SymbolsFile,
                                 ExpirationsFile,
                                 '$execute',
                                 0)
                                 
pulledcsvfilepath = opulled.OutputPathString
print(pulledcsvfilepath)

