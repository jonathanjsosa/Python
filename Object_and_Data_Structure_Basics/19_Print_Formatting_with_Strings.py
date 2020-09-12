''' STRING INTERPOLATION (stick a variable into a str for printing)

.format() method
f-strings (formatting strings literals)
'''

''' 
.format()

Syntax:
'String here {} then also {}'.format('something1', 'something2')
'''
print("This is a string {}".format('INSERTED'))

# Strings can be inserted by index position.
print('The {} {} {}'.format('fox', 'brown', 'quick'))
# The fox brown quick

print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
# The quick brown fox

print('The {0} {0} {0}'.format('fox', 'brown', 'quick'))
# The quick brown fox

# Assigning keywords
print("The {f} {b} {q}".format(f='fox', b='brown', q='quick'))
# The fox brown quick
print("The {q} {b} {f}".format(f='fox', b='brown', q='quick'))
# The fox brown quick
print("The {f} {f} {f}".format(f='fox', b='brown', q='quick'))
# The fox fox fox

print("\n")

''' Float formatting

Syntax:
{value:width.precision f}
'''
result = 100/777
print('The result was {r}'.format(r=result))
print('The result was {r:1.3f}'.format(r=result))
# Cuenta tantos numeros indiquemos en el 'precision' y si el siguiente numero es mayor a 5
# entonces se redondea
print('The result was {r:10.5f}'.format(r=result))

result = 104.12345
print('The result was {r:1.5f}'.format(r=result))
print('The result was {r:1.3f}'.format(r=result))

print("\n")

''' f-strings '''
name = 'Jonathan'
print("Hello, his name is {n}".format(n=name))
# f-strings
print(f"Hello, his name is {name}")
age = 30
print(f"{name} is {age} years old.")
