'''
I/O with Basic Files in Python

Files
'''

myfile = open('myfile.txt')
print(myfile)

'''
GET AN  [Errno 2] No such file or directory: 'opsss.txt'
1.- When we pass in the wrong file name.
2.- When we didn't provide the correct file path.
'''

#myfile1 = open('opsss.txt')
#print(myfile1)


'''                                         .read() method
                                Allows you to grab everything as one giant string
'''
myfile = open('myfile.txt')
print(myfile.read())

print('Read by 2nd time')

print(myfile.read())

'''
When we try to print the content of the file by 2nd time, we get an empty string.

CAUSE:
Imagine there is a cursor at the beginning of the file.
When you .read() it, the cursor goes all the way to the end of the file.
You need to seek the cursor back to zero in order to read it again.
'''

print(myfile.seek(0))
print(myfile.read())

myfile.seek(0)
content = myfile.read()
print(content)


'''
                                            .readlines() method
                               Retrieve a list where each line in the file will be an item in the list
'''
myfile.seek(0)
content = myfile.readlines()
enhaced_content = [x.strip() for x in content]
print(enhaced_content)


'''
FILE LOCATIONS - PASSING FULL PATH FILE

Windows = \\
Linux = /
'''
print('\n')
'''
BEST PRACTICES FOR OPENING FILES.
'''
# Technically because myfile.txt is open, we actually have to close it.
# If we don't close it, if we try to open it, modify or even delete it, we are going to get an alert about the file
# is in use by the system.
myfile.close()

'''
To avoid open and close the file we can use the "with" statement
'''
with open('myfile.txt') as my_new_file:
    contents = my_new_file.read()

print(contents)
    

