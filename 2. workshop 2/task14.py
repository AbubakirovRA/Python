#14. Подсчитать сумму цифр в вещественном числе.

def sum_float_digits(num):
    digits_string = str(num).replace('.','')
    all_digits = int(digits_string)
    sum = 0
    while all_digits > 0:
        sum += all_digits % 10
        all_digits //= 10
    return sum

print(sum_float_digits(5511.1511))
