from fractions import Fraction
def view_data(data):
    print(data)

def get_value():
    value = input('value = ')
    if value.find('/') != -1:
        return Fraction(value)
    elif value.find('j') != -1:
        return complex(value)
    else:
        return int(value)

def get_math_action():
    return input('math_action ')

