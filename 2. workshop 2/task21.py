# 21. Определить, позицию второго вхождения строки в списке либо сообщить, что его нет.

list = ['q', 'w', 'e', 'r', 't', 'q', 'e', 't', 'y']
str = 'y'


def check_enter(list, str):
    count = 0
    i = 0
    while i < len(list):
        if list[i] == str:
            count += 1
        if count == 2:
            return i
        i += 1
    return "None"


print(f"Position of second enter '{str}'-line in {list} is - {check_enter(list, str)}")