import EquationSolver
import InputValidator
import InputFormatter


def main():
    list = InputFormatter.string_to_list(
       "(-(700%64)!~)")
    InputFormatter.fix_minuses(list)
    print(list)
    result = EquationSolver.calculate(list)
    print(result)


if __name__ == "__main__":
    main()
