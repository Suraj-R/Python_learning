# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 21:55:00 2018

@author: Suraj-Desktop
"""

# ist way to make dictionaries
bob = {'name': 'Bob Smith', 'age':42, 'pay':30000, 'job':'dev'}
sue = {'name': 'Sue Jones', 'age':42, 'pay':40000, 'job':'hdw'}

#print(bob['name'],sue['pay'])

# second way to make dictionares

bob = dict(name = 'Bob Smith', age=42, pay=30000, job='dev')
sue = dict(name = 'Sue Jones', age=45, pay=40000, job='hwd')

#print (bob, sue)

#print(bob['name'], sue['pay'])

sue = {}
sue['name'] = 'Sue Jones'
sue['age'] = 45
sue['pay'] = 40000
sue['job'] = 'hdw'

#print(sue)

names = ['name', 'age', 'pay', 'job']
values = ['Sue Jones', 45, 40000, 'hdw']
sue = dict(zip(names,values))
#print(sue)

#empty dictionary initialization

fields = ('name', 'age', 'pay', 'job')
record = dict.fromkeys(fields, 0)
#print(record)

people = [bob, sue, record]
#print (people)

"""for person in people:
    if person['name'] == 'Sue Jones':
        print (person['pay'])"""
        
names = [person['name'] for person in people]

names = list(map(lambda x:x['name'],people))
print (names)