from typing import Union

def to_power(x: Union[int, float], exp: int) -> Union[int, float]:
    if exp < 0:
        raise ValueError(' This function works only with exp > 0 ')
    return 1 if exp == 0 else x * to_power(x, exp - 1)

if __name__ == '__main__':
    print(to_power(2, 3))
    print(to_power(3.5, 2))
    # print(to_power(2,-1))
