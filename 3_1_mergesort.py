# Merge sort

N = int (input('Введіть довжину списку.'))
import random
a = random.sample (range(1, N*10), N)
print ('Input list : {}'.format (a))

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
print ('Output list : {}'.format (a))

        
