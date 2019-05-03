import random
import sys
import os

#Conditional Code
# if else elif
# and or not

age = 18
if age > 16 :
    print('You are old enough to drive')
else :
    print("You are NOT old enough to drive")

if age >= 21 :
    print("You are old enought to drive a tractor")
elif age >=16:
    print('You are old enough to drive a car')
else:
    print("You are not old enough to drive")

if ((age >=1) and (age<= 18)):
    print("You get a birthday")
elif (age == 21) or (age >= 65):
    print("You don't get a birthday")
else:
    print('You get a birthday party yay!')
