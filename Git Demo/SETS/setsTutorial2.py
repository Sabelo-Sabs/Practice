# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 20:29:09 2021

@author: sabelo sibabalwe
Sets Tutorial 2
Difference Method.
"""
even = {0,2,4,6,8}
odd = {1,3,5,7,9,11}
prime = {2,3,5,7,11}

#Numbers that even have and odd does'nt

diff1 = even.difference(odd)
print(diff1)

#Numbers that odd have and even does'nt

diff2 = odd.difference(even)
print(diff2)

#Numbers that odd has and prime does'nt
diff3 = odd.difference(prime)
print(diff3)

#Numbers that prime has and odd does'nt
diff4 = prime.difference(odd)
print(diff4)