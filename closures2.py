def make_repeater_of(n: int):

    def repeater(string: str):
        assert type(string) == str, "Debes enviar texto!"
        return string * n

    return repeater


def make_divisor_by(n: int):

    def divisor(integer: int):
        return integer / n

    return divisor
    

def main():
    repeat_by_3 = make_repeater_of(3)
    print(repeat_by_3("Hola"))
    divide_by_5 = make_divisor_by(5)
    print(divide_by_5(80))



if __name__ == "__main__":
    main()