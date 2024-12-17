import re 
order_operations=['/','%','**','*','+','-']


def split_bodmas(expression):
    # Use regular expression to split the string, keeping operators with the numbers
    result = re.findall(r'\d+\.?\d*|[+\-*/%()]', expression)
    print(result)
    for op in order_operations:
        while op in result:
            if op in result:
                position = result.index(op)
                # Find the position of '%' in the expression
                position = result.index(op)
                val1=float(result[position-1])
                val2=float(result[position+1])
                if op=='+':
                    result1=val1+val2
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

    return result[0]


