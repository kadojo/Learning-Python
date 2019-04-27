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
