"""
    ____     _            _       _
  / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __
 | |   / _` | |/ __| | | | |/ _` | __/ _ \| '__|
 | |__| (_| | | (__| |_| | | (_| | || (_) | |
  \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|
              by Daniel Herschel
                 January 2021
"""

import equation_solver
import input_validator
import input_formatter


def main():

    print(" ▄████████    ▄████████  ▄█        ▄████████ ███    █▄   ▄█        "
          "  ▄████████     ███      ▄██████▄     ▄████████ \n"
            "███    ███   ███    ███ ███       ███    ███ ███    ███ ███      "
          "   ███    ███ ▀█████████▄ ███    ███   ███    ███ \n"
            "███    █▀    ███    ███ ███       ███    █▀  ███    ███ ███      "
          "   ███    ███    ▀███▀▀██ ███    ███   ███    ███ \n"
            "███          ███    ███ ███       ███        ███    ███ ███      "
          "   ███    ███     ███   ▀ ███    ███  ▄███▄▄▄▄██▀ \n"
            "███        ▀███████████ ███       ███        ███    ███ ███      "
          " ▀███████████     ███     ███    ███ ▀▀███▀▀▀▀▀   \n"
            "███    █▄    ███    ███ ███       ███    █▄  ███    ███ ███      "
          "   ███    ███     ███     ███    ███ ▀███████████ \n"
            "███    ███   ███    ███ ███▌    ▄ ███    ███ ███    ███ ███▌    ▄"
          "   ███    ███     ███     ███    ███   ███    ███ \n"
            "████████▀    ███    █▀  █████▄▄██ ████████▀  ████████▀  █████▄▄██"
          "   ███    █▀     ▄████▀    ▀██████▀    ███    ███ \n"
          "                                              by Daniel Herschel \n"
              "                                                 January 2021")

    while True:
        print("Enter an equation (X to exit): ")
        user_input = get_input_from_user() # Get input from the user.
        if user_input is not None: # If the input is not None.
            if user_input.lower() == 'x': # If the input is 'x' then close the
                # program.
                break

            deleted_whitespaces = input_formatter.delete_whitespaces(
                user_input) # Delete the whitespaces of the string.

            if deleted_whitespaces is not None: # If removed the whitepaces
                # successfully.
                validate_flag = False # Validation flag.
                try:
                    validate_flag = input_validator.validate_string(
                        deleted_whitespaces) # Validate the input.
                except Exception as e:
                    print(e)
                    validate_flag = False

                if validate_flag: # If the string is valid.
                    equation = handle_input_from_user(deleted_whitespaces)
                    # Handle the string to make it an equation.
                    if equation is not None: # If successfully handled the
                        # string.
                        try:
                            result = equation_solver.calculate(equation) # Try
                            # to calculate the equation.
                            print(result)
                        except RecursionError as re: # If crashed because or
                            x# max depth recursion.
                            print(re)
                        except Exception as e:
                            print(e)
                    else: # If handled the string unsuccessfully.
                        print("Could not handle the equation. "
                              "Please try again.")
                else: # If the string is invalid or did not validate
                    # successfully.
                    print("Invalid input. Please try again.")
            else: # If could not delete the whitespaces.
                print("Could not delete whitespaces. Please try again.")
        else: # If could not get the input.
            print("Could not get input. Please try again.")

    print("Goodbye :)")


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
        list = input_formatter.string_to_list(str)
        input_formatter.fix_operators(list)
        return list
    except Exception as e:
        print(e)
        return None


if __name__ == "__main__":
    main()
