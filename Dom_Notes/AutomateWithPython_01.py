# This program will say 'Hello' and ask you 'What is your name?'

print('Hello sir.')
print('What is your name?') # Message to User
userName = input() # User responds - Store result in variable
print('It is a pleasure to meet you, ' + userName)
print('The length of your name is: ' + str(len(userName)))
print('How old are you ' + userName + '?')
userAge = input()
print('Amazing. You will be ' + str(int(userAge) + 1) + ' in a year.')
