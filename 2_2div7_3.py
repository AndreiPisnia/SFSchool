
start_i = int (input ('Від якого числа перевіряти?'))
end_i = int (input ('До якого числа перевіряти?'))
l = []

i = start_i

while i <= end_i:
    if i % 7 == 0 and i % 3 != 0:
        l.append(i)
    i = i + 1
print ('Output list : {}'.format(l))
print ('У списку {} елементів, що діляться на 7 але не діляться на 3'.format(len(l)))

