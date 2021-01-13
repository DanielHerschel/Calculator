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
