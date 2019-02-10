"""Generator for list of numbers.

"""

def gen_numbers(start=1, end_number=20, step=2):
    """Function generates list of numbers.
       User can define own start and end points of range.
       Also uset can define step for numbers.
    """
    
    number = start

    while number <= end_number:
        yield number
        number += step

nums = gen_numbers(1, 40, 3)

##nums
##print(nums)


print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
