class Solution(object):
    def twoSum(self, nums, target):
        arr = [(num, i) for i, num in enumerate(nums)]
        arr.sort()

        l, r = 0, len(arr) - 1

        while l < r:
            s = arr[l][0] + arr[r][0]

            if s == target:
                return [arr[l][1], arr[r][1]]
            elif s > target:
                r -= 1
            else:
                l += 1