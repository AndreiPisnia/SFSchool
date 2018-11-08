# Merge sort

import random

N = int (input('Введіть довжину списку 1:'))
l1 = random.sample (range(1, N*10), N)
N = int (input('Введіть довжину списку 2:'))
l2 = random.sample (range(1, N*10), N)
a = l1 + l2

print ('Input list 1: {}'.format (l1))
print ('Input list 2: {}'.format (l2))

n = len(a) - 1
size = 1
while size < len(a):
    l = 0
    while l < n:
        m = min(l + size - 1, n)
        r = min(l + size * 2 - 1, n)

#        merge (a,l,m,r)    майбутня функція merge

        s1 = m - l + 1
        s2 = r - m
        L = a[l: m + 1]
        R = a[m + 1: r + 1]
            
        i, j, k = (0, 0, l)

        while i < s1 and j < s2:
            if L[i] > R[j]:
                a[k] = R[j]
                j = j + 1
            else:
                a[k] = L[i]
                i = i + 1
            k = k + 1
        if i < s1:
            a[k: k + len(L[i:])] = L[i:]
        if j < s2:
            a[k: k + len(R[j:])] = R[j:]
           
        l = l + size * 2
    size = size * 2

if len(a) % 2 > 0:
    median = a[len(a) // 2]
else:
    median = (a[len(a)//2 - 1] + a[len(a)//2])/ 2

print (a)    
print ('The median is {}'.format (median))

        
