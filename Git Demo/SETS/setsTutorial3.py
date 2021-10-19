# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 20:51:42 2021

@author: sabelo sibabalwe
Sets Tutorial 3
"""

even = {0,2,4,6,8}
odd = {1,3,5,7,9,11}
prime = {2,3,5,7,11,13}

#Removes items that exist in both sets
even.difference_update(odd)
print(even)

#Removes items that exist in both sets
odd.difference_update(prime)
print(odd)

#Removes items that exists in both set, but in this case we have to comment
#out the upper lines of code since we have already modified the odd set
prime.difference_update(odd)
print(prime)