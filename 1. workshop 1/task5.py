# Написать программу вычисления значения функции sin(x)/x
# def f(x):
    # import math
    # return math.sin(x)

from math import * # данное выражение полностью импортирует библиотеку math
# что позволяет далее вызывать математические функции не обращаясь к библиотеке
# в каждом выражении с математической функцией

def f(x):
    return sin(x)

def request_number():
    while True:
        try:
            num=float(input('enter float or integer '))
            return num
        except ValueError:
            print('You entered not float or integer! One more!')

print('Result of sin function = ', f(request_number()))