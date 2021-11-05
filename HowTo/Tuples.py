import random
import sys
import os

#Tuples
#Can't edit the contents
pi_tuple = (3,1,4,1,5,9)

#list can be edited
new_tuple = list(pi_tuple)
new_list = tuple(new_tuple)

print(new_tuple)
print(new_list)
print(len(new_tuple))
print(min(new_tuple))
print(max(new_tuple))

print(new_tuple[2])


def doubleStuff(aList):
    """ Overwrite each element in aList with double its value. """
    for position in range(len(aList)):
        aList[position] = 2 * aList[position]

things = [2, 5, 9]
print(things)
doubleStuff(things)
print(things)