def print1(n):
    for i in range(n):
        print("*" * n)


def print2(n):
    for i in range(1, n + 1):
        print("*" * i)


def print3(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(j + 1, end="")
        print("")


def print4(n):
    for i in range(1, n + 1):
        print(f"{i}" * i)


def print5(n):
    for i in range(n, 0, -1):
        print("*" * i)


def main():
    n = int(input("Enter number: "))
    print5(n)


main()
