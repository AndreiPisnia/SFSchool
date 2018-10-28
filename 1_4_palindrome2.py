
#Програма перевіряє чи є введене слово паліндромом

word = input ('Введіть, будь ласка, слово.')
word2 = word[::-1]

x = word.find (word2)

if x == 0:
    print ('The word "{}" is palindrom.' .format(word))
else:
    print ('The word "{}" is not palindrom.' .format(word))
