'''
Lists
Ordered sequences of objects.
Support indexing and slicing (All ordered sequences support it).
'''

my_list = [1, 2, 3]
my_list = ['STRING', 100, 23.2]

''' Checking the list length'''
print(len(my_list))


''' Indexing and Slicing '''
mylist = ['one', 'two', 'three']

# Grab element in the index 0
index0 = mylist[0]
print(f"The element in the index 0 is '{index0}'")

# Grab from the 2nd element all the way to the end
slicing1 = mylist[1:]
print(f"The elements in the slicing are {slicing1}")


''' Concatenating lists '''
another_list = ['four', 'five']
my_new_list = mylist + another_list
print(my_new_list)

''' Mutate a list '''
# Change the first item
my_new_list[0] = 'ONE ALL CAPS'
print(my_new_list)

''' IN PLACE METHODS '''

''' Add item to the beginning of the list'''
my_new_list.insert(0, "Jonathan")
print(my_new_list)

''' Add item to the end of the list'''
my_new_list.append("six")
print(my_new_list)

''' Remove the last item of the list '''
my_new_list.pop()
print(my_new_list)

''' Remove the first item of the list '''
my_new_list.pop(0)
print(my_new_list)

'''
.pop() returns the value of the item that 'pop' off from the list.
'''
my_new_list.insert(0, 'Jonathan')
frst_element = my_new_list.pop(0)
print(frst_element)
# Jonathan

''' --------------------------------------------------------------- '''
print(my_new_list)
my_new_list.append("six")
my_new_list.append("seven")
print(my_new_list)
print(my_new_list.pop)
print(my_new_list.pop())
print(my_new_list)

popped_item = my_new_list.pop()
print(popped_item)
print(my_new_list)

# Passing index position to remove with .pop(), by default the index is -1
print(my_new_list.pop(0))
print(my_new_list)
print(my_new_list[::-1])



'''
SORT & REVERSE
'''
new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4, 1, 8, 3]

#sort method   -   IN PLACE method because it actually return anything
new_list.sort()
print(new_list)
'''
So, like .sort() doesn't return anything, do something like this doesn't have any sense:
my_sorted_list = new_list.sort()
print(my_sorted_list)
# _________ doesn't print anything cause it doesn't return any value
'''
a_list = ['a', 'c', 'i', 'b', 'd']
sorted_a_list = a_list.sort()
print(f"Sorted List: {sorted_a_list}")
# El unico que regresa valor es .pop()
appended_value = a_list.append("Hola")
print(f"Appended value: {appended_value}")

b = ['x', 'z', 'y']
b.sort()
b_sorted = b
print(b_sorted)


# NO IN PLACE method
a = "hola"
a.upper()
print(a)
#hola


print(num_list)
num_list.sort()
print(num_list)


'''
REVERSE
'''
num_list.reverse()
print(num_list)

'''
NESTED list
'''
nested_list = ["Hola", "como", ["Tengo", 100, "mi", 50.5, ["nombre", [100, "es", ["Jonathan", 15]]]], "estas"]
print(nested_list)
''' Formar la frase "Hola mi nombre es Jonathan" '''
new_nested_list = f"{nested_list[0]} {nested_list[2][2]} {nested_list[2][4][0]} {nested_list[2][4][1][1]} {nested_list[2][4][1][2][0]}"
print(new_nested_list)
print(nested_list[2][4][1][2][1])

other_nested_list = [["Esto", 105, 99.09, ["hola", 23.452, 555, [["es", 50], 15, ["lol", 13.21], [14, "programado", ["Veracruz", "Python"]]], "con"]]]
new_other_nested_list = f"{other_nested_list[0][0]} {other_nested_list[0][3][3][0][0]} {other_nested_list[0][3][3][3][1]} " \
                        f"{other_nested_list[0][3][4]} {other_nested_list[0][3][3][3][2][1]}"
print(new_other_nested_list)


x = ["one", "two", "three", "four", "five"]
x.insert(0, "zero")
print(x)

x.append("six")
print(x)

x.pop()
print(x)

popped_item = x.pop()
print(popped_item)
print(x)

x.pop(0)
print(x)



