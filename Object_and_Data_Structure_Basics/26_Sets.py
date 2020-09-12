'''
Sets

Unordered collection of unique elements.
'''

myset = set()
print(myset)

myset.add(1)
print(myset)

myset.add(2)
print(myset)

''' Sets doesn't accept repeated values '''
myset.add(2)
print(myset)


''' 
Using .add() is not useful to add items to the set 


Instead what might be useful is casting a list to set that we ony get the unique values
'''

mylist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3]
myset= set(mylist)
print(mylist)
print(myset)
