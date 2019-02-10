
def gen_primes(end):
    end_primes = end
    primes = []
    num = 2
    while num <= end_primes:
        prime = True
        for p in primes:
            if num % p == 0:
                prime = False
                break

        if prime:
            primes.append(num)
            yield num
        num += 1

numbers = gen_primes(50)
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
