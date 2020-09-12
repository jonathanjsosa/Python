int   : Whole numbers, such as = 3 300 200
float : Numbers with decimal point = 2.3  4.6  100.0
str   : Ordered sequence of characters = "hello" 'Sammy' "2000" "你好"
list  : Ordered sequence of objects = [10, "hello", 200.3]
dict  : Unordered key-value pairs = {"my_key": "value", "name": "Franklin"}
tup   : Ordered immutable sequence of objects = (10, "hello", 200.3)
set   : Unordered collection of unique objects = {"a", "b"}
bool : Logical value indicating = True or False

## Python Numbers.
#### Mod Operator
```python
print(7 % 4)
// 3
```
```python
print(50 % 5)
// 0
```
#### Power
```python
print(2 ** 3)
// 8
```
#### Order of Operations
```python
print(f"2 + 10 * 10 + 3 = {2 + 10 * 10 + 3}")
// 105
print(f"(2 + 10) * (10 + 3) = {(2 + 10) * (10 + 3)}")
// 156
```

## Variable Assignments.
#### type Function.
```python
a = 30.1
print(type(a))
// float
```
```python
a = "Hello World"
print(type(a))
// str
```
```python
a = 5
print(type(a))
// int
```

## Introduction to Strings.
#### len Function.
```python
print(len('hello'))
// 5
print(len('hello world'))
// 11
```
#### Scape Sequences.
```python
# new line - \n
print(len('hello \nworld'))
// hello
// world
# tab - \t
print(len('hello \tworld'))
// hello	world
```

## Indexing and Slicing.
#### 
```python

```



## String properties.
### NO IN PLACE Methods
#### .upper() Function.
```python
x = "Hello World"
print(x.upper())
// HELLO WORLD
```
#### .lower() Function.
```python
x = "Hello World"
print(x.lower())
// hello world
```
#### .split() Function.
```python
''' split '''
print(x.split())
# ['Hello', 'World']

x = "Hi this is a string"
print(x.split())
print(x.split("i"))
# ['H', '_th', 's_', 's_a_str', 'ng']
```
## Lists.
### IN PLACE Methods
#### .insert() Function to add item to the beginning of the list.
```python
x = ["one", "two", "three", "four", "five"]
x.insert(0, "zero")
print(x)
# ["zero", "one", "two", "three", "four", "five"]
```
#### .append() Function to add item to the end of the list.
```python
x.append("six")
print(x)
# ["zero", "one", "two", "three", "four", "five", "six"]
```
#### .pop() Function to remove the last item of the list.
```python
x.pop()
print(x)
# ["zero", "one", "two", "three", "four", "five"]
```
```python
# .pop() returns the item that we popped off
popped_item = x.pop()
print(popped_item)
# five
print(x)
# ["zero", "one", "two", "three", "four"]
```
#### .pop(index) Function to remove an item based on its index.
```python
# .pop() its index by default is -1  ---  .pop(-1)
x.pop(0)
print(x)
# ["one", "two", "three", "four"]
```
#### .sort() Function to sort a list.
```python
new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4, 1, 8, 3]

new_list.sort()
print(new_list)
# ['a', 'b', 'c', 'e', 'x']

num_list.sort()
print(num_list)
# [1, 3, 4, 8]
```
#### .reverse() Function to reverse a list.
```python
new_list.reverse()
print(new_list)
# ['x', 'e', 'c', 'b', 'a']

num_list.reverse()
print(num_list)
# [8, 4, 3, 1]
```
