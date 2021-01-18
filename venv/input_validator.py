# Legal operands
legal_operands = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'}
# Legal operators
legal_operators = {'+', '-', '*', '/', '^', '~', '%', '!', '@', '$',
                   '&', '(', ')'}
# Legal whitespaces
legal_white_spaces = {' ', '\t', '\n'}


def validate_string(str):
    """
    :param str: string
    :return: True if string is valid, False if not.
    Prints out a message if found an error in the string.
    """

    if not check_legal_chars(str):
        print("Illegal characters are used.")
        return False
    elif check_parentheses(str) > 0:
        print("There are too many opening parentheses.")
        return False
    elif check_parentheses(str) < 0:
        print("There are too many closing parentheses.")
        return False
    elif not check_unnecessary_parentheses(str):
        print("There are unnecessary parentheses.")
        return False
    elif not check_numbers(str):
        return False
    elif not check_operators(str):
        return False

    return True


def check_legal_chars(str):
    """
    :param str: string
    :return: True if all the chars in the string are legal, False if not.
    """
    global legal_operators, legal_operands, legal_white_spaces

    for i in str: # Go over the string
        if i not in legal_operands and i not in legal_operators \
            and i not in legal_white_spaces: # If a char is not legal.
           return False

    return True


def check_parentheses(str):
    """
    :param str: string
    :return: Count of the parentheses. Positive if there are too many opening
    parentheses, negative if there are too many closing ones and 0 if
    there are as many opening parentheses as closing ones.
    """

    parentheses_count = 0
    for i in str: # Go over the string.
        if i == '(':
            parentheses_count = parentheses_count + 1
        elif i == ')':
            parentheses_count = parentheses_count - 1

    return parentheses_count


def check_unnecessary_parentheses(str):
    """
    :param str: string.
    :return: True if there are no unnecessary parentheses and False if there
    are.
    """

    # TODO: implement this method.

    return True


def check_operators(str):
    """
    :param str: string
    :return: True if all the operators in the string are correctly used and
    False if not.
    Also prints out a message if an operator is not used correctly.
    """

    # Operators with two operands with no minus.
    two_operands_no_minus = {'+', '*', '/', '^', '%', '@', '$', '&'}
    # Operators with one operand.
    one_operand = {'!', '~'}

    for i in range(len(str)): # Go over the string
        if str[i] in two_operands_no_minus: # If operator found is with two
            # operands.
            if not str[i - 1].isdigit() and str[i - 1] != ')':
                # If the place before the operator is not a digit or it's
                # not a closing parentheses.
                print("There is no number before the operator:", str[i])
                return False
            elif not str[i + 1].isdigit() and str[i + 1] != '-': # If the place
                # after the operator is not a digit oe a minus
                if str[i + 1] != '(': # If the place after the operator is
                    # not an opening parentheses.
                    print("There is no number after the operator:", str[i])
                    return False
        elif str[i] in one_operand: # If operator found is with one operand.
            if not str[i - 1].isdigit() and str[i - 1] != ')': # If the place
                # before the operator is not a digit or it's not a closing
                # parentheses.
                print("There is no number before the operator:", str[i])
                return False
            elif str[i + 1].isdigit() and str[i + 1] == '(': # If the place
                # after the operator is a digit or an opening parentheses.
                print("There is no operator after the operator:", str[i])
                return False

    return True


def check_numbers(str):
    """
    :param str: string
    :return: True if the numbers don't have two decimal points or if the
    decimal points are used correctly and False otherwise.
    """

    i = 0
    while i < len(str):
        if str[i] in legal_operands: # Start of a number.
            start_index = i # Start index of the number.
            decimal_flag = False # Flag if found a decimal point in a number.
            while i < len(str): # Find the end index of the number.
                if str[i].isdigit(): # Skip on the digits.
                    i = i + 1
                elif str[i] == '.': # If found a decimal point.
                    if not decimal_flag: # If not found one already.
                        decimal_flag = True
                    else: # If found one in this number already.
                        print("There are two decimal points for one number.")
                        return False

                    if not str[i - 1].isdigit() or not str[i + 1].isdigit():
                        # If the decimal point doen't have a digit before or
                        # after it.
                        print("Decimal point not used correctly. "
                              "Missing digits.")
                        return False

                    i = i + 1
                else: # End of number
                    break

        i = i + 1

    return True