def q1(arr: list[int]) -> int:
    return max(arr)


def q2(arr: list[int]) -> int:
    lar = arr[0]
    seclar = float("-inf")
    for i in arr[1:]:
        if i > lar:
            seclar = lar
            lar = i
        elif i > seclar and i < lar:
            seclar = i
    return int(seclar)


def q3(arr: list[int]) -> bool:
    count = 0
    n = len(arr)
    for i in range(n):
        if arr[i] > arr[(i + 1) % n]:
            count += 1
            if count > 1:
                return False
    return True


def q4(arr: list[int]) -> int:
    a = 0
    b = 1
    count = 1
    while b < len(arr):
        if arr[a] != arr[b]:
            a += 1
            arr[a] = arr[b]
            b += 1
            count += 1
        else:
            b += 1
    arr.append(arr[b - 1])
    return count


def main():
    arr1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    arr2 = [1, 1, 2]
    print(q4(arr1))
    print(q4(arr2))


main()
