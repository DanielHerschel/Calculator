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


def solve_equation(equation):
    """
    :param equation: list
    :return: a float that is the answer if the equation.
    For each parentheses (from the outside to the inside) run this function for the equation inside them
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
            count = 1 # Count checks if the closing parentheses is closing the current open parentheses.
            while count != 0: # Find the closing parentheses of the open parentheses.
                i = i + 1
                if equation[i] == '(': # Increase count by 1 if found open parentheses.
                    count = count + 1
                elif equation[i] == ')': # Decrease count by 1 if found closing parentheses.
                    count = count - 1

            result = solve_equation(equation[start_index: i]) # Run this function for the equation found in the parentheses.
            for j in range(i - start_index + 1): # Pop all the elements of the equation we solved (until the closing parentheses).
                equation.pop(start_index)
            equation[start_index - 1] = result # Replace the element that's before start_index with the result (will always be the opening parentheses).
            i = -1 # Assign -1 to i to start over the search for parentheses (I assign -1 because i do i = i + 1 right after that).

        i = i + 1 # Skip all the elements that are not open parentheses.

    return solve_simple_equation(equation) # If not found any parentheses in the equation, run solve_simple_equation.


def solve_simple_equation(equation):
    """
    :param equation: list
    :return: a value that is the answer of the simple equation
    a simple equation is an equation with no parentheses.
    """

    # TODO: solve the simple equation given in the equation list. Solve via the rules of the levels of the operands.

    return 1
