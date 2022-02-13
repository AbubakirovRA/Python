from fractions import Fraction
def view_data(data):
    print(data)

def get_value():
    while True:
        try:
            value = input('value = ')
            if value.find('/') != -1:
                return Fraction(value)
            elif value.find('j') != -1:
                return complex(value)
            else:
                return int(value)
        except ValueError:
            print('Check entered value!')

def get_math_action():
    while True:
        math_action = input('math_action ')
        if math_action == '+':
            return math_action
        elif math_action == '-':
            return math_action
        elif math_action == '*':
            return math_action
        elif math_action == '/':
            return math_action
        print('Check entered value!')

