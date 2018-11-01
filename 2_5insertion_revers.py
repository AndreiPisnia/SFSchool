
import random
N = int (input ('Скільки чисел у списку?'))

l = random.sample (range(1,100),N)
l2 = l[:]
print (l)

for i in range(1, len(l)):
    k = l[i]
    j = i -1
    while j >= 0 and l[j] <k:
        l [j+1] = l[j]
        j = j - 1
    l [j + 1] = k
print(l)
    
