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
    while b < len(arr):
        if arr[a] != arr[b]:
            a += 1
            arr[a] = arr[b]
            b += 1
        else:
            b += 1
    return a + 1


def q56(nums: list[int], k: int) -> None:
    n = len(nums)
    k %= n

    def reverse(left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)


def q7(nums: list[int]) -> None:
    l, r = 0, 0
    while r < len(nums):
        if nums[r] != 0:
            nums[l] = nums[r]
            l += 1
        r += 1
    while l < len(nums):
        nums[l] = 0
        l += 1


def q8(nums: list[int], target: int) -> int:
    if target in nums:
        return nums.index(target)
    return -1


def q9(nums1: list[int], nums2: list[int]) -> list[int]:
    i = j = 0
    nums3 = []
    while i < len(nums1) or j < len(nums2):
        if i >= len(nums1):
            if nums3 or nums3[-1] != nums2[j]:
                nums3.append(nums2[j])
                j += 1
            else:
                j += 1
        elif j >= len(nums2):
            if nums3[-1] != nums1[i]:
                nums3.append(nums1[i])
                i += 1
            else:
                i += 1
        else:
            if nums1[i] < nums2[j] and nums3[-1] != nums1[i]:
                nums3.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j] and nums3[-1] != nums2[j]:
                nums3.append(nums2[j])
                j += 1
            else:
                if not nums3 or nums3[-1] != nums1[i]:
                    nums3.append(nums1[i])
                    i += 1
                else:
                    i += 1
                    j += 1
    return nums3


def q10(nums: list[int]) -> int:
    asums = (len(nums) * (len(nums) + 1)) // 2
    sums = sum(nums)
    return asums - sums


def q11(nums: list[int]) -> int:
    cmax = count = 0
    for i in nums:
        if i == 1:
            count += 1
            cmax = max(count, cmax)
        else:
            count = 0
    return cmax


def q12(nums: list[int]) -> int:
    ele = 0
    for i in nums:
        ele ^= i
    return ele


def q13(nums: list[int], target: int) -> int:
    i = j = maxs = 0
    sums = nums[0]
    while j < len(nums):
        if sums < target:
            j += 1
            if j < len(nums):
                sums += nums[j]
        elif sums > target:
            sums -= nums[i]
            i += 1
        else:
            maxs = max(maxs, (j - i + 1))
            j += 1
            if j < len(nums):
                sums += nums[j]
    return maxs


def q14(nums: list[int], target: int) -> int:
    psum = {}
    csum = 0
    longsa = 0
    for index, n in enumerate(nums):
        csum += n
        if csum not in psum:
            psum[csum] = index
        elif (csum - target) in psum:
            longsa = max(longsa, index - psum[csum - target])
        elif csum == target:
            longsa = max(longsa, index + 1)
    return longsa


def main():
    arr1 = [1, 2, -3, 1, 1, 1, 4, -1]
    print(q14(arr1, 3))


main()
