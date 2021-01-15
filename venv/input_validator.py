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
    pass


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

    count = 0
    for i in str: # Go over the string.
        if i == '(':
            count = count + 1
        elif i == ')':
            count = count - 1

    return count


def check_unnecessary_parentheses(str):
    """
    :param str: string.
    :return: True if there are no unnecessary parentheses and False if there
    are.
    """

    pass


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
    :return: True if the numbers don't have two decimal points and False if
    they do.
    """

    pass
