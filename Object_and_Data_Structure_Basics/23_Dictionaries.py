'''
DICTIONARIES.
Unordered mapping for storing objects.
Key-Value pair

Syntax:
{"key1": "value1", "key2": "value2"}

Dictionaries: Objects retrieved by key name. Unordered and can not be sorted.
Lists: Objects retrieved by location. Ordered Sequence can be indexed and/or sliced.
'''

my_dict = {"key1": "value1", "key2": "value2"}
print(my_dict)

''' Grab a dictionary value'''
print(my_dict["key1"])
# value1

prices_lookup = {'apple': 2.99, 'oranges': 1.99, 'milk': 5.80}
print(prices_lookup)
print(prices_lookup['apple'])

d = {'k1': 123, 'k2': [0, 1, 2], 'k3': {'inside_key': 100}}
''' Grab the value of k1'''
print(d['k1'])
''' Grab the value of k2/ 2nd element (number 1)of the list '''
print(d['k2'][1])
''' Grab the value of 100 in k3 '''
print(d['k3']['inside_key'])

d = {'key1': ['a', 'b', 'c']}
''' Grab c and turns it UPPER'''
print(d['key1'][2].upper())

''' Adding pairs '''
d = {'key1': 100, 'key2': 200}
d['key3'] = 300
print(d)

''' Overwrite pairs '''
d['key3'] = 'NEW VALUE'
print(d)

''' DELETE pairs '''
d = {'k1': "Hola", 'k2': 30, 'k3': 20.5, 'k4': "Mundo"}
print(d)
# Remove a particular item, returns its value
popped_pair_value = d.pop('k4')
print(popped_pair_value)
print(d)
# Remove an arbitrary item, return (key,value), it seems removes the last key-value pair
d['k4'] = "lol"
arbitrary_popped_pair_value = d.popitem()
print(arbitrary_popped_pair_value)
print(d)
# Remove ALL key-value pairs
d.clear()
print(d)


'''
Dictionaries methods
'''
d = {'k1': 100, 'k2': 200, 'k3': 300}

# .keys() to return a list of keys
print(d.keys())

# .values() to return a list of values
print(d.values())

# .items() to return a list of tuples
print(d.items())

'''
1. Do dictionaries keep an order? How do I print the values of the dictionary in order?

Dictionaries are mappings and do not retain order! If you do want the capabilities of a 
dictionary but you would like ordering as well, check out the ordereddict object lecture 
later on in the course!
'''