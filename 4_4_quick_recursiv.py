import random

lst = random.sample(range(1, 100), 15)
print('Input list: {}'.format(lst))

def split(l, start, end):
    """
    Splits list into two parts.
    Split list into two parts each element of first part
    are not bigge then every element"""

    i = start - 1
    splitter = l[end]

    for j in range(start, end):
        if l[j] >= splitter:
            i = i + 1
            l[i], l[j] = l[j], l[i]
    l[i+1], l[end] = l[end], l[i+1]
    return i + 1

def quick_sort(lst, start, end):
    """
    Sorts list using quick sort algorithm.
    This is recursive implementation of quick sort algorithm.
    """

    if start <end:
        s = split(lst, start, end)
        quick_sort(lst, start, s - 1)
        quick_sort(lst, s + 1, end)

quick_sort(lst, 0, len(lst) - 1)
print('Output list : {}'.format(lst))
