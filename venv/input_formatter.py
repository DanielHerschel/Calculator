import operators as o

# Legal operands
legal_operands = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'}
# Legal whitespaces
legal_white_spaces = {' ', '\t', '\n'}

def delete_whitespaces(str):
    """
    Deletes all the whitespaces in the string.
    :param str: string
    :return: A string if replaced the whitespaces and None if there was an
    exception.
    :exception: Exception if could not replace the whitespaces.
    """
    global legal_white_spaces

    try:
        str_copy = str
        for i in legal_white_spaces:
            str_copy = str_copy.replace(i, '')
        return str_copy
    except Exception as e:
        print(e)
        return None


def string_to_list(str):
    """
    Turns the string into a list of operators and operands.
    :param str: string
    :return: a list of the operators and operands.
    """
    global legal_operands

    op_list = []
    string_iterator = 0
    while string_iterator < len(str): # Go over the string.

        # If found a number, find the end of it and add it to the list.
        if str[string_iterator] in legal_operands:
            start_index = string_iterator # Start index of the number.
            while string_iterator < len(str): # Find the end index of the
                # number.
                if str[string_iterator] in legal_operands:
                    string_iterator = string_iterator + 1
                else:
                    break
            op_list.append(float(str[start_index:string_iterator])) # Append to
            # the list the number that has been found.

        # Insert the operators to the list.
        if string_iterator < len(str):
            while string_iterator < len(str):
                if str[string_iterator] in o.legal_operators: # If found a
                    # legal operator, add it to the list.
                    op_list.append(str[string_iterator])
                    string_iterator = string_iterator + 1
                else:
                    break

    return op_list


def fix_operators(list):
    """
    :param list: list
    :return: a list that it's operators are fixes (minus and tilda for example)
    """

    while not _check_fixed_operators(list):
        _fix_tildas(list)
        _fix_minuses(list)


def _check_fixed_operators(list):
    """
    :param list: list, operators_to_check: list
    :return: check if the operators are fixed.
    """

    list_iterator = 0
    while list_iterator < len(list) - 1:  # Go over the equation.
        if list[list_iterator] in o.operators_to_fix and \
                list[list_iterator + 1] == list[list_iterator]:
            # If found an operator and found the same operator next to it.
            return False
        list_iterator = list_iterator + 1

    return True


def _fix_minuses(list):
    """
    :param list: list
    :return: a list that it's minuses are fixed.
    For example:
    for: [2, '-', '-', 3] will be: [2, '+', 3]
    """

    # Check adjacent minuses
    list_iterator = 0
    while list_iterator < len(list): # Go over the equation.
        if list[list_iterator] == '-': # If found a minus
            start_index = list_iterator
            while list_iterator < len(list): # Find the index of the last minus
                # in a row.
                if list[list_iterator] == '-':
                    list_iterator = list_iterator + 1
                else:
                    break

            minus_count = list_iterator - start_index # Number of minuses in a
            # row.
            if minus_count % 2 == 0: # If the number is even
                # (should be positive).
                for j in range(minus_count - 1): # Pop all the minuses except
                    # the last one.
                    list.pop(start_index)
                if (list[start_index-1] == ')' or \
                        isinstance(list[start_index-1], float)) and \
                        start_index > 0: # If the minus
                    # is right next to a closing parentheses or a number
                    # and if it's not at the start of the equation.
                    list[start_index] = '+' # Change the minus to plus.
                else:
                    list.pop(start_index)
                list_iterator = start_index - 1 # Offset i to make it where it
                # was before the popping.
            elif minus_count % 2 == 1: # Number of minuses if odd.
                if list[start_index - 1] == '+': # If there is a plus before.
                    for j in range(minus_count): # Pop all the minuses.
                        list.pop(start_index)
                    list[start_index - 1] = '-' # Set minus instead of plus.
                    list_iterator = start_index - 1 # Offset i to make it where
                    # it was before the popping.
                else:
                    for j in range(minus_count - 1): # Pop all the minuses
                        # except the last one.
                        list.pop(start_index)
                    list_iterator = start_index # Offset i to make it where it
                    # was before the popping.

        list_iterator = list_iterator + 1


def _fix_tildas(list):
    """
    :param list: list
    :return: a list that it's tildas are fixed.
    For example:
    for: [2, '-', '~', '~', 3] will be: [2, '-', 3]
    """

    # Check adjacent tildas
    list_iterator = 0
    while list_iterator < len(list): # Go over the equation.
        if list[list_iterator] == '~': # If found a tilda.
            start_index = list_iterator
            while list_iterator < len(list): # Find the index of the last tilda
                # in a row.
                if list[list_iterator] == '~':
                    list_iterator = list_iterator + 1
                else:
                    break

            tilda_count = list_iterator - start_index # Number of tildas in a
            # row.
            if tilda_count % 2 == 0: # If the number is even.
                for j in range(tilda_count): # Pop all the tildas except
                    # the last one.
                    list.pop(start_index)
                list_iterator = start_index - 1 # Offset the iteraor to make it
                # where it was before the popping.
            elif tilda_count % 2 == 1: # Number of tildas if odd.
                for j in range(tilda_count - 1): # Pop all the minuses
                    # except the last one.
                    list.pop(start_index)
                list_iterator = start_index # Offset i to make it where it
                # was before the popping.

        list_iterator = list_iterator + 1
