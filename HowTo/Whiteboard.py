import random
import sys
import os

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

print('My', drone_components[0], 'will', drone_tasks[0])
print('')
print('My', drone_components[1], 'and', drone_components[4], 'will allow me to', drone_tasks[2])
print('')

drone = [drone_tasks, drone_components]
print('DojoDrone has been fitted with a', drone[1][2], 'in order to', drone[0][5], 'my diabetes.')
print('')

drone_directives = ['to see', 'to know', 'to learn']

drone.append(drone_directives)
print('I am', drone_components)
print('')
print('I will', drone_tasks)
print('')
print('My directives are', drone[2][0], ',', drone[2][1], 'and', drone[2][2], '.')
