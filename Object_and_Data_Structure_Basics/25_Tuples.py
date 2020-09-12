'''
Tuples

Are similar to lists. However they have one key difference - IMMUTABILITY
Once an element is inside a tuple, it can not be reassigned.
Tuples uses parenthesis: (1, 2, 3)
'''

t = (1, 2, 3)
my_list = [1, 2, 3]
print(type(t))
print(type(my_list))

print(len(t))
print(len(my_list))

# Mix object types
t = ('one', 2, 3.0)
print(t)

''' Slicing & Indexing'''
# Indexing
print(t[0])

#Slicing
print(t[1:])
print(t[::-1])

''' TUPLES BUILT-IN METHODS '''
t = ('a', 'a', 'b')
# .count('value') to count how many times a value occurs in the tuple
print(t.count('a'))

# .index('value') to get the index that the value we pass in, returns back the very first time the value appears in the
# tuple.
print(t.index('a'))
print(t.index('b'))

# IMMUTABILITY
mylist = [1, 2, 3]
print(mylist)
mylist[0] = "NEW"
print(mylist)

t = (1, 2, 3)
print(t)
# t[0] = "NEW"
# tuples doesn't support item reassignment


t = (1, 3.0, 'Hello', [3, 2, 5], {"key1": "value1"})
print(t)
