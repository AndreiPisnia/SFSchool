def func_fibo(n):
    'Function generates Fibonacci number'

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return func_fibo(n - 1) + func_fibo(n - 2) 



N = int (input('Скільки чисел сформувати в послідовності Фібоначі.'))
fibolist = []

for i in range(0, N):
    fibolist.append(func_fibo(i))

print (fibolist)                    
