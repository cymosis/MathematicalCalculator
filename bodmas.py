import re

# Correct order of operations based on BODMAS
order_operations = ['**', '*', '/', '%', '+', '-']

def split_bodmas(expression):
    expression=expression.replace(' ','')
    print(expression)
    result = re.findall(r'\d+\.?\d*|[+\-*/%()]', expression)
    print(result)
    for op in order_operations:
        while op in result:
            if op in result:
                position = result.index(op)
                print(position)
                position_before=result[position-2]
                print(position_before)
                val1=float(result[position-1])
                val2=float(result[position+1])
                if op=='+' and position_before=='-':
                    val1=-1*val1
                    result1=-1*(val1+val2)
                elif op=='+':
                    result1=val1+val2
                elif op=='-' and position_before=='-':
                    val1=-1*val1
                    result1=val1-val2
                elif op=='-':
                    result1=val1-val2
                elif op=='/':
                    result1=val1/val2
                elif op=='%':
                    result1=val1%val2
                elif op=='*':
                    result1=val1*val2
                elif op=='**':
                    result1=val1**val2


                result = result[:position - 1] + [str(result1)] + result[position + 2:]
                print(result)
    return result[0]

