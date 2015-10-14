# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 17:44:13 2015

@author: Justin.Malinchak
"""

S = [2 * x for x in range(101) if x ** 2 > 3]
print S
print '-test -------'
R = [x*2 for x in range(101) if x % 3.0 == 0.0]
print R

print '-not primes --------'
noprimes = [j for i in range(2, 8) for j in range(i*2, 100, i)]
print noprimes

print '-primes --------'
primes = [x for x in range(0, 100) if x not in noprimes]
print primes

for i in range(2, 8):
    for j in range(i*2, 100, i):
        print j

#import pandas 
#chart.plot([l[0] for l in data], [l[1] for l in data])

