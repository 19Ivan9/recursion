def reverse(input_str: str) -> str:
    return input_str if input_str == '' else reverse(input_str[1:]) + input_str[0]

if __name__ == '__main__':

    print(reverse("hello"))
    print(reverse("o"))