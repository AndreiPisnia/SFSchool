
import random

N = int (input ('Скільки чисел у першому списку ?'))
l1 = random.sample (range(1, 100), N)
l1.sort ()

M = int (input ('Скільки чисел в першому списку ?'))
l2 = random.sample (range(1, 100), M)
l2.sort ()

print (l1)
print (l2)

duplicates = []

for i in l1:
    for j in l2:
        if i == j:
            duplicates.append (j)

print ('Output list : {}'.format(duplicates))

