import random

# ---------------------------- #

def welcome():
    print('Welcome to "Guess the Number". Would you like to play?')
    x = input()
    if str(x) == 'y' or 'Y' or 'Yes':
        print("Great! Let's begin!")
        difficulty()
    elif str(x) == 'n' or 'N' or 'No':
        print("No worries. Goodbye for now!")

def difficulty():
    d = 0
    print('What number range would you like?')
    print('1. Casual = 1-10\n2. Normal = 1-20\n3. Hard = 1-30\n4. INSANE =  1-100')
    x = input()
    if str(x) == '1':
        d = 10
    elif str(x) == '2':
        d = 20
    elif str(x) == '3':
        d = 30
    elif str(x) == '4':
        d = 100
    newGame(d)

def newGame(d):
    n = random.randint(1,int(d)) # number to be guessed
    a = 0 # attempts
    print('A number has been locked in place!')
    print('All you need to do, is guess the number in as few attempts as possible. The fewer the attempts, the better the prize!')
    print('Now for your first attempt! Enter your guess below:')
    x = input() # user input
    a += 1 # increment no. of attempts
    if int(x) == int(n):
        print('You Win! And on your first attempt! Amazing!')
        print("You'll be added to the Guess the Number hall of fame!")
        gameOver(a)
    elif int(x) != int(n):
        print("Sorry! That's incorrect! Give it another go!")
        guessAgain(n, a)

def guessAgain(n, a):
    print("Enter your guess below:")
    print("THE CORRECT NO. IS = " + str(n) + ".") #DEV CHEAT
    x = input()
    numberVerifier(x, n, a)

def numberVerifier(x, n, a):
    a += 1 # increment no. of attempts
    if int(x) != int(n):
        print("Sorry! That's incorrect! Give it another go!")
        if int(x) > int(n):
            print("Clue: Lower!")
        elif int(x) < int(n):
            print("Clue: Higher!")
        guessAgain(n, a)
    elif int(x) == int(n):
        print('You did it! ' + str(x) + ' is the correct number!')
        gameOver(a)

def gameOver(a):
    print("Your no. of attempts is " + str(a) + ".")
    print("Thank you for playing Guess the Number! We'll see you again soon!")

# ---------------------------- #

welcome()
