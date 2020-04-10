# Lists

numlist = [1, 2, 3, 4, 5]

print(numlist)

# To reverse list
numlist.reverse()
print(numlist)

# sort 
numlist.sort()
print(numlist)

# to print all values in list
for num in numlist:
	print(str(num))

# cut string to list
mystring = 'carlone'
l = list(mystring)
print(l)

# returns last element and removes it from list
l.pop()
print(l)

# insert into list index and element
l.insert(6, 'e')
print(l)

# 
l[0] = 'k'
print(l)
# deletes an element
del l[0]
print(l)

l.insert(0, 'f')
print(l)

l.append('S')
print(l)

# lists are mutable
# tiples are immutable
# REMEMBER dictionaries are unordered

things = {'mouse': 100, 'laptop': 1500, 'monitor': 200}

# add items to list
things['book'] = 30

print(things.keys())
print(things.values())
print(things.items())

# print each keys 
for keys in things.keys():
	print(keys)

for value in things.values():
	print(value)

for keys, values in things.items():
	print(keys + str(values))

for keys, values in things.items():
		print('%s costs %d dollars' %(keys, values))


