import time


def fibonacci_gen(max=None):
    n1, n2 = 0, 1
    while True:
        if n2 >= max:
            break
        else:
            yield n2
            n1, n2 = n2, n1+n2


if __name__ == "__main__":
    fibonacci = fibonacci_gen(40)

    for element in fibonacci:
        print(element)
        time.sleep(1)
