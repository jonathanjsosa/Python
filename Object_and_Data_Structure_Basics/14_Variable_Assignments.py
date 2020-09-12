# Python uses Dynamic Typing
# This means you can reassign variables to different data types.

a = 5
print(a)

a = 10
print(a)

print(a + a)

a = a + a
print(a)

a = a + a
print(a)

print("\n")
'''type built-in function'''
print(type(a))

a = 30.1
print(type(a))

# int = 4
# Error because int is a built-in name

my_income = 100
tax_rate = 0.1
my_taxes = my_income * tax_rate
print(my_taxes)
