import random
import sys
import os

#Dictionary (or maps)
#can't join together like Lists

super_villans = {'Fiddler' : 'Isaac Bowin','Captain Cold' : 'Leonard Snart', 'Weather Wizard' : 'Mark Mardon', 'Mirror Master' : 'Sam Scudder', 'Pied Piper' : 'Thomas Peterson'}

print(super_villans['Captain Cold'])

del super_villans['Fiddler']

super_villans['Pied Piper'] = 'Hartley Rathaway'

print(len(super_villans))

print(super_villans.get("Pied Piper"))

print(super_villans.keys())
print(super_villans.values())
