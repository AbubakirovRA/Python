def polynom(k):
    import random
    index = []
    for i in range(0, k+1):
        if i == 0:
            index.append(str(random.randint(0, 100)))
        elif i == 1:
            index.append(f'{str(random.randint(0, 100))}*x ')
        else:
            index.append(f'{str(random.randint(0, 100))}*x^{i} ')
    string = f'{str(index[k])} + '
    for j in reversed(range(k)):
        if j == 0:
            string += str(index[j])
        else:
            string += str(index[j]) + ' + '
    string = string + ' = 0'
    return string

def new_file(name_file, k):
    with open(name_file, 'w', encoding='utf-8') as file:
        file.write(polynom(k))
    return name_file


k = int(input('enter k value '))
name_file = input('enter name file ')+'.txt'
new_file(name_file, k)