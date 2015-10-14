
############################
#
SymbolsFile = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\inputs\\quad\\Symbols.txt'
ExpirationsFile = 'C:\\Documents and Settings\\jmalinchak\\My Documents\\My Python\\Active\\py\inputs\\quad\\Expirations.txt'

import pulloptionscsvbasedoninputfiles

opulled = pulloptionscsvbasedoninputfiles.pull(SymbolsFile,
                                 ExpirationsFile,
                                 'downloadsquad',
                                 0)
                                 
pulledcsvfilepath = opulled.OutputPathString
print(pulledcsvfilepath)

