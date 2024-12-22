import re
import math
from view import get_user_input

def trigon_value(expression):
    # Split the expression to extract function and value
    expression= expression.replace(' ','')
    match = re.match(r'^(sin|cos|tan|cot|cosec)(\d+(\.\d+)?)$', expression)
    trigon_function = match.group(1)
    value = float(match.group(2))
    round_degrees=4

    if trigon_function == 'sin':
        result_trigon= round(math.sin(value), round_degrees)
    elif trigon_function == 'cos':
        result_trigon= round(math.cos(value), round_degrees)
    elif trigon_function == 'cot':
        result_trigon= round((math.cos(value) / math.sin(value)), round_degrees) if math.sin(value) != 0 else "Undefined"
    elif trigon_function == 'tan':
        result_trigon= round(math.tan(value), round_degrees) if math.cos(value) != 0 else "Undefined"
    elif trigon_function == 'sec':
        result_trigon= round(1/ math.sin(value), round_degrees) if  math.sin(value) != 0 else "Undefined"
    else:
        result_trigon= "Invalid Function"
    return result_trigon




