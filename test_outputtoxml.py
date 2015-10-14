# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 08:33:14 2014

@author: jmalinchak
"""
import pickle

# write python dict to a file
mydict = {'a': 1, 'b': 2, 'c': 3}
output = open('myfile.pkl', 'wb')
pickle.dump(mydict, output)
output.close()
print(mydict)

# read python dict back from the file
pkl_file = open('myfile.pkl', 'rb')
mydict = pickle.load(pkl_file)
pkl_file.close()
print(mydict)

# update dict and write to the file again
mydict.update({'d': 4})
output = open('myfile.pkl', 'wb')
pickle.dump(mydict, output)
output.close()

# read python dict back from the file
pkl_file = open('myfile.pkl', 'rb')
mydict = pickle.load(pkl_file)
pkl_file.close()
print(mydict)