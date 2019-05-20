import random # Module for random number generators
import sys # Module that provides access to variables used and maintained by the interpreter
import os # Module for a portable way of using operating system dependent functionality

# Print to Console
print("DojoDrone")
print('')

# Array
drone_tasks = ['observe', 'analyse', 'follow', 'record', 'capture', 'monitor', 'detect', 'assist']
print('I will: ', drone_tasks[0])
print('I will: ', drone_tasks[1])
print('I will: ', drone_tasks[2])
print('I will: ', drone_tasks[3])
print('I will: ', drone_tasks[4])
print('I will: ', drone_tasks[5])
print('I will: ', drone_tasks[6])
print('I will: ', drone_tasks[7])
print('')

# Second Array
drone_components = ['camera', 'laser tracking', 'blood glucose monitor', 'GPS',
 'propellers', 'speaker', 'microphone', 'bluetooth', 'wireless', 'hard drive']
print('I have: ', drone_components[0])
print('I have: ', drone_components[1])
print('I have: ', drone_components[2])
print('I have: ', drone_components[3])
print('I have: ', drone_components[4])
print('I have: ', drone_components[5])
print('I have: ', drone_components[6])
print('I have: ', drone_components[7])
print('I have: ', drone_components[8])
print('I have: ', drone_components[9])
print('')

# Using two Array elements in a single string
print('My', drone_components[0], 'will', drone_tasks[0])
print('')
print('My', drone_components[1], 'and', drone_components[4], 'will allow me to', drone_tasks[2])
print('')

# 2D Array
drone = [drone_tasks, drone_components]
print('DojoDrone has been fitted with a', drone[1][2], 'in order to', drone[0][5], 'my diabetes.')
print('')

drone_directives = ['to see', 'to know', 'to learn']

# Adding an Array to an Array ('Arrayception')
drone.append(drone_directives)
print('I am', drone_components)
print('')
print('I will', drone_tasks)
print('')
print('My directives are', drone[2][0], ',', drone[2][1], 'and', drone[2][2], '.')
print('')

drone_components.insert(10, 'Fart Noise Generator')
print(drone_components)
drone_components.remove('Fart Noise Generator')
print(drone_components)

#file = open("C:\\Users\\Dojod\\Documents\\Learning-Python\\HowTo\\chalkboard.txt", "w+") # If file doesn't exists, create one called 'chalkboard.txt'
#for a in drone: # For every Array(a) in Drone(array)
    #for i in a: # For every Item(i) in Array*fromDrone(a)
        #string = i + ' \n' # Write each item from Array(a) with a space added and new line after each
        #file.write(string) # Write to file
#file.close() # Close file

drone_maxDistance = 20
drone_minDistance = 1
drone_distance = 8 # Metres
drone_inRange = False

if drone_distance > 20 :
    drone_inRange = False
    print('Drone is not in range.')
    print('drone_inRange = ' + str(drone_inRange))
    print('drone_distance = ' + str(drone_distance))
    print('')
else :
    drone_inRange = True
    print('Drone is in range.')
    print('drone_inRange = ' + str(drone_inRange))
    print('drone_distance = ' + str(drone_distance))
    print('')

if drone_distance >= 21 :
    print('I am out of range!')
    print('')
elif drone_distance >= 5 :
    print('I am within range!')
    print('')
else :
    print('I am following you!')
    print('')

if (drone_distance < 21) and (drone_distance > 5) :
    print('I am within range!')
    print('')
elif (drone_distance < 5) and (drone_distance > 0) :
    print('I am folllowing you!')
    print('')
elif (drone_distance > 21) :
    print('I am out of range!')
    print('')
else :
    print('Error')
    print('')

print('What would you like me to do?')
command = sys.stdin.readline()
print('Beginning ', command, 'routine now.')

drone_component_ids = (1,2,3,4,5,6)

list = list(drone_component_ids) # Contents can be edited
tuple = tuple(list) # Contents cannot be edited

print(list)
print(tuple)
print(len(tuple))
print(min(tuple))
print(max(tuple))

# Functions
def greeting():
    print('Good morning sir!')

greeting()

def checkBloodLevels():
    print('Blood sugar levels -> 7.6')

checkBloodLevels()
