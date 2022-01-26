# 1. По двум заданным числам проверять является ли первое квадратом второго
def test_square(n1, n2):
    x1, x2 = int(n1), int(n2)
    return x1 == x2*x2

print('The first number is square of second number - ', test_square(input('enter n1 '), input('enter n2 ')))
