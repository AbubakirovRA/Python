# 32. Дана последовательность чисел.
# Получить список уникальных элементов заданной последовательности.

def get_unique(list):
    i = 0
    unique = []
    while i < len(list):
        if check_element(list, list[i], i):
            unique.append(list[i])
            i +=1
        else:
            i +=1
        
    return unique

def check_element(list, element, count):
    exception_index = []
    i= count +1
    while i < len(list):
        if i == len(list)-1:
            if list[i] == element:
                return False
            else:
                return True
        elif list[i] == element:
            exception_index.append(i)
        i +=1

list = [1, 4, 7, 8, 10, 3, 4, 7, 1, 7, 1]
print(get_unique(list))


