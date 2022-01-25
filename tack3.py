
def mult(a: int, n: int) -> int:
    if a < 0 or n < 0:
        raise ValueError('This function works only with postive integers')
    return n if a == 1 else n + mult(a - 1, n)


if __name__ == '__main__':
    print(mult(2, 4))
    print(mult(2, 0))
    print(mult(2, -4))
