def is_palindrome(string: str) -> bool:
    string = (string.replace(" ", "")).lower()
    return string[::-1] == string


def is_prime(number: int) -> bool:
    return len([x for x in range(1, number + 1) if number % x == 0]) == 2

def main():
    print(is_prime("2"))
    #mypy palindrome.py --ckeck-untyped-defs


if __name__ == "__main__":
    main()