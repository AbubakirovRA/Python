# 24 В заданном списке вещественных чисел найдите разницу 
# между максимальным и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# complete = [1.1, 1.2, 3.1, 5.2553, 10.015]

# def Max(arr):
#     max = arr[0]
#     i = 1
#     while i < len(arr):
#         if arr[i] > max:
#             max = arr[i]
#         i+=1
#     return max

# def Min(arr):
#     min = arr[0]
#     i = 1
#     while i < len(arr):
#         if arr[i] < min:
#             min = arr[i]
#         i+=1
#     return min


# def Difference(arr,x):
#     fraction = []
#     for i in arr:
#         fraction.append(round(i-int(i),x))
#     return (Max(fraction)- Min(fraction))

# print(Difference(complete, 4))

