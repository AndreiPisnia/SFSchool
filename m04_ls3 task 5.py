# Programm converts user name into bytes cod

name = input("Як Вас звати? \n")
#a = name.encode('utf-8')
#print(a)
print("Ваше ім'я у бінарному представленні \n")
print(" ".join(format(ord(l), 'b') for l in name))
