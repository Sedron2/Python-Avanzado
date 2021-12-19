import time

class FiboIter:
    
    def __init__(self, max=None):
        self.max = max
        self.n1 = 0
        self.n2 = 1
        self.n3 = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n2 >= self.max:
            raise StopIteration
        else:
            self.n1 = self.n2
            self.n2 = self.n3
            self.n3 = self.n1 + self.n2
            return self.n1


def main():
    fibonacci = FiboIter(max=100)
    for number in fibonacci:
        print(number)
        time.sleep(0.5)


if __name__ == "__main__":
    main()