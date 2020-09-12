mystring = "Hello World"
print(mystring)

''' INDEXING'''

'''Grab and print letter H '''
print(mystring[0])

'''Grab and print letter r '''
print(mystring[8])

'''Grab and print letter l with normal indexing and reverse indexing '''
print(mystring[9])
print(mystring[-2])

'''Grab and print last letter '''
print(mystring[-1])

print("\n")

''' SLICING'''
mystring = 'abcdefghijk'

'''Grab and print a subsection of the string ('cdefghijk') '''
print(mystring[2:])

'''Grab and print a subsection of the string ('abc') '''
print(mystring[:3])
# Go up to 3 but not include it that index position (go to letter 'd' but not include it).

'''Grab and print a subsection of the string ('def') '''
print(mystring[3:6])

'''Grab and print a subsection of the string ('bc') '''
print(mystring[1:3])

'''Grab and print a subsection of the string ('defghi') '''
# Positive
print(mystring[3:9])
# Start positive - Stop reverse
print(mystring[3:-2])
# Start reverse - Stop positive
print(mystring[-8:9])
# Start reverse - Stop reverse
print(mystring[-8:-2])

''' Step Size'''
'''Grab everything from the beginning of the string all the way to the end '''
print(mystring[::1])
print(mystring[::2])
print(mystring[::-2])
