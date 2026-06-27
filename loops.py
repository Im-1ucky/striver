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


def print6(n):
    for i in range(1, n + 1):
        for j in range(1, n - i + 2):
            print(j, end="")
        print("")


def print7(n):
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        print("*" * (2 * i - 1), end="")
        print(" " * (n - i), end="")
        print("")


def print8(n):
    for i in range(n):
        print(" " * (i), end="")
        print("*" * (2 * n - (2 * i) - 1), end="")
        print(" " * (i), end="")
        print("")


def print9(n):
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        print("*" * (2 * i - 1), end="")
        print(" " * (n - i), end="")
        print("")
    for i in range(n):
        print(" " * (i), end="")
        print("*" * (2 * n - (2 * i) - 1), end="")
        print(" " * (i), end="")
        print("")


def main():
    n = int(input("Enter number: "))
    print9(n)


main()
