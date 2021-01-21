import equation_solver
import input_validator
import input_formatter


def main():
    str = ""
    input_validator.validate_string(str)
    list = handle_input_from_user(str)
    print(list)
    result = equation_solver.calculate(list)
    print(result)


def get_input_from_user():
    """
    :return: a string that was inputted from the useror None if could not get
    an input from the user.
    """
    try:
        user_input = str(input())
        return user_input
    except Exception as e:
        print(e)
        return None


def handle_input_from_user(str):
    """
    Handles the string input from the user.
    :param str: string
    :return: A list if handled the string and None if not.
    """

    try:
        list = input_formatter.string_to_list(
            input_formatter.delete_whitespaces(str))
        input_formatter.fix_operators(list)
        return list
    except Exception as e:
        print(e)
        return None


if __name__ == "__main__":
    main()
