# Legal operands
legal_operands = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'}
# Legal operators
legal_operators = {'+', '-', '*', '/', '^', '~', '%', 'x', '@', '$', '&', '(', ')'}
# Legal whitespaces
legal_white_space_set = {' ', '\t', '\n'}


def string_to_list(str):
    """
    :param str:
    :return: a list of the operators and operands.
    Turns the string into a list of operators and operands.
    """

    op_list = []
    str = str.replace(' ', '').replace('\t', '').replace('\n', '') # Remove all the whitespaces.

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
            op_list.append(float(str[start_index:i])) # Append to the list the number that has been found.

        # Insert the operators to the list.
        if i < len(str):
            while i < len(str):
                if str[i] in legal_operators: # If found a legat operator, add it to the list.
                    op_list.append(str[i])
                    i = i + 1
                else:
                    break

    return op_list
