#!/usr/bin/python3
def print_last_digit(number):
    last_digit = 0
    if number < 0:
        number = -1 * number
    last_digit = number % 10
    if number < 0:
        last_digit = -1 * last_digit
    print(last_digit, end='')
    return (last_digit)
