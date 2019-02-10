            
class GenPrimes:
    """ Generates sequence of prime numbers
    """

    def __init__(self, stop=10):
        self.stop = stop
        self.lst = []
        self.num = 2

    def __iter__(self):
        return self

    def is_prime(self):
        while self.num <= self.stop:
            prime = True
            for p in self.lst:
                if self.num % p == 0:
                    prime = False
                    break

            if prime:
                self.lst.append(self.num)
                return self.num
            self.num += 1
        else:
            raise StopIteration

    def __next__(self):
        return self.is_prime()
        

            
N = int(input('Please input number to which generate the sequence of primes \n'))                 
numbers = GenPrimes(N)
for i in numbers:
    print(i)

