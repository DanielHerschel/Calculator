import EquationSolver
import InputValidator


def main():
    list = InputValidator.string_to_list("(23.5 + 55) & (75 - (3 * 6))")
    print(list)
    result = EquationSolver.solve_equation(list)
    print(result)


if __name__ == "__main__":
    main()
