"""Create iterable object to generate list of numbers.
"""


class RangeNumbers:
    """Create iterable object to generate list of numbers in a given range
       and with given step.
       Use in for loop.
    """
    

    def __init__(self, end, step):
        self.number = 0
        self.end = end
        self.step = step
        

    def __iter__(self):
        return self

    def __next__(self):
        self.number += self.step        
        if self.number >= self.end:
            raise StopIteration
        else:
            return self.number


range_nums = RangeNumbers(20, 3)

for num in range_nums:
    print(num)

