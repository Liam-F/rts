# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 17:34:59 2015

@author: Justin.Malinchak
"""

class Pizza(object):
    def __init__(self):
        self.toppings = []
    def __call__(self, topping):
        # when using '@instance_of_pizza' before a function def
        # the function gets passed onto 'topping'
        self.toppings.append(topping())
    def __repr__(self):
        return str(self.toppings)

pizza = Pizza()

@pizza
def cheese():
    return 'cheese'
@pizza
def sauce():
    return 'sauce'
@pizza
def meat():
    return 'pepperoni'


print pizza
# ['cheese', 'sauce']

# Flask?  Not sure what this is doing
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
rule      = "/"
view_func = hello
# they go as arguments here in 'flask/app.py'
def add_url_rule(self, rule, endpoint=None, view_func=None, **options):
    pass

print add_url_rule(1,2)

#Another explanation
def decorator(func):
   return func

@decorator
def some_func():
    pass