<<<<<<< HEAD
def write_to_file(name):
    print('enter the string for writing \nor empty line to close and press enter')
    with open(name, 'w', encoding='utf-8') as file:
        while (line :=input()) != '':
            file.write(f'{line}\n')
=======
print('Введите данные для записи в файл \nДля окончаниия ввода введите пустую строку')
with open('New_file.txt', 'w', encoding='utf-8') as my_file:
    while (line := input()) !='':
        my_file.write(f"{line}\n")
>>>>>>> ebe51ded323f43b388aeaa179b4dd8a856ff1554
