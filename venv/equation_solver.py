import operators as o
import math

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
    :exception: Exception if the result of _solve_simple_equation() is a
    complex number, an infinite number or NaN.
    """

    parentheses_iterator = 0
    while parentheses_iterator < len(equation): # Find all the parentheses.

        if equation[parentheses_iterator] == '(': # If found an open
            # parentheses.
            start_index = parentheses_iterator + 1 # Index of the first
            # parentheses.
            count = 1 # Count checks if the closing parentheses
            # is closing the current open parentheses.
            while count != 0: # Find the closing parentheses
                # of the open parentheses.
                parentheses_iterator = parentheses_iterator + 1
                if equation[parentheses_iterator] == '(': # Increase count by 1
                    # if found open parentheses.
                    count = count + 1
                elif equation[parentheses_iterator] == ')': # Decrease count by
                    # 1 if found closing parentheses.
                    count = count - 1

            # Run this function for the equation found in the parentheses.
            result = calculate(equation[start_index: parentheses_iterator])

            # Check if the result is an illegal number.
            if isinstance(result, complex):
                raise Exception("Can't use complex numbers.")
            elif math.isinf(result):
                raise Exception("Can't use infinite numbers.")
            elif math.isnan(result):
                raise Exception("Can't use NaN.")

            # Pop all the elements of the equation we solved
            # (until the closing parentheses).
            for j in range(parentheses_iterator - start_index + 1):
                equation.pop(start_index)
            equation[start_index - 1] = result # Replace the element that's
            # before start_index with the result (will always be
            # the opening parentheses).
            parentheses_iterator = -1 # Assign -1 to i to start over the search
            # for parentheses (I assign -1 because I add 1 to the iterator
            # right after that).

        parentheses_iterator = parentheses_iterator + 1 # Skip all the elements
        # that are not open parentheses.

    result = _solve_simple_equation(equation) # If not found any parentheses
    # in the equation, run _solve_simple_equation.

    # Check if the result is an illegal number.
    if isinstance(result, complex):
        raise Exception("Can't use complex numbers.")
    elif math.isinf(result):
        raise Exception("Can't use infinite numbers.")
    elif math.isnan(result):
        raise Exception("Can't use NaN.")

    return result


def _solve_simple_equation(equation):
    """
    :param equation: list
    :return: a value that is the answer of the simple equation
    a simple equation is an equation with no parentheses.
    """

    # TODO: solve the simple equation given in the equation list.
    #  Solve via the rules of the levels of the operands.

    if len(equation) == 1: # Stop condition. When there is only 1 operand left.
        return equation[0]

    max_level_operator = '' # Operator with max level in the equation.
    max_level_operator_index = 0 # Index of the max level operator.

    for equation_iterator in range(len(equation)): # Go over the equation.
        if isinstance(equation[equation_iterator], str): # If it's a string
            if max_level_operator == '': # Check if not found an operator yet.
                # Assign the operator.
                max_level_operator = equation[equation_iterator]
                # Assign the index of the operator.
                max_level_operator_index = equation_iterator
            elif o.operator_dic[equation[equation_iterator]] > \
                    o.operator_dic[max_level_operator]:
                # If found an operator already, check if the current one has
                # a higher level.

                # Assign the max level operator.
                max_level_operator = equation[equation_iterator]
                # Assign the index of max level operator.
                max_level_operator_index = equation_iterator

    operator = max_level_operator # Just to make it easier to write.
    index = max_level_operator_index # Just to make it easier to write.

    # Handle operators that should be with two operands.
    if operator in o.two_operands:
        handled = _handle_edge_cases_two_operands(operator, index, equation)
        if handled is True:
            return _solve_simple_equation(equation)
        elif isinstance(handled, float):
            return handled
         # Normal operator
        if equation[index + 1] == '-': # If there is a minus after the
            # operator.
            equation.pop(index + 1)
            equation[index + 1] = -equation[index + 1]

        result = _solve_two_operand(
            equation[index - 1:index + 2]) # Solve an equation with two
        # operands.

        # Edit the list to fit the result in it.
        equation.pop(index) # Erase the operator.
        equation.pop(index) # Erase the second operand.
        equation[index - 1] = result # Replace the first operand with the
        # result.
    elif operator in o.one_operand_after: # Operator with one operand that
        # comes after it.

        # Solve an equation with one operand after.
        result = _solve_one_operand_after(equation[index - 1:index + 1])

        # Edit the list to fit the result in it.
        equation.pop(index) # Erase the operator
        equation[index - 1] = result # Replace the operand with the result.
    elif operator in o.one_operand_before: # Operator with one operand that
        # comes before it.
        result = _solve_one_operand_before(equation[index:index + 2]) # Solve
        # an equation with one operand after.

        # Edit the list to fit the result in it.
        equation.pop(index)  # Erase the operator
        # tilda() function can return None so I handle it here.
        if result is not None:
            equation[index] = result  # Replace the operand with the result.
        else:
            equation.pop(index)  # Erase the second operator

    return _solve_simple_equation(equation)


def _handle_edge_cases_two_operands(operator, index, equation):
    """
    Check edge cases for operators with two operands.
    :param operator: string
    :param index: int
    :param equation: list
    :return: a number of False if not done anything or True if done anything.
    """
    # Handle minuses
    if operator == '-' and index == 0 and len(equation) == 2:
        # If the operator is minus, it's at the start of the equation
        # and the length of the equation is 2
        return -equation[1]
    elif operator == '-' and index == 0 and len(equation) > 2 \
            and o.operator_dic[equation[index + 2]] == \
            o.operator_dic[operator]:
        # If the operator is minus, it's at the start of the equation,
        # the length of the equation is 2 and the operator after has the
        # same level as minus.
        equation.pop(0)
        equation[0] = -equation[0]
        return True

    return False


def _solve_two_operand(equation):
    """
    :param equation: list
    :return: a floating point number that is the result of an
    equation with two operands and one operator.
    :exception: ZeroDivisionError if operand2 is zero and the operator is
    division.
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
        if operand2 == 0:
            raise ZeroDivisionError("Can't divide by zero.")
        return operand1 / operand2
    elif operator == '^':
        return operand1 ** operand2
    elif operator == '%':
        return  operand1 % operand2
    elif operator == '@':
        return  (operand1 + operand2) / 2
    elif operator == '$':
        return  max(operand1, operand2)
    elif operator == '&':
        return min(operand1, operand2)

    return 0 # Just for emergency.


def _solve_one_operand_after(equation):
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
        return _factorial(operand)

    return 0 # Just for emergency.


def _solve_one_operand_before(equation):
    """
    :param equation: list
    :return: a floating point number that is the result of an
    equation with one operand and one operator where the operator is
    before the operand.
    """

    operator = equation[0]  # Always in the first place.
    operand = equation[1]  # Always in the second place.

    if operator == '~':
        return _tilda(operand)

    return 0 # Just for emergency.


def _tilda(operand):
    """
    :param operand: string or float
    :return: None if the operand is a string and -operand if it's a
    float.
    """

    if operand == '-':
        return None
    else:
        return -operand


def _factorial(x):
    """
    :param x: int
    :return: factorial of x.
    :exception: Exception if x is negative or decimal.
    """

    if x < 0:
        raise Exception("Can't factorialize numbers below 0.")
    elif not x.is_integer():
        raise  Exception("Can't factorialize decimal numbers'.")

    factorial_result = 1
    while int(x) > 0:
        factorial_result *= int(x)
        x = x - 1

    return factorial_result
