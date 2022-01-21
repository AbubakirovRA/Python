# Написать программу вычисления значения функции sin(x)/x
def f(x):
    import math
    return math.sin(x)

def data_request():
    while True:
        try:
            num=float(input('enter float or integer '))
            return num
        except ValueError:
            print('You entered not float or integer! One more!')

print('Result of sin function = ', f(data_request()))