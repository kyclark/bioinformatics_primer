#!/usr/bin/env python3

person = {}
print(person)

print('\n'.join([
    'Stop!', 'Who would cross the Bridge of Death',
    'Must answer me these questions three,',
    '\'ere the other side he see.'
]))

for field in ['name', 'quest', 'favorite color']:
    person[field] = input('What is your {}? '.format(field))
    print(person)

if person['favorite color'].lower() == 'blue':
    print('Right, off you go.')
else:
    print('You have been eaten by a grue.')
