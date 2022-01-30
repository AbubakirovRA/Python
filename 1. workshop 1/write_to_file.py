print('Введите данные для записи в файл \nДля окончаниия ввода введите пустую строку')
with open('New_file.txt', 'w', encoding='utf-8') as my_file:
    while (line := input()) !='':
        my_file.write(f"{line}\n")