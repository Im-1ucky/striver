from typing import List


class Solution:
    def q1(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in store:
                return [store[complement], i]
            store[n] = i
        return []

    def q2(self, nums: List[int]) -> None:
        mid = low = 0
        high = len(nums) - 1
        while mid < high:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
            elif nums[mid] == 2:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
            else:
                mid += 1
        print(nums)

    def q3(self, nums: List[int]) -> int:
        count = 0
        ele = nums[0]
        for i in nums:
            if i == ele:
                count += 1
            else:
                count -= 1
                if count < 0:
                    ele = i
                    count = 1
        return ele

    def q4(self, nums: List[int]) -> int:
        cur_sum = 0
        max_sum = 0
        for i in nums:
            cur_sum += i
            if cur_sum < 0:
                cur_sum = 0
            else:
                max_sum = max(cur_sum, max_sum)
        return max_sum

    def q5(self, nums: List[int]) -> None:
        cur_sum = 0
        max_sum = 0
        start = 0
        temp_start = 0
        end = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum < 0:
                cur_sum = 0
                temp_start = i + 1
            else:
                if cur_sum > max_sum:
                    max_sum = cur_sum
                    end = i
                    start = temp_start
        print(nums[start : end + 1])

    def q6(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_sum = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                max_sum = max(max_sum, (prices[r] - prices[l]))
            r += 1
        return max_sum

    def q7(self, nums: List[int]) -> List[int]:
        pos_p = 0
        neg_p = 0
        res = []
        for i in range(len(nums)):
            if i % 2 == 0:
                while not nums[pos_p] > 0:
                    pos_p += 1
                res.append(nums[pos_p])
                pos_p += 1
            else:
                while not nums[neg_p] < 0:
                    neg_p += 1
                res.append(nums[neg_p])
                neg_p += 1
        return res

    def q8(self, nums: List[int]) -> None:
        pivot = -1
        minei = 0
        for i in range(len(nums) - 1, 0, -1):
            if (nums[i - 1]) < nums[i]:
                pivot = i
                break
        if pivot == -1:
            nums.reverse()
        else:
            for j in range(len(nums) - 1, pivot - 1, -1):
                if nums[j] > nums[pivot - 1]:
                    minei = j
                    break
            nums[pivot - 1], nums[minei] = nums[minei], nums[pivot - 1]
            r = len(nums) - 1
            while pivot < r:
                nums[pivot], nums[r] = nums[r], nums[pivot]
                pivot += 1
                r -= 1

    def q9(self, nums: List[int]) -> List[int]:
        max = float("-inf")
        res = []
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > max:
                res.append(nums[i])
                max = nums[i]
        return res

    def q10(self, nums: List[int]) -> int:
        nums.sort()
        ele = nums[0]
        max_l = 1
        for i in nums:
            if ele + 1 == i:
                ele = i
                max_l += 1
            else:
                ele = i
            i += 1
        return max_l

    def q11(self, matrix: List[List[int]]) -> None:
        nrows = len(matrix)
        ncols = len(matrix[0])
        rz, cz = False, False
        for i in range(nrows):
            if matrix[i][0] == 0:
                rz = True
                break
            i += 1
        for i in range(ncols):
            if matrix[0][i] == 0:
                cz = True
                break
            i += 1
        for i in range(1, nrows):
            for j in range(1, ncols):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                j += 1
            i += 1
        for i in range(1, nrows):
            for j in range(1, ncols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                j += 1
            i += 1
        if rz:
            for i in range(nrows):
                matrix[i][0] = 0
                i += 1
        if cz:
            for i in range(ncols):
                matrix[0][i] = 0
                i += 1

    def q12(self, matrix: List[List[int]]) -> None:
        nrows = len(matrix)
        ncols = len(matrix[0])
        for i in range(nrows):
            for j in range(i + 1, ncols):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(nrows):
            matrix[i].reverse()

    def q13(self, matrix: List[List[int]]) -> List[int]:
        top, left = 0, 0
        right = len(matrix[0])
        bottom = len(matrix)
        res = []
        while top < bottom and left < right:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            if top >= bottom or left >= right:
                break
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            if top >= bottom or left >= right:
                break
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            if top >= bottom or left >= right:
                break
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            if top >= bottom or left >= right:
                break
        return res

    def q14(self, nums: List, k: int) -> int:
        curSum = 0
        prefixSum = {0: 1}
        res = 0
        for i in nums:
            curSum += i
            diff = curSum - k
            res += prefixSum.get(diff, 0)
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)
        return res


def main():
    arr1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    s = Solution()
    print(s.q13(arr1))


main()
