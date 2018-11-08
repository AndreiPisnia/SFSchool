def func_factorial(n):
    if n < 0:
        return -1
    elif n < 2:
        return 1
    else:
        return n * func_factorial(n - 1)

N = int(input('Для якого числа порахувати факторіал?'))
print('Факторіал числа {} :{}'.format(N, func_factorial(N)))
         
         
