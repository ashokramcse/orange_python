# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 23:01:25 2017

@author: BALASUBRAMANIAM
"""

simple = dict(int_list=[1, 2, 3],
 
              text='string',
 
              number=3.44,
 
              boolean=True,
 
              none=None)
import json
 
print (json.dumps(simple, indent=4))

import datetime
d={}
d['date'] = datetime.datetime.now()
 
def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()
 
print(json.dumps(d, default = myconverter))



class User(object):
    def __init__(self, name, password):
        self.name = name
        self.password = password
anz = User('ANZ Technologies', 'secret')

def jdefault(o):
    return o.__dict__
print(json.dumps(anz, default=jdefault))


class Student:
 
    def __init__(self,name,email,contact,skills,ug=None,pg=None):
 
        self.email=email
        self.contact=contact
        self.name=name
        self.skills=[skills]
 
        self.edu={"ug":[ug],"pg":[pg]} 
        
james=Student("James","j@j.com","+1 7789990007","Python","CS", "CS")
print (vars(james))

print (json.dumps(vars(james),sort_keys=True, indent=4))
