
N = int (input ('До якого числа сформувати послідовність Фібоначі?'))
print (N)

fibo = []
#print (fibo) якщо буде необхідно перевірити роботу програми

num1 = 0
num2 = 1
nextnumber = 0
fibo.append (num1)
fibo.append (num2)
#print (fibo) якщо буде необхідно перевірити роботу програми

while nextnumber < N:
    nextnumber = num1 + num2
    num1 = num2
    num2 = nextnumber
#    print (num1, num2, nextnumber) якщо буде необхідно перевірити роботу програми

    if nextnumber <= N:
        fibo.append (nextnumber)
        
print (fibo)


