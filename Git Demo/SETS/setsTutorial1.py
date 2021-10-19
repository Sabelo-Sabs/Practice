# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 21:06:01 2021

@author: sabelo sibabalwe

sets: mutable, unordered, No duplicates

sets are mostly used when dealing with numbers.
"""
# Creating an even number set
even = {0,2,4,6,8,9,10}
# Making a copy
even1 = even.copy()

# Adding 12 to the even1 set
even1.add(12)

print("Original list: ",even)
print("Copy of the original changed: ",even1)
