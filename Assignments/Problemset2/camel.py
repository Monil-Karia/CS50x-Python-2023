def camel_to_snake(var_name):
    """
    Convert a variable name from camel case to snake case.
    """
    snake_name = ''
    for i, c in enumerate(var_name):
        if c.isupper() and i > 0:
            snake_name += '_'
        snake_name += c.lower()
    return snake_name

# Prompt the user for input
var_name = input('Enter a variable name in camel case: ')

# Convert the variable name to snake case and output the result
snake_name = camel_to_snake(var_name)
print('The variable name in snake case is:', snake_name)
