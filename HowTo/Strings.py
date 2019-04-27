import random
import sys
import os

#Strings
quote = "\"Always remember you are unique"

muti_line_quote = ''' just
like everyone else'''

new_string = quote + muti_line_quote

print(new_string)

print("%s %s %s" % ('I like the quote',quote, muti_line_quote))

print("I don't like ", end="")
print("newlines")
print('\n' * 5)
print("but sometimes it is ok")


long_string = "i'll catch you if you fall - The Floor"
print(long_string)
print(long_string[0:6])
print(long_string[6])
print(long_string[-5])
print(long_string[-9:])
print(long_string[:-12])
print(long_string[:4] + ' be there')
print("%c is my %s letter and my number %d number is %.5f" %
('X', 'favourite', 1, 0.14))
print(long_string.capitalize())
print(long_string.find("Floor"))
print(long_string.isalpha()) #All Letters
print(long_string.isalnum()) #All Numbers
print(len(long_string))
print(long_string.replace("Floor","Ground"))

quote_list = long_string.split(" ")
print(quote_list)
