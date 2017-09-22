# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 22:17:07 2017

@author: BALASUBRAMANIAM
"""

from copy import deepcopy

colours1 = ["red", "green"]
colours2 = colours1
colours2 = ["rouge", "vert"]
print (colours1)

colours2 = colours1
colours2[1] = "blue"
#issue in copy
print (colours1)

#shallow copy
list1 = ['a','b','c','d']
list2 = list1[:]
list2[1] = 'x'
print (list2)
print (list1)

#but with sub list
lst1 = ['a','b',['ab','ba']]
lst2 = lst1[:]
lst2[0] = 'c'
lst2[2][1] = 'd'
print(lst1)


#to overcome above issue go for deep copy

lst1 = ['a','b',['ab','ba']]

lst2 = deepcopy(lst1)

lst2[2][1] = "d"
lst2[0] = "c";

print (lst2)
print (lst1)

