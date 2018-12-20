import re


s = str(input('What is your name?\n'))
name = re.sub('My name is | is my name.?', '', s)
print('Hello, ', name + '!')
