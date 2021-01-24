from ..input_formatter import *


def test_delete_whitespaces():
    """
    Test the delete_whitespaces() function.
    """

    # Setup
    string_with_whitespaces = "(    5\t+ -6!\n)+          - 5"

    # Test
    deleted_whitespaces = delete_whitespaces(string_with_whitespaces)

    # Assert
    assert deleted_whitespaces == "(5+-6!)+-5"


def test_string_to_list():
    """
    Test the string_to_list() function.
    """

    # Setup
    string_to_transform = "(5+-6!)-5"

    # Test
    list_from_string = string_to_list(string_to_transform)

    # Assert
    assert list_from_string == ['(', 5.0, '+', '-', 6.0, '!', ')', '-', 5.0]


def test_fix_operators_1():
    """
    Test the _fix_operators() function. Part 1.
    """

    # Setup
    # Test when there is a plus before a minus sequence.
    plus_before_odd_minus = string_to_list("5+---6")
    plus_before_even_minus = string_to_list("5+--6")
    # Test when there is no operator before a minus sequence.
    odd_minuses_no_operator = string_to_list("5-----6")
    even_minuses_no_operator = string_to_list("5----6")

    # Test
    fix_operators(plus_before_odd_minus)
    fix_operators(plus_before_even_minus)

    fix_operators(odd_minuses_no_operator)
    fix_operators(even_minuses_no_operator)

    # Assert
    assert plus_before_odd_minus == [5.0, '-', 6.0]
    assert plus_before_even_minus == [5.0, '+', 6.0]

    assert odd_minuses_no_operator == [5.0, '-', 6.0]
    assert even_minuses_no_operator == [5.0, '+', 6.0]


def test_fix_operators_2():
    """
    Test the _fix_operators() function. Part 2.
    """

    # Setup
    # Test when there is an operator (not '+') before a minus sequence.
    operator_before_odd_minus = string_to_list("5%---6")
    operator_before_even_minus = string_to_list("5%--6")
    # Test when there is a minus sequence at the start of the equation.
    odd_minuses_start_equation = string_to_list("---5")
    even_minuses_start_equation = string_to_list("--5")

    # Test
    fix_operators(operator_before_odd_minus)
    fix_operators(operator_before_even_minus)

    fix_operators(odd_minuses_start_equation)
    fix_operators(even_minuses_start_equation)

    # Assert
    assert operator_before_odd_minus == [5.0, '%', '-', 6.0]
    assert operator_before_even_minus == [5.0, '%', 6.0]

    assert odd_minuses_start_equation == ['-', 5.0]
    assert even_minuses_start_equation == [5.0]


def test_fix_operators_3():
    """
    Test the _fix_operators() function. Part 3.
    """

    # Setup
    # Test when there is a minus sequence next to an opening
    # parentheses.
    open_parentheses_odd_minus = string_to_list("(---5+6)/2")
    open_parentheses_even_minus = string_to_list("(--5+6)/2")
    # Test when there is a minus sequence next to an closing
    # parentheses.
    close_parentheses_odd_minus = string_to_list("(5+6)---2")
    close_parentheses_even_minus = string_to_list("(5+6)--2")

    # Test
    fix_operators(open_parentheses_odd_minus)
    fix_operators(open_parentheses_even_minus)

    fix_operators(close_parentheses_odd_minus)
    fix_operators(close_parentheses_even_minus)

    # Assert
    assert open_parentheses_odd_minus == ['(', '-', 5.0, '+', 6.0, ')',
                                          '/', 2.0]
    assert open_parentheses_even_minus == ['(', 5.0, '+', 6.0, ')',
                                           '/', 2.0]

    assert close_parentheses_odd_minus == ['(', 5.0, '+', 6.0, ')',
                                           '-', 2.0]
    assert close_parentheses_even_minus == ['(', 5.0, '+', 6.0, ')',
                                            '+', 2.0]
