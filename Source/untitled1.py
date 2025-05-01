# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 19:14:41 2021

@author: Anjan Payra
"""

class MyClass:
 
    # Hidden member of MyClass
    __hiddenVariable = 0
   
    # A member method that changes
    # __hiddenVariable
    def add(self, increment):
        self.__hiddenVariable += increment
        print (self.__hiddenVariable)
  
# Driver code
myObject = MyClass()    
myObject.add(2)
myObject.add(5)
 
# This line causes error
print (myObject.__hiddenVariable)


class MyClass:
 
    # Hidden member of MyClass
    __hiddenVariable = 10
 
# Driver code
myObject = MyClass()    
print(myObject._MyClass__hiddenVariable)


class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b
 
    def __repr__(self):
        return "Test a:%s b:%s" % (self.a, self.b)
 
    def __str__(self):
        return "From str method of Test: a is %s,b is %s" % (self.a, self.b)
 
# Driver Code       
t = Test(1, 2)
print(t) # This calls __str__()
print([t]) # This calls __repr__()


class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

obj = MyClass()
obj.method()

obj.classmethod()

MyClass.staticmethod()


class A:
    def __init__(self, bb):
        self.b = bb
  
class B:
    def __init__(self):
        self.a = A(self)
    def __del__(self):
        print("die")
  
def fun():
    b = B()
    del b
  
fun()

