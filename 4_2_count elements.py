    #Program counts elements in the string

text = 'His name is Andrei. His name is Max. Her name is Nadia.'
print(text)

text2 = text.replace('.', '')    #Replace '.' dots in the end of sentences.
lst = text2.split()              #Split elements and convert to list
lst.sort()                       #Sort list 

name = ''
count = 0
lst_sorted = []

for i in range(0,len(lst)):       #Count element and make new list.
    new_name = lst[i]
    if new_name != name:
        count = str(lst.count(new_name))
        new_element = new_name+':'+count
        lst_sorted.append(new_element)
        name = new_name
        
print(lst_sorted)
    
