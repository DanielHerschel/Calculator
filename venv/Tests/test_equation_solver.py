from equation_solver import *
from input_formatter import string_to_list, delete_whitespaces, fix_operators


def test_easy_equations():
    """
    Test 15 easy equations.
    """

    # Setup
    string_equations = ["2+3", "3-6", "220*5.4", "10.6/8.9", "2^2.5",
                        "~5.8", "-~5", "~-6", "5%7.5", "8!",
                        "7@5.3", "6.1$8.99", "8.99&9.001", "2+7/-8", "-2$7-5"]
    list_equaions = [string_to_list(str) for str in string_equations]
    answers = [5.0, -3.0, 1188, 1.1910112359550562, 5.656854249492381,
               -5.8, 5.0, 6.0, 5.0, 40320,
               6.15, 8.99, 8.99, 1.125, -12.0]

    # Test
    calculate_answers = [calculate(list) for list in list_equaions]

    # Assert
    for answer_iterator in range(len(answers)):
        assert calculate_answers[answer_iterator] == answers[answer_iterator]


def test_complex_equations():
    """
    Test 20 complex equations.
    """

    # Setup
    string_equations = ["24%12^2-7*9&(2+3-4+6$22--8--~9+8!)",
                        "----(8--8)$5+2%456+99*~(6+6)+2^(-(1+1))",
                        "((1+1)!^2)*5$6+(21&-(1+4)^3)",
                        "18-6^2+5%4$3+2+4+5+6-------9+7&5/3.2%4.2",
                        "0!+-1*2/3^4%5&6$7@     ~8",
                        "(1+2)^((-1+~2)*-1)!+(3-1)!",
                        "~((88/23*2.2)^3&(5!+-  --6^3))",
                        "14$5%2&4+4+4-7.7+(5*  3$2)!",
                        "005* 2^2&2-7&88+224@\t26-(43-44+66&2--- -45*(321&2))",
                        "----~4+67 * 2-4522/221+(2&23 * 22%3^2)-7*2@4",
                        "87^3%2&66@45%\n((22%4$2^2)+7*6!)^~2 *6",
                        "24%12^2-7*9&(2+3-4+6$22--8--~((9+8)!))",
                        "7&8*22^3!-7^3+((22%2 * 7)+3$5^3&~7)",
                        "24%12^2-7*9&(2+3-4+6$22--8--~((9+8)!))",
                        "~~~----~-~---~--~~~~~----~-~-~2323",
                        "(123 @ ((145*2/4%6-6/7) @ ~(3^5 - 9000)))",
                        "87^3  %2&66@4   *~5%((22%4$2^2)+7 *6!)^2 *6",
                        "24%12^2-7*9&(2+3-4+6$22--8--~((9+8)!))",
                        "5!-52&5*2-((2 *2)+45^5+~2+2)",
                        "87^3%2&66@45%((22%4$2^2)+7*6!)^~2 *6"]
    list_equstions = [string_to_list(delete_whitespaces(str))
                      for str in string_equations]
    for list in list_equstions:
        fix_operators(list)
    answers = [-63, -1169.75, -101.0, -7.4375, -1.0, 731.0,
               -1.5239066784713154e-89, 1307674368000.3, 47.0,
               90.53846153846155, 1.3836802264343499e-11, 2489811996671783.0,
               793658985.0000128, 2489811996671783.0, 2323, 2268.660714285714,
               152349126.0, 2489811996671783.0, -184528019.0,
               1.3836802264343499e-11]

    # Test
    equation_answers = []
    for list in list_equstions:
        equation_answers.append(calculate(list))

    # Assert
    for answer_iterator in range(len(answers)):
        assert equation_answers[answer_iterator] == answers[answer_iterator]


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
    Test the calculate() function for factorialization of negative
    numbers.
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
    Test the calculate() function for factorialization of negative
    numbers.
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
