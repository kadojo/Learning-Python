import random
import sys
import os

#Looping
for x in range(0,10):
    print(x, ' ', end="")

print('\n')

for y in grocery_list:
    print(y)

for z in [2,4,6,8,10]:
    print(z)

num_list = [[1,2,3],[10,20,30],[100,200,300]]

for a in range(0,3):
    for b in range(0,3):
        print(num_list[a][b])


random_num = random.randrange(0,100)

while(random_num != 15):
    print(random_num)
    random_num = random.randrange(0,100)

i = 0;

while(i <= 20):
    if(i%2 ==0): #Is number even
        print(i)
    elif(i == 9): #stop if 9 to show the break command
        break
    else:
        i += 1
        continue

    i += 1
