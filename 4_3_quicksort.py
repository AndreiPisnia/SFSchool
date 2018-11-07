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
        if l[j] <= splitter:
            i = i + 1
            l[i], l[j] = l[j], l[i]
    l[i+1], l[end] = l[end], l[i+1]
    return i + 1

def quick_sort(lst, start, end):
    """
    Sorts list using quick sort algorithm.
    This is iterativ implementation of quick sort algorithm.
    """
    stack = []
    stack.append(start)
    stack.append(end)
    while stack:
        end = stack.pop()
        start = stack.pop()
        s = split(lst, start, end)

        if s - 1 > start:
            stack.append(start)
            stack.append(s - 1)

        if s + 1 < end:
            stack.append(s + 1)
            stack.append(end)

quick_sort(lst, 0, len(lst) -1)
print('Output list : {}'.format(lst))



