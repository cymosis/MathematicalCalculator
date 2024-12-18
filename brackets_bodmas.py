from bodmas import split_bodmas
def evaluate_expression(expression):
    # Handle parentheses first
    while '(' in expression:
        # Find the innermost parentheses
        start_idx = expression.find('(')
        end_idx = expression.find(')', start_idx)
        
        # Extract the expression inside the parentheses
        inner_expr = expression[start_idx + 1:end_idx]
        
        # Evaluate the inner expression using split_bodmas
        result = str(split_bodmas(inner_expr))
        
        # Replace the whole parentheses expression with the result
        expression = expression[:start_idx] + result + expression[end_idx + 1:]
    
    # After all parentheses are resolved, evaluate the remaining expression
    return split_bodmas(expression)