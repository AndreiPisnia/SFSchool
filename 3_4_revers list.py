# Revers list

def revers_list(l):
    'Function reverses list from end to start'

    if len(l) > 1:
        mid = len(l) // 2
        left = l[:mid]
        right = l[mid:]
        
        revers_list(left)
        revers_list(right)

        i = j = k = 0

        l[k: k + len(right[j:])] = right[j:]
        k = k + len(right[j:])
        l[k: k + len(left[i:])] = left[i:]

import random
N = int (input('Введіть довжину списку.'))
lst = random.sample (range(1, 100), N)
#lst = random.sample (range(1, 100), 21)
print ('Input list : {}'.format (lst))

revers_list(lst)

print ('Output list : {}'.format (lst))

        
