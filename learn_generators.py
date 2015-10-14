# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 17:47:41 2015

@author: Justin.Malinchak
"""

from itertools import count

def generate_primes(stop_at=0):
    primes = []
    for n in count(2):
        if 0 < stop_at < n:
            return # raises the StopIteration exception
        composite = False
        for p in primes:
            if not n % p:
                composite = True
                break
            elif p ** 2 > n:
                break
        if not composite:
            primes.append(n)
            yield n

for i in generate_primes():  # iterate over ALL primes
    if i > 100:
        break
    print(i)