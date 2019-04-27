import random
import sys
import os

#Lists
grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
print('First Item:', grocery_list[0])
grocery_list[0] = "Orange Juice"
print('First Item:', grocery_list[0])
print(grocery_list[1:3])

other_events = ['Wash Car', 'Pick Up Kids', 'Cash Cheque']

to_do_list = [other_events, grocery_list]
print(to_do_list)
print(to_do_list[1][1])
print(to_do_list[0][1])

grocery_list.append('Onions')
print(to_do_list)

grocery_list.insert(1,'Pickle')
print(grocery_list)
grocery_list.remove("Pickle")
print(grocery_list)
grocery_list.sort()
print(grocery_list)
grocery_list.reverse()
print(grocery_list)

del grocery_list[4]
print(to_do_list)

to_do_list2 = other_events + grocery_list
print(to_do_list2)

print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))
