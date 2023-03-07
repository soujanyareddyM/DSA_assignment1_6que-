def prefix_to_infix(prefix_expr):
    operators = set(['+', '-', '*', '/', '^'])
    stack = []
    for char in reversed(prefix_expr.split()):
        if char in operators:
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append(f"({operand1} {char} {operand2})")
        else:
            stack.append(char)
    return stack.pop()

# Example 
prefix_expr = "* + 2 3 4"
infix_expr = prefix_to_infix(prefix_expr)
print(infix_expr)