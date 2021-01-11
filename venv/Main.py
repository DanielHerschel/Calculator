import EquationSolver
import InputValidator
import InputFormatter


def main():
    #list = InputValidator.string_to_list("5$-6!")
    list = InputFormatter.string_to_list(
       "2&-5!")
    print(list)
    result = EquationSolver.calculate(list)
    print(result)


if __name__ == "__main__":
    main()
