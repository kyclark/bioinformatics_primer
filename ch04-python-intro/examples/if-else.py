#!/usr/bin/env python3
"""conditions"""

name = input('What is your name? ')
age = int(input('Hi, ' + name + '. What is your age? '))

if age < 0:
    print("That isn't possible.")
elif age < 18:
    print('You are a minor.')
else:
    print('You are an adult.')
