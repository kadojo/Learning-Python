import random
import sys
import os
#File I/O

#Create the file
test_file = open("test.txt", "wb")
print(test_file.mode)
print(test_file.name)
test_file.write(bytes("Write me to the file\nHello", 'UTF-8'))
test_file.close()

#Open and read the file
test_file = open("test.txt", "r+")
text_in_file = test_file.read()
print(text_in_file)

#Delete the file
#os.remove("test.txt")
