import random

def rollTheDice():
    y = []
    c = 0;
    while len(y) != 6:
        x = random.randint(1,6)
        print(x)
        c+=1
        if x not in y:
            y.append(x)
        else:
            print('Already stored.')
    print('Process Complete!')
    print('No. of rolls = ' + str(c))

def openingQuestion():
    print('Would you like to roll the dice?')
    x = input()
    if str(x) == 'y' or str(x) == 'Y':
        print('Rolling the dice!')
        rollTheDice()
    elif str(x) == 'n' or str(x) == 'N':
        print('No worries! Have a good night!')
    else:
        print('ERROR')

openingQuestion()

def rollTheDice():
    print(random(1,6))
