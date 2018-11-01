
N = int (input ('Скільки чисел в списку?'))

import random
l = random.sample(range(1, N*10), N)
print('Input list : {}'.format(l))


for i in range(N-1):
    for j in range(N-1):
        if l[j] % 2 != 0 and l[j+1] % 2 == 0 or l[j] % 2 == l[j+1] % 2 and l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]

           
print('Output list {}'.format(l))
