
import random
N = int (input ('Скільки чисел у списку?'))

l = random.sample (range(1,100),N)
l2 = l[:]
print (l)

print ('Цикл WHILE')
i = 1
while i <= N - 1:
    k = l[i]
    j = i - 1
    
    while j >= 0 and l[j] >k:
        l [j+1] = l[j]
        j = j - 1
    l [j + 1] = k
    i = i + 1

print(l)
        
print('Цикл FOR')

for i in range(1, len(l2)):
    k = l2[i]
    j = i -1
    while j >= 0 and l2[j] >k:
        l2 [j+1] = l2[j]
        j = j - 1
    l2 [j + 1] = k
print(l2)
    
