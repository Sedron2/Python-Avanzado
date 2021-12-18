from datetime import datetime

def print_execution_time(func):
    def wrapper(*args, **kwargs):
        init = datetime.now()
        func(*args, **kwargs)
        end = datetime.now()
        time_elapse = end - init
        print(f'El tiempo de ejecución fue de: {time_elapse}')
    return wrapper


@print_execution_time
def random_func(a: int):
    for _ in range(a):
        pass


def main():
    random_func(1000000)


if __name__ == "__main__":
    main()