# Legal operands
legal_operands = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'}
# Legal operators
legal_operators = {'+', '-', '*', '/', '^', '~', '%', '!', '@', '$',
                   '&', '(', ')'}
# Legal whitespaces
legal_white_space_set = {' ', '\t', '\n'}


def string_to_list(str):
    """
    :param str: string
    :return: a list of the operators and operands.
    Turns the string into a list of operators and operands.
    """

    op_list = []
    str = str.replace(' ', '').replace('\t', '').replace('\n', '') # Remove all
    # the whitespaces.

    i = 0
    while i < len(str): # Go over the string.

        # If found a number, find the end of it and add it to the list.
        if str[i] in legal_operands:
            start_index = i # Start index of the number.
            while i < len(str): # Find the end index of the number.
                if str[i] in legal_operands:
                    i = i + 1
                else:
                    break
            op_list.append(float(str[start_index:i])) # Append to the list the
            # number that has been found.

        # Insert the operators to the list.
        if i < len(str):
            while i < len(str):
                if str[i] in legal_operators: # If found a legat operator,
                    # add it to the list.
                    op_list.append(str[i])
                    i = i + 1
                else:
                    break

    return op_list


def fix_minuses(list):
    """
    :param list: list
    :return: a list that it's minuses are fixed.
    For example:
    for: [2, '-', '-', 3] will be: [2, '+', 3]
    """

    # Check adjacent minuses
    i = 0
    while i < len(list): # Go over the equation.
        if list[i] == '-': # If found a minus
            start_index = i
            while i < len(list): # Find the index of the last minus in a row.
                if list[i] == '-':
                    i = i + 1
                else:
                    break

            minus_count = i - start_index # Number of minuses in a row.
            if minus_count % 2 == 0: # If the number is even
                # (should be positive).
                for j in range(minus_count - 1): # Pop all the minuses except
                    # the last one.
                    list.pop(start_index)
                if list[start_index-1] == ')' or \
                        isinstance(list[start_index-1], float): # If the minus
                    # is right next to a closing parentheses or a number
                    list[start_index] = '+' # Change the minus to plus.
                else:
                    list.pop(start_index)
                i = start_index - 1 # Offset i to make it where it was before
                # the popping.
            elif minus_count % 2 == 1: # Number of minuses if odd.
                if list[start_index - 1] == '+': # If there is a plus before.
                    for j in range(minus_count): # Pop all the minuses.
                        list.pop(start_index)
                    list[start_index - 1] = '-' # Set minus instead of plus.
                    i = start_index - 1 # Offset i to make it where it was
                    # before the popping.
                else:
                    for j in range(minus_count - 1): # Pop all the minuses
                        # except the last one.
                        list.pop(start_index)
                    i = start_index # Offset i to make it where it was
                    # before the popping.

        i = i + 1
