import random

def check_sorted(lst, size):
    """
    Check if list is sorted.
    This is recursive implementation.
    Function checks if the last element bigger than previous.
    If yes, starts to compare privious second and third elements.
    And do the same till begine of the list.
    
    """
    if size <= 1:
        print('The list is sorted.')
    
    elif lst[size - 1] >= lst[size - 2]:
        check_sorted(lst, size - 1)
    else:
        print ('The list is unsorted')


lst = [1, 9, 22, 23, 36, 38, 50, 52, 53, 55, 56, 57, 60, 75, 78]

print('Input list: {}'.format(lst))
check_sorted(lst, len(lst))
