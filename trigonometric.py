import re
import math
from view import get_user_input

def trigon_value(expression):
    # Split the expression to extract function and value
    split_exp = expression.split(sep=' ')
    trigon_function = split_exp[0]
    value= float(split_exp[1])
    round_degrees=4

    if trigon_function == 'sin':
        result_trigon= round(math.sin(value), round_degrees)
    elif trigon_function == 'cos':
        result_trigon= round(math.cos(value), round_degrees)
    elif trigon_function == 'cosec':
        result_trigon= round(1 / math.sin(value), round_degrees) if math.sin(value) != 0 else "Undefined"
    elif trigon_function == 'tan':
        result_trigon= round(math.tan(value), round_degrees) if math.cos(value) != 0 else "Undefined"
    elif trigon_function == 'arcsin':
        result_trigon= round(1/ math.sin(value), round_degrees) if  math.sin(value) != 0 else "Undefined"
    else:
        result_trigon= "Invalid Function"
    return result_trigon




