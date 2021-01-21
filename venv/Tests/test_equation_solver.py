from equation_solver import *
from input_formatter import string_to_list


def test_stack_overflow():
    """
    Test the calculate() function for stack overflow.
    """

    # Setup
    with open("three_plus_three_stack_overflow") as threes_file:
        equation_str = threes_file.read().replace('\n', '')
    equation = string_to_list(equation_str)

    # Test
    stack_overflow_flag = False
    try:
        answer = calculate(equation)
    except RecursionError as e:
        print(e)
        stack_overflow_flag = True

    # Assert
    assert stack_overflow_flag


def test_divide_by_zero():
    """
    Test the calculate() function for zero division.
    """

    # Setup
    equation_str = "3+5/(2-2)"
    equation = string_to_list(equation_str)

    # Test
    zero_division_flag = False
    try:
        answer = calculate(equation)
    except ZeroDivisionError as e:
        print(e)
        zero_division_flag = True

    # Assert
    assert zero_division_flag


def test_negative_factorial():
    """
    Test the calculate() function for factorialization of negative numbers.
    """

    # Setup
    equation_str = "(-5)!"
    equation = string_to_list(equation_str)

    # Test
    negative_factorial_flag = False
    try:
        answer = calculate(equation)
    except Exception as e:
        print(e)
        negative_factorial_flag = True

    # Assert
    assert negative_factorial_flag


def test_decimal_factorial():
    """
    Test the calculate() function for factorialization of negative numbers.
    """

    # Setup
    equation_str = "5.5!"
    equation = string_to_list(equation_str)

    # Test
    decimal_factorial_flag = False
    try:
        answer = calculate(equation)
    except Exception as e:
        print(e)
        decimal_factorial_flag = True

    # Assert
    assert decimal_factorial_flag
