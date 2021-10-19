# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 22:31:07 2021

@author: sabelo sibabalwe
"""

even = {0,2,4,6,8}
odd = {1,3,5,7,9,11}
prime = {2,3,5,7,11,13}

# =============================================================================
# #Returns true if the given sets have nothing in common.
# ans = even.isdisjoint(odd)
# print(ans)
# 
# ans1 = even.isdisjoint(prime)
# print(ans1)
# 
# ans2 = odd.isdisjoint(prime)
# print(ans2)
# 
# 
# =============================================================================

# =============================================================================
# #Returns true if a set is a subset of another set.
# sub = even.issubset(odd)
# print(sub)
# 
# #Returns true if a set is asuperset of another set
# sup = even.issuperset(odd)
# print(sup)
# #Returns union of the two sets.
# union1 = even.union(odd)
# print(union1)
# =============================================================================
#Updating the even set with the odd 
even.update(odd)
print(even)
