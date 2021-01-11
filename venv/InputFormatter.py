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

    fix_minuses(op_list)

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
    while i < len(list):
        if list[i] == '-':
            start_index = i
            while i < len(list):
                if list[i] == '-':
                    i = i + 1
                else:
                    break

            minus_count = i - start_index
            if minus_count % 2 == 0:
                for j in range(minus_count - 1):
                    list.pop(start_index)
                if (list[start_index-1] == ')' or \
                        isinstance(list[start_index-1], float)) and \
                        start_index != 0:
                    list[start_index] = '+'
                else:
                    list.pop(start_index)
                i = start_index - 1
            elif minus_count % 2 == 1 and list[start_index - 1] == '+':
                for j in range(minus_count):
                    list.pop(start_index)
                list[start_index - 1] = '-'
                i = start_index - 1
            elif minus_count % 2 == 1 and list[start_index - 1] != '+':
                for j in range(minus_count - 1):
                    list.pop(start_index)
                i = start_index

        i = i + 1

