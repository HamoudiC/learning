# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-In


#local scope
def func1():
    a = 1
    print(a)

def func2():
    b = 2
    print(b)

func1()
func2()

#Enclosed scope:
def func1():
    a = 1
    
    def func2():
        b = 2
        print(a)    #works bc func1 is the big func and func2 is inside func 1. 

func2()

#Global Scope:
def func1():
    x = 1 
    print(x)

def func2():
    print(x)

x = 3

func1()
func2()

#Built-In Scope:
from math import e

def func1():
    print(e)

e = 3

func1()     #will print 3 because variable e overrides the e module