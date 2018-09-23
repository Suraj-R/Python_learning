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
#for person in people:
    #print(person)

#print (people[1][0])
    
for person in people:
    #print(person[0].split()[-1])
    person[2] *= 1.2
    
#print (people)
    
# lists maps ans generators

#pays = [person[2] for person in people] # example of list

#pays = map((lambda x:x[2]),people)      # example of map
#pays = list(pays) 
    
#pays = sum(person[2] for person in people) # example of generator expressions
    
#print(pays)
    
people.append(['Tom', 50, 0, None])
#print(people[-1])

# Field labels

Name, age, pay = range(3)
bob = ['Bob Smith', 42, 10000]
print(bob[Name],bob[pay])