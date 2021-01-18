from input_validator import *


def test_check_operators():
    """
    Test the check_operators() function.
    """

    # Setup
    valid_str = "(5+-6!)+-5"
    invalid_str = "!(---5-+-6!)+-5"

    # Test
    result_of_valid_test = check_operators(valid_str)
    result_of_invalid_test = check_operators(invalid_str)

    # Assert
    assert result_of_valid_test == True
    assert result_of_invalid_test == False


def test_check_parentheses():
    """
    Test the check_parentheses() function.
    """

    # Setup
    valid_str = "(5+-6!)+-5"
    too_many_opening_str = "!((---5-+-6!)+-5"
    too_many_closing_str = "!(---5-+-6!))+-5"

    # Test
    result_of_valid_test = check_parentheses(valid_str)
    result_of_too_many_opening_test = check_parentheses(too_many_opening_str)
    result_of_too_many_closing_test = check_parentheses(too_many_closing_str)

    # Assert
    assert result_of_valid_test == 0
    assert result_of_too_many_opening_test > 0
    assert result_of_too_many_closing_test < 0


def test_check_legal_chars():
    """
    Test the check_legal_chars() function.
    """

    # Setup
    valid_str = "(5+-6!)+-5"
    invalid_str = "(---s5-+f..dfasdf-6!)+-5"

    # Test
    result_of_valid_test = check_operators(valid_str)
    result_of_invalid_test = check_operators(invalid_str)

    # Assert
    assert result_of_valid_test == True
    assert result_of_invalid_test == False


def test_check_numbers():
    """
    Test the check_numbers() function.
    """

    # Setup
    valid_str = "(5+-6!)+-5"
    invalid_decimal_str = "(5.+-6!)+-5"
    invalid_two_decimal_str = "(5+-6.7.7!)+-5"

    # Test
    result_of_valid_test = check_numbers(valid_str)
    result_of_invalid_decimal_test = check_numbers(invalid_decimal_str)
    result_of_invalid_two_decimal_test = check_numbers(invalid_two_decimal_str)

    # Assert
    assert result_of_valid_test == True
    assert result_of_invalid_decimal_test == False
    assert result_of_invalid_two_decimal_test == False
