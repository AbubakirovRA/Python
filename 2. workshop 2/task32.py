# 32. Дана последовательность чисел. 
#     Получить список неповторяющихся элементов исходной последовательности
#     Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

list1 = [1, 2, 3, 0, 5, 1, 5, 14, 26, 155, 3, 10]
# list2 = sorted(list1)

# for i in reversed(range(len(list2)-1)):
#     if list2[i+1] > list2[i]:
#         continue
#     elif list2[i] == list2[i+1]:
#         list2.remove(list2[i])
# print(f'{list1} => {list2}')

list2=[]
k = 1
for j in range(len(list1)-1):
    for i in range(len(list1)-1):
        try:
            if list1[j] == list1[i+k]:
                k += 1
                break
        except ValueError:         
            if i == len(list1)-1:
                list2.append(list1[j])
                k += 1
            else:
                continue
            k = 0
print(f'{list1} => {list2}') 
