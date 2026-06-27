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


def print10(n):
    for i in range(1, n * 2):
        if i <= n:
            print("*" * i)
        else:
            print("*" * (n * 2 - i))


def print11(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(((i + j + 1) % 2), end="")
        print("")


def print12(n):
    for i in range(1, n + 1):
        for a in range(1, i + 1):
            print(a, end="")
        print(" " * ((n * 2) - (i * 2)), end="")
        for c in range(i, 0, -1):
            print(c, end="")
        print("")


def print13(n):
    va = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(va, end="")
            va += 1
        print("")


def print14(n):
    for i in range(1, n + 1):
        for j in range(0, i):
            print(chr(ord("A") + j), end="")
        print("")


def print15(n):
    for i in range(1, n + 1):
        for j in range(0, n - i + 1):
            print(chr(ord("A") + j), end="")
        print("")


def print16(n):
    for i in range(n):
        print(chr(ord("A") + i) * (i + 1))


def print17(n):
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        for j in range((2 * i) - 1):
            if j <= i - 1:
                print(chr(ord("A") + j), end="")
            else:
                print(chr(ord("A") + (2 * i - 2 - j)), end="")
        print(" " * (n - i))


def print18(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(chr(ord("E") - i + j + 1), end="")
        print("")


def print19(n):
    for i in range(n):
        for j in range(n):
            if j < n - i:
                print("*", end="")
            else:
                print(" ", end="")
        for j in range(n):
            if j < i:
                print(" ", end="")
            else:
                print("*", end="")
        print("")
    for i in range(n):
        for j in range(n):
            if j <= i:
                print("*", end="")
            else:
                print(" ", end="")
        for j in range(n):
            if (n - i - 1 - j) <= 0:
                print("*", end="")
            else:
                print(" ", end="")
        print("")


def print20(n):
    for i in range(n):
        for j in range(n):
            if j <= i:
                print("*", end="")
            else:
                print(" ", end="")
        for j in range(n):
            if j < n - i - 1:
                print(" ", end="")
            else:
                print("*", end="")
        print("")
    for i in range(1, n):
        for j in range(n):
            if j < n - i:
                print("*", end="")
            else:
                print(" ", end="")
        for j in range(n):
            if j < i:
                print(" ", end="")
            else:
                print("*", end="")
        print("")


def print21(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or (i + 1) == n:
                print("*" * n, end="")
                break
            elif j == 0 or (j + 1) == n:
                print("*", end="")
            else:
                print(" ", end="")
        print("")


def print22(n):
    for i in range(n * 2 - 1):
        for j in range(n * 2 - 1):
            if j == 0 or j == 2 * n - 2 or i == 0 or i == 2 * n - 2:
                print(n, end="")
            else:
                print(n - min(i, j, 2 * n - i - 2, 2 * n - j - 2), end="")
        print("")


def main():
    n = int(input("Enter number: "))
    print22(n)


main()
