#!/usr/bin/python

#import os
#files = os.listdir()
#for file in files:
#    print(file)

'''print list of directories and files from current directory'''

from pathlib import Path
path = Path()

for directory in path.iterdir():
    if directory.is_dir():
        print(directory)
print('-'*20)
for file in path.iterdir():
    if file.is_file():
        print(file)


#x = [f.name for f in path.iterdir() if f.is_file()]
#for f in x:
#    print(f)
