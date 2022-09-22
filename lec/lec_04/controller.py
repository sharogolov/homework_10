from statistics import mode
import  model_exp as model
import view

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    num = view.get_oper()
    model.init(value_a, value_b)
    result = model.do_it()
    view.view_data(result, "resul")