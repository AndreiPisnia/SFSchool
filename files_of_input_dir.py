#!/usr/bin/python

'''print list of directories and files from given directory'''

from pathlib import Path

p = input('Enter path to directory in format "/home/dir" \n')
path = Path(p)

for directory in path.iterdir():
    if directory.is_dir():
        print(directory)
print('-'*20)
for file in path.iterdir():
    if file.is_file():
        print(file)

