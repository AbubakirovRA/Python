import calc_model
import view

def button_click():
    value_a = view.get_value()
    math_action = view.get_math_action()
    value_b = view.get_value()
    calc_model.init(value_a, value_b)
    if math_action == '+':
        result = calc_model.sum()
    elif math_action == '-':
        result = calc_model.dif()
    elif math_action == '*':
        result = calc_model.mult()
    elif math_action == '/':
        result = calc_model.div()
    view.view_data(result)