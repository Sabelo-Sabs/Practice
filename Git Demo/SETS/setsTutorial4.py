# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 21:16:52 2021

@author: sabelo sibabalwe
Sets Tutorial 4
"""
even = {0,2,4,6,8}
odd = {1,3,5,7,9,11}
prime = {2,3,5,7,11,13}

# =============================================================================
# #Removes 0 from the even set; this method takes exactly one argument.
# even.discard(0)
# print(even)
# #Removes 5 from the odd set.
# odd.discard(5)
# print(odd)
# #Removes 5 from the odd set.
# prime.discard(13)
# print(prime)
# 
# =============================================================================

"""
Using the intersection method
"""
# =============================================================================
# #Gives you the numbers that exists in both sets.
# int1 = even.intersection(odd)
# print(int1)
# 
# #Gives you the numbers that exists in both sets.
# int2 = odd.intersection(prime)
# print(int2)
# 
# #Gives you the numbers that exists in both sets.
# int3 = even.intersection(prime)
# print(int3)
# =============================================================================

"""
Using the Intersection_update
"""
even.intersection_update(prime)
print(even)