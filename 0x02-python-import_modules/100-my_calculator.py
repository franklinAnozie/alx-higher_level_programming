#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit

    operator = ['+', '-', '*', '/']

    nargs = len(argv) - 1
    if nargs != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    op = argv[2]
    if op not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    from calculator_1 import add, sub, mul, div
    a = int(argv[1])
    b = int(argv[3])

    if op == '+':
        print("{} {} {} = {}".format(a, op, b, add(a, b)))
    elif op == '-':
        print("{} {} {} = {}".format(a, op, b, sub(a, b)))
    elif op == '*':
        print("{} {} {} = {}".format(a, op, b, mul(a, b)))
    else:
        print("{} {} {} = {}".format(a, op, b, div(a, b)))
