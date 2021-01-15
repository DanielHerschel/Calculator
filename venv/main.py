import equation_solver
import input_validator
import input_formatter


def main():
    list = "(-(700%64)!~)"
    input_formatter.delete_whitespaces(list)
    list = input_formatter.string_to_list(list)
    input_formatter.fix_minuses(list)
    print(list)
    result = equation_solver.calculate(list)
    print(result)


if __name__ == "__main__":
    main()
