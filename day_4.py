
from collections import defaultdict, namedtuple, Counter, deque
import csv
import random
from urllib.request import urlretrieve


# namedtuple
user = ('bob', 'coder')
#print(f'{user[0]} is a {user[1]}')

User = namedtuple('User', 'name role')

user = User(name = 'bob', role = 'coder')
#print(user.role)

#print(f'{user.name} is a {user.role}')

#defaultdict
users = {'bob': 'coder'}
print(users['bob'])
# print(users.get('jilian')) # returns error

# If you want to print a user that doesn't have a key this throws and error
# To get around this:

words = """Lorem Ipsum is simply dummy test of the printing and typesetting industry.
Lorem Ipsum is the industry's standard dummy text ever since the 1500's, when and unknown 
printer took a gallery of words and scrambled it to make a type specimen book.""".split()

print(Counter(words).most_common(5))

print(users.get('jilian') is None) # returns true

challenges_done = [('mike', 10), ('julian', 7), ('bob', 5),
					('mike', 11), ('julian', 8), ('bob', 6)]

#challengess = {}
#for name, challenge in challenges_done:
#	challenges[name].append(challenge)
# Throws an error

challenges = defaultdict(list)
for name, challenge in challenges_done:
	challenges[name].append(challenge)

print(challenges[name])

Measurement = namedtuple(
	'Measurement',
	'temp, lat, long, quality')
m = Measurement(22, 44, 19.5, 'strong')

print(m.temp)

# Class

class Creature:
	def __init__(self, name, level):
		self.name = name
		self.level = level

	def walk(self):
		print('{} walks around'.format(
			self.name))
C = Creature("Carlone", 10)
print(C.walk())


