import operators as o

# Legal operands
legal_operands = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'}


def validate_string(str):
    """
    :param str: string
    :return: True if string is valid, False if not.
    Prints out a message if found an error in the string.
    """

    if len(str) == 0:
        print("Can't solve an empty equation.")
        return False
    elif not check_legal_chars(str):
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
    :return: True if all the chars in the string are legal, False if
    not.
    I don't check for whitespaces because they are deleted before the
    validation.
    """
    global legal_operands

    for i in str: # Go over the string
        if i not in legal_operands and i not in o.legal_operators: # If
            # a char is not legal.
           return False

    return True


def check_parentheses(str):
    """
    :param str: string
    :return: Count of the parentheses. Positive if there are too many
    opening parentheses, negative if there are too many closing ones and
    0 if there are as many opening parentheses as closing ones.
    """

    parentheses_count = 0
    for parentheses_iterator in str: # Go over the string.
        if parentheses_iterator == '(':
            parentheses_count = parentheses_count + 1
        elif parentheses_iterator == ')':
            parentheses_count = parentheses_count - 1

    return parentheses_count


def check_unnecessary_parentheses(str):
    """
    :param str: string.
    :return: True if there are no unnecessary parentheses and False if
    there are.
    """

    str_copy = str # Copy of the string to not break the original.

    parentheses_iterator = 0
    while parentheses_iterator < len(str_copy):  # Find all the
        # parentheses.

        if str_copy[parentheses_iterator] == '(':  # If found an open
            # parentheses.
            start_index = parentheses_iterator  # Index of the first
            # parentheses.
        elif str_copy[parentheses_iterator] == ')': # Found most inside
            # parentheses.
            if start_index == parentheses_iterator - 1: # If the opening
                # parentheses is right next to the closing one.
                return False

            # Delete the parentheses and what's in it.
            str_copy = str_copy[0:start_index] + \
                       str_copy[parentheses_iterator + 1:len(str_copy)]
            parentheses_iterator = -1 # Check again from the start

        parentheses_iterator = parentheses_iterator + 1  # Skip all the
        # elements that are not open parentheses.

    return True



def check_operators(str):
    """
    :param str: string
    :return: True if all the operators in the string are correctly used
    and False if not.
    Also prints out a message if an operator is not used correctly.
    """

    for string_iterator in range(len(str)): # Go over the string
        if str[string_iterator] in o.two_operands_no_minus: # If
            # operator found is with two operands.
            if string_iterator > 0:
                if not str[string_iterator - 1].isdigit() and \
                        str[string_iterator - 1] != ')':
                    # If the place before the operator is not a digit or
                    # it's not a closing parentheses.
                    print("There is no number before the operator:",
                          str[string_iterator])
                    return False
            else:
                print("There is no number before the operator:",
                      str[string_iterator])
                return False
            if string_iterator < len(str) - 1:
                if not str[string_iterator + 1].isdigit() and \
                        str[string_iterator + 1] != '-' and \
                        str[string_iterator + 1] != '~':  # If the place
                    # after the operator is not a digit oe a minus
                    if str[
                        string_iterator + 1] != '(':  # If the place
                        # after the operator is not an opening
                        # parentheses.
                        print("There is no number after the operator:",
                              str[string_iterator])
                        return False
            else:
                print("There is no number after the operator:",
                      str[string_iterator])
                return False
        elif str[string_iterator] in o.one_operand_after: # If operator
            # found is with one operand that come after it.
            if string_iterator > 0:
                if not str[string_iterator - 1].isdigit() and \
                        str[string_iterator - 1] != ')' and \
                        str[string_iterator - 1] not in o.one_operand_after:
                        # If the place
                    # before the operator is not a digit or it's not a
                    # closing parentheses.
                    print("There is no number before the operator:",
                          str[string_iterator])
                    return False
            else:
                print("There is no number before the operator:",
                      str[string_iterator])
                return False

            if string_iterator < len(str) - 1:
                if string_iterator < len(str) - 1:
                    if str[string_iterator + 1].isdigit() and \
                            str[string_iterator + 1] == '(':  # If the
                        # place after the operator is a digit or an
                        # opening parentheses.
                        print("There is no operator after the operator:",
                              str[string_iterator])
                        return False
        elif str[string_iterator] in o.one_operand_before: # If operator
            # found is with one operand that come before it.
            if string_iterator > 0:
                if str[string_iterator - 1].isdigit() or \
                        str[string_iterator - 1] == ')': # If the place
                    # before the operator is a digit or it's a
                    # closing parentheses.
                    print("There is no operator before the operator:",
                        str[string_iterator])
                    return False

            if string_iterator < len(str) - 1:
                if not str[string_iterator + 1].isdigit() and \
                        not str[string_iterator + 1] == '(':  # If
                    # the place after the operator is a digit or an
                    # opening parentheses.
                    if str[string_iterator] != '~':  # Exclusions.
                        print(
                            "There is no number or minus after the operator:",
                            str[string_iterator])
                        return False
            else:
                print(
                    "There is no number or minus after the operator:",
                    str[string_iterator])
                return False

    return True


def check_numbers(str):
    """
    :param str: string
    :return: True if the numbers don't have two decimal points or if the
    decimal points are used correctly and False otherwise and if the
    number has an operator where it needs to be.
    """

    string_iterator = 0
    while string_iterator < len(str):
        if str[string_iterator] in legal_operands: # Start of a number.
            start_index = string_iterator # Start index of the number.
            decimal_flag = False # Flag if found a decimal point in a
            # number.
            while string_iterator < len(str): # Find the end index of
                # the number.
                if str[string_iterator].isdigit(): # If found a digit.
                    if string_iterator > 0:
                        if str[string_iterator - 1] == ')': # If there
                            # is a closing parentheses before the digit.
                            print("There is no operator between the number and"
                                  " closing parentheses.")
                            return False
                    elif string_iterator < len(str) - 1:
                        if str[string_iterator + 1] == '(': # If there
                            # is an opening parentheses after the digit.
                            print("There is no operator between the number and"
                                  " the opening parentheses.")
                            return False
                    string_iterator += 1
                elif str[string_iterator] == '.': # If found a decimal
                    # point.
                    if not decimal_flag: # If not found one already.
                        decimal_flag = True
                    else: # If found one in this number already.
                        print("There are two decimal points for one number.")
                        return False

                    if string_iterator < len(str) - 1:
                        if not str[string_iterator + 1].isdigit():
                            # If the decimal point doen't have a digit
                            # before or after it.
                            print("Decimal point not used correctly. "
                                "Missing digits after it.")
                            return False
                    else:
                        print("Decimal point not used correctly. "
                              "Missing digits after it.")
                        return False

                    if string_iterator > 0:
                        if not str[string_iterator - 1].isdigit(): # If
                            # The place before the digit is not a digit.
                            print("Decimal point not used correctly. "
                                  "Missing digits before it.")
                            return False
                    else:
                        print("Decimal point not used correctly. "
                              "Missing digits before it.")
                        return False

                    string_iterator += 1
                else: # End of number
                    break

        string_iterator += 1

    return True