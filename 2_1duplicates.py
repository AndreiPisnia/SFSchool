
# Сформуємо список із повторюваними елементами

import random
N = int(input('How many numbers in list?'))
l = []
for i in range(N):
    n = random.randint(1, 10)
    l.append(n)
print('Input list : {}'.format(l))

#Видалимо елементи, що поторяються.

for i in l[:-1]:
    for j in l[l.index(i) + 1:]:
        if j == i:
            l.remove(j)
print('Output list : {}'.format(l))
