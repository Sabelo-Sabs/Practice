# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 12:58:39 2021

@author: sabelo sibabalwe
dICTIONARY TUTORIAL 1
KEY-VALUE PAIRS
UNORDERED
MUTABLE
"""

#CREATING A DICTIONARY
dict1 = {'name': "Sabelo", 'age': 21, 'email':"Sabs@gmail.com"}
dict2 = dict(name = "Sabelo", age = 21, email = "Sabs@gmail.com")

print(dict1)
print(dict2)
# =============================================================================
# #Clearing the dictionary
# dict1.clear()
# dict2.clear()
# 
# print(dict1)
# print(dict2)
# 
# =============================================================================



# =============================================================================
# #Iterating through the dictionary
# #Getting a key-value pair
# for key,value in dict1.items():
#     print(key,value)
#     
# for items in dict1.items():
#     print(items)
#     
# #Getting keys only
# for keys in dict1.keys():
#     print(keys)
#     
# #Getting values only
# for values in dict1.values():
#     print(values)
#     
# =============================================================================
    
#Modifying the name key from the dictionary.

dict1["name"] = "Sibabalwe"
print(dict1)

#Creating a new key-value pair
dict1["Goal"] = "data scientist"
print(dict1)


#Checking if key exists in the list
if "name" in dict1:
    print("yes")
else:
    print("no")


