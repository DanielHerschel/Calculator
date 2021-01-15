# Dictionary of the operators and their levels.
operator_dic = {
    # Level 1
    '+': 1,
    '-': 1,
    # Level 2
    '*': 2,
    '/': 2,
    # Level 3
    '^': 3,
    # Level 4
    '%': 4,
    # Level 5
    '@': 5,
    '$': 5,
    '&': 5,
    # Level 6
    '~': 6,
    '!': 6
}

# Operators with two operands.
two_operands = {'+', '*', '/', '-', '^', '%', '@', '$', '&'}
# Operators with one operand.
one_operand = {'!', '~'}

def calculate(equation):
    """
    :param equation: list
    :return: a float that is the answer if the equation.
    For each parentheses (from the outside to the inside)
    run this function for the equation inside them
    recursivly.
    For example:

    for:
    (2 + (7 - 5)) + 3
    run like this:
    solve_equation((2 + (7 - 5)) + 3)
    solve_equation(2 + (7 - 5))
    solve_equation(7 - 5)
    """

    i = 0
    while i < len(equation): # Find all the parentheses

        if equation[i] == '(': # If found an open parentheses
            start_index = i + 1 # Index of the first parentheses
            count = 1 # Count checks if the closing parentheses
            # is closing the current open parentheses.
            while count != 0: # Find the closing parentheses
                # of the open parentheses.
                i = i + 1
                if equation[i] == '(': # Increase count by 1
                    # if found open parentheses.
                    count = count + 1
                elif equation[i] == ')': # Decrease count by 1
                    # if found closing parentheses.
                    count = count - 1

            result = calculate(equation[start_index: i]) # Run this
            # function for the equation found in the parentheses.
            for j in range(i - start_index + 1): # Pop all the elements
                # of the equation we solved (until the closing parentheses).
                equation.pop(start_index)
            equation[start_index - 1] = result # Replace the element that's
            # before start_index with the result (will always be
            # the opening parentheses).
            i = -1 # Assign -1 to i to start over the search for parentheses
            # (I assign -1 because i do i = i + 1 right after that).

        i = i + 1 # Skip all the elements that are not open parentheses.

    return solve_simple_equation(equation) # If not found any parentheses
    # in the equation, run solve_simple_equation.


def solve_simple_equation(equation):
    """
    :param equation: list
    :return: a value that is the answer of the simple equation
    a simple equation is an equation with no parentheses.
    """

    # TODO: solve the simple equation given in the equation list.
    #  Solve via the rules of the levels of the operands.

    if len(equation) == 1: # Stop condition. When there is only 1 operand left.
        return equation[0]

    global operator_dic, two_operands, one_operand
    max_level_operator = '' # Operator with max level in the equation.
    max_level_operator_index = 0 # Index of the max level operator.

    for i in range(len(equation)): # Go over the equation.
        if isinstance(equation[i], str): # If it's a string
            if max_level_operator == '': # Check if not found an operator yet.
                max_level_operator = equation[i] # Assign the operator.
                max_level_operator_index = i # Assign the index of
                # the operator.
            elif operator_dic[equation[i]] > operator_dic[max_level_operator]:
                # If found an operator already, check if the current one has
                # a higher level.
                max_level_operator = equation[i]  # Assign the operator.
                max_level_operator_index = i  # Assign the index of

    operator = max_level_operator # Just to make it easier to write.
    index = max_level_operator_index # Just to make it easier to write.

    # Handle operators that should be with two operands.
    if operator in two_operands:

        # Handle minuses
        if operator == '-' and index == 0 and len(equation) == 2:
            # If the operator is minus, it's at the start of the equation
            # and the length of the equation is 2
            return -equation[1]
        elif operator == '-' and index == 0 and len(equation) > 2 \
                and operator_dic[equation[index + 2]] == \
                operator_dic[operator]:
            # If the operator is minus, it's at the start of the equation,
            # the length of the equation is 2 and the operator after has the
            # same level as minus.
            equation.pop(0)
            equation[0] = -equation[0]
        else: # Normal operator
            if equation[index + 1] == '-': # If there is a minus after the
                # operator.
                equation.pop(index + 1)
                equation[index + 1] = -equation[index + 1]

            result = solve_two_operand(
                equation[index - 1:index + 2]) # Solve an equation with two
            # operands.

            # Format the list.
            equation.pop(index) # Erase the operator.
            equation.pop(index) # Erase the second operand.
            equation[index - 1] = result # Replace the first operand with the
            # result.
    else: # Operator with one operand.
        result = solve_one_operand(equation[index - 1:index + 1]) # Solve an
        # equation with one operand.
        equation.pop(index) # Erase the operator
        equation[index - 1] = result # Replace the operand with the result.

    return solve_simple_equation(equation)


def solve_two_operand(equation):
    """
    :param equation: list
    :return: a floating point number that is the result of an
    equation with two operands and one operator.
    """
    operand1 = equation[0] # Always in the first place.
    operand2 = equation[2] # Always in the third place.
    operator = equation[1] # Always in the second place.

    # Check which type of operator we got and solve it accordingly.
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return  operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2
    elif operator == '^':
        return pow(operand1, operand2)
    elif operator == '%':
        return  operand1 % operand2
    elif operator == '@':
        return  (operand1 + operand2) / 2
    elif operator == '$':
        return  max(operand1, operand2)
    elif operator == '&':
        return min(operand1, operand2)

    return  0 # Just for emergency.


def solve_one_operand(equation):
    """
        :param equation: list
        :return: a floating point number that is the result of an
        equation with one operand and one operator where the operator is
        after the operand.
    """
    operand = equation[0] # Always in the first place.
    operator = equation[1] # Always in the second place.

    # Check which type of operator we got and solve it accordingly.
    if operator == '!':
        return factorial(int(operand))
    if operator == '~':
        return -operand

    return 0 # Just for emergency.


def factorial(x):
    """
    :param x: int
    :return: factorial of x.
    """
    result = 1
    while x > 0:
        result *= x
        x = x -1

    return result
