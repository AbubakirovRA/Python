<<<<<<< HEAD
def new_file():
    name_file = input('enter name file ')+'.txt'
    with open(name_file, 'w', encoding='utf-8') as file:
        file.write('')
    return name_file
=======
def create_file():
    with open('New_file.txt', 'w', encoding='utf-8') as my_file:
        my_file.write('')

create_file()
>>>>>>> ebe51ded323f43b388aeaa179b4dd8a856ff1554
