import random # Module for random number generators
import sys # Module that provides access to variables used and maintained by the interpreter
import os # Module for a portable way of using operating system dependent functionality

# Printing strings
s_one = "The shield that guards the realms of men."
s_two = "Don't let them construct the bridge!"
s_three = "Name:\tSir Bronn of the fuckin' Blackwater!\nReward:\tA fuckin' castle!"

# Converting strings to numbers
x_one = '2077'
print(int(x_one))
# Use int() to convert to number // Will also convert binary / hexidecimal strings to numbers
# Binary - int("1001", 2) // Hexidecimal - int("AFF0", 16)
# Use float() to convert to floating-point number

# Length of string
print(len(s_one))

# Find position of one string inside another (starting position)
print(s_one.find('shield'))

# Extracting part of a string (starting postion : end position)
print(s_one[27:32])

# Replace part of string
print(s_one.replace('shield', 'sword'))

# Repeating Instructions
for i in range(1,6): #Range - 5
    print(str(i) + ' aah aah aah')

# Repeating Instruction with conditions
answer = ''

while answer != 'x':
    answer = input('Enter command: ')

# Defining a function
def count_to_10():
    for i in range(1,11):
        print(i)

count_to_10()
