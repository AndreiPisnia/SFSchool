# Merge sort

def merge_sort(l):
    'Function for Recursive Merge Sort'

    if len(l) > 1:
        mid = len(l) // 2
        L = l[:mid]
        R = l[mid:]
        
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] > R[j]:
                l[k] = R[j]
                j += 1
            else:
                l[k] = L[i]
                i += 1
            k += 1
        if i < len(L):
            l[k: k + len(L[i:])] = L[i:]
        if j < len(R):
            l[k: k + len(R[j:])] = R[j:]

           
N = int (input('Введіть довжину списку.'))
import random
a = random.sample (range(1, 10*N), N)
print ('Input list : {}'.format (a))

merge_sort(a)

print ('Output list : {}'.format (a))

        
