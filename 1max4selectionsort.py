
N = int (input ('Скільки чисел в списку?'))

import random
list1 = []
i = 1
while i <= N:
    list1.append (random.randint (1, N * 10))
    i = i + 1
#print (list1)   #- для перевірки роботи

i = 0
temp = 0

while i < N - 1:
    i_min = i    
    j = i + 1
    while j < N:
        if list1 [i_min] > list1 [j]:
            i_min = j
        j = j + 1

    temp = list1 [i]    
    list1 [i] = list1 [i_min]
    list1 [i_min] = temp
#    print ('i =', i, list1 [i], 'i_min =', i_min, list1 [i_min], 'j =', j)
    i = i + 1

print (list1)
