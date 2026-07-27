class Solution(object):
    def triangleNumber(self, nums):
        nums.sort()
        n = len(nums)
        res = 0

        for i in range(n - 1, 1, -1):
            l = 0
            r = i - 1

            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    res += (r - l)   
                    r -= 1
                else:
                    l += 1

        return res