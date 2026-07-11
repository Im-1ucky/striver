from collections import defaultdict
from typing import List


class Solution:
    def q1(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            temp_t = []
            for j in range(0, i + 1):
                if i == j or j == 0:
                    temp_t.append(1)
                else:
                    k = res[i - 1][j] + res[i - 1][j - 1]
                    temp_t.append(k)
            res.append(temp_t)
        return res

    def q2(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
            if len(count) < 2:
                continue
            new_count = defaultdict(int)
            for n, c in count.items():
                if c > 1:
                    new_count[n] = c - 1
            count = new_count
        res = []
        for n in count:
            if nums.count(n) > len(nums) // 3:
                res.append(n)
        return res

    def q3(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                ts = n + nums[l] + nums[r]
                if ts == 0:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif ts > 0:
                    r -= 1
                elif ts < 0:
                    l += 1
        return res

    def q4(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i, a in enumerate(nums[:-3]):
            if i > 0 and a == nums[i - 1]:
                continue
            for b in range(i + 1, len(nums) - 2):
                if b > i + 1 and nums[b] == nums[b - 1]:
                    continue
                l = b + 1
                r = len(nums) - 1
                while l < r:
                    fs = a + nums[b] + nums[l] + nums[r]
                    if fs == target:
                        res.append([a, nums[b], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif fs > target:
                        r -= 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif fs < target:
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
        return res

    def q5(self, nums: List[int]) -> int:
        psum = {}
        csum = 0
        max_l = 0
        for i, a in enumerate(nums):
            csum += a
            if csum == 0:
                max_l = max(max_l, i + 1)
            if csum not in psum:
                psum[csum] = i
            else:
                max_l = max(max_l, i - psum[csum] + 1)
        return max_l


def main():
    s = Solution()
    print(s.q1(5))


main()
