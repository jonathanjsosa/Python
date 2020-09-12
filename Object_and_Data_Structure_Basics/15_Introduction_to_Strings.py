'''
Because strings are ordered sequences (specific position)
it means we can using indexing and slicing to grab a
subsection of the string.

Indexing allows us to grab a single character from the
string.
Indexing notation uses [] notation after the string (or
variable assigned the string). These actions use [] square
brackets and a number index to indicate positions of what
you wish to grab.

Character:  h  e  l  l  o
Index:      0  1  2  3  4
Reverse:    0 -4 -3 -2 -1
string[1] = 'e'

Slicing allows you to grab a subsection of multiple
characters, a slice of the string.
Syntax:
        [start:stop:step]

start:  is a numerical index for the slice start.
stop:   is the index you will go up to (BUT NOT INCLUDE)
step:   is the size of the jump you take
'''

'''Words (Double & Single Quotes)'''
greetings1 = "Hello"
print(greetings1)
greetings2 = 'World'
print(greetings2)

'''Whole Phrases (Double & Single Quotes)'''
greetings3 = "this is also a string"
print(greetings3)
greetings4 = 'this is also a string'
print(greetings4)

'''WHITE SPACES COUNT LIKE A CHARACTER INSIDE THE STRING'''


'''MIXING SINGLE AND DOUBLE QUOTES'''
# print('I'm going on a run'')
# Python thinks the phrase ends in 'I' and ignores the last
# '
print("I'm going on a run")

''' print function '''
print("hello")

''' scape sequences '''
#new line
print("hello \nworld")

#tab
print("hello \tworld")

''' len function'''
print(len('hello'))
print(len('hello world'))
