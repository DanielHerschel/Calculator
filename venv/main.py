import equation_solver
import input_validator
import input_formatter


def main():
    list = input_formatter.string_to_list("24%12^2-7*9&(2+3-4+6$22--8--~((9+8)!))")
    input_formatter.fix_minuses(list)
    print(list)
    result = equation_solver.calculate(list)
    print(result)


if __name__ == "__main__":
    main()
