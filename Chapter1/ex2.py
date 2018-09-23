# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 21:35:25 2018

@author: Suraj-Desktop
"""

bob = [['name', 'Bob Smith'], ['age', 42], ['pay', 10000]]
sue = [['name', 'Sue Jones'], ['age', 45], ['pay', 20000]]
people = [bob,sue]

for person in people:
    person[2][1] *= 1.10 
    #print(person[0][1], person[2][1]) #name and pay
    
def field(record, label):
    for (fname, fvalue) in record:
        if fname == label:
            print(fvalue)
            
#field(bob, 'age')
            
for rec in people:
    field(rec, 'pay')