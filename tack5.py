def sum_of_digits(digit_string: str) -> int:
    try:
        digit = int(digit_string)
        return 0 if digit_string == 0 else digit% 10 + sum_of_digits(digit/10)
    except ValueError:
        msg = 'input string must be digit string'
        return msg

if __name__ == '__main__':
    print(sum_of_digits('26'))
    print(sum_of_digits('test'))