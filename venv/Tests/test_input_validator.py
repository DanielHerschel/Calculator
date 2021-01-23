from input_validator import *
from input_formatter import *


def test_syntax():
    """
    Test the check_legal_chars() function.
    """

    # Setup
    valid_str = "(5+-6!)+-5"
    invalid_strings = ["(---s5-+f..dfasdf-6!)+-5",
                       "dsl;kajf940hhasd;ljfnas",
                       "",
                       "2*^3",
                       "        \t\n ",
                       "-2~"]

    # Test
    result_of_valid_test = validate_string(valid_str)
    results_of_invalid_test = [validate_string(str) for str in invalid_strings]

    # Assert
    assert result_of_valid_test == True
    for invalid_result in results_of_invalid_test:
        assert invalid_result == False


def test_check_operators():
    """
    Test the check_operators() function.
    """

    # Setup
    valid_str = "(5+~~~~-~~6!)+-5"
    invalid_str = "(-~~~-+-5-6!)+-5~"

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


def test_check_unnecessary_parentheses():
    """
    Test the check_unnecessary_parentheses() function.
    """

    # Setup
    valid_str = "(5+-6!)+-5"
    unnecessary_str = "!((-~--5-6!))+-5"

    # Test
    result_of_valid_test = check_unnecessary_parentheses(valid_str)
    result_of_unnecessary_test = check_unnecessary_parentheses(
        unnecessary_str)

    # Assert
    assert result_of_valid_test == True
    assert result_of_unnecessary_test == False


def test_check_numbers():
    """
    Test the check_numbers() function.
    """

    # Setup
    valid_str = "(5+-6!)+-5"
    invalid_decimal_str = "(5+-6!)+-5."
    invalid_two_decimal_str = "(5+-6.7.7!)+-5"

    # Test
    result_of_valid_test = check_numbers(valid_str)
    result_of_invalid_decimal_test = check_numbers(invalid_decimal_str)
    result_of_invalid_two_decimal_test = check_numbers(invalid_two_decimal_str)

    # Assert
    assert result_of_valid_test == True
    assert result_of_invalid_decimal_test == False
    assert result_of_invalid_two_decimal_test == False
