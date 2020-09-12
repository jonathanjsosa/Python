'''
Immutability.
Immutate or you can't mutate or can't change.
'''

name = "Sam"
'''Now we want to change the name to Pam'''
# name[0] = "P" --- str objects does not support item assignment.

''' Concatenation (plus/+) '''
name = "P" + name[1:]
print(name)

x = "Hello World"
x = f"{x} it is beautiful outside!"
x = f"{x} it is beautiful outside!"
print(x)


''' String Multiplication '''
letter = "z"
print(letter * 10)


''' YOU ARE GONNA GET AN ERROR IF YOU TRY TO CONCATENATE A NUMBER WITH A STRING '''
print(2 + 3)
# 5 (int)
print('2' + '3')
# 23 (str)

''' ~~~~~~~~~ BUILT-IN STRING METHODS ~~~~~~~~~ '''

''' UPPERCASE   -   This method is not IN PLACE (it doesn't actually affect the original str) '''
x = "Hello World"
print(f"UPPERCASE (.upper()) = {x.upper()}")
x = x.upper()
print(f"x = x.upper() in order to affect the original str {x}")

'''
x.upper()   - Call the function
x.upper     - Just ask to Python what is that
'''


''' lowercase '''
print(f"lowercase (.lower()) = {x.lower()}")

''' split '''
print(x.split())

x = "Hi this is a string"
print(x.split())
print(x.split("i"))
# H, _th, s_, s_a_str, ng


'''
Strings FAQ

1. Are strings mutable?

Strings are not mutable! (meaning you can't use indexing to change individual elements of a string)

2. How do I create comments in my code?

You can use the hashtag # to create comments in your code
'''