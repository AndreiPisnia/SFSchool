
N = int (input ('Скільки чисел в списку?'))

import random
list1 = []
i = 1
while i <= N:
    list1.append (random.randint (1, N * 10))
    i = i + 1
#    print (list1)   - для перевірки роботи

i = 0
temp = 0

while i <= N:
    j = 0
    while j < N - 1:
        if list1 [j] <= list1 [j + 1]:
            j = j + 1
#            print (list1, i, j)    - для перевірки роботи
        else:
            temp = list1 [j]
            list1 [j] = list1 [j + 1]
            list1 [j + 1] = temp
            j = j + 1
#            print (list1, i, j)    - для перевірки роботи
    i = i + 1

print (list1)
