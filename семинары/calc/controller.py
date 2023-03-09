import model_sub as model    # меняем только название модуля model_sum или model_mult или model_sub
import view

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    model.init(value_a, value_b)
    result = model.do_it()
    view.view_data(result)