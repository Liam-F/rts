# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 09:51:32 2015

@author: jmalinchak
"""

# ###########
# C/F using just a Map Example
def fahrenheit(T):
    return ((float(9)/5)*T + 32)
    
def celsius(T):
    return (float(5)/9)*(T-32)
celsius_list = (36.5, 37, 37.5,39)

fahrenheit_list = list(map(fahrenheit, celsius_list))
for val1 in fahrenheit_list:
    print('F',val1)
    
print('------- map ------')
new_celsius_list = list(map(celsius, fahrenheit_list))
for val2 in new_celsius_list:
    print('new_celsius_list items',val2)
print('-------')

Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)
Fahrenheit_list = list(Fahrenheit)
print('Fahrenheit_list',Fahrenheit_list)

C = map(lambda x: (float(5)/9)*(x-32), Fahrenheit_list)
Celsius_list = list(C)
print('Celsius_list',Celsius_list)

print('------- lambda/map ------')
a = [1,2,3,4]
b = [17,12,11,10]
c = [-1,-4,5,9]
print(list(map(lambda x,y:x+y, a,b)))
#[18, 14, 14, 14]
print(list(map(lambda x,y,z:x+y+z, a,b,c)))
#[17, 10, 19, 23]
list_01 = (list(map(lambda x,y,z:x+y-z, a,b,c)))
#[19, 18, 9, 5]
for each in list_01:
    print(each)
    
print('------- filter/lambda -------')

fib = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x: x % 2 > 0, fib)
print(list(result))
#[1, 1, 3, 5, 13, 21, 55]
result = filter(lambda x: x % 2 == 0, fib)
print(list(result))
#[0, 2, 8, 34]


print('-------- reduce ---------')
import functools
reduced_value = functools.reduce(lambda x,y: x/y+x, [47,11,42,13])
print(reduced_value)

print(47+11+42+13)

print('------- list comprehension -----')
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = [ ((float(9)/5)*x + 32) for x in Celsius ]
print(Fahrenheit)