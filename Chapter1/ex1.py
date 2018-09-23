# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

bob = ['Bob Smith', 42, 30000, 'software']
sue = ['Sue Jones', 45, 40000, 'hardware']

a = [bob[0] , sue[2]]
a = bob[0].split()[-1]

#print (a)
sue[2] *= 1.25
#print(sue)

# a database list

people = [bob, sue]
for person in people:
    print(person)

