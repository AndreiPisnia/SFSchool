
import random
a = random.randint (1,10)
#print (a)  - для можливого контролю 

print ("Комп'ютер загадав число. Спробуйте угадати його.")

counter = 1
number = ''

while number != a:
    number = int (input ('Введіть число.'))
#    print ('Ви ввели число "', number, '"')
    if number == a:
        print ('Ви вгадали! Загадане число', a, '. Молодець!')
    else :
        if number < a:
            print ('Ви не вгадали. Загадане число більше. Спробуйте ще раз')
        else:
            print ('Ви не вгадали. Загадане число менше. Спробуйте ще раз') 
