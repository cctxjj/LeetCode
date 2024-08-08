import sys


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        if nums.count(nums[0]) == len(nums):
            return False

        a = 10000000000000
        b = 10000000000000
        for i in range(len(nums)):
            if b < nums[i] and a < nums[i]:
                return True
            elif a >= nums[i]:
                a = nums[i]
            elif b >= nums[i] > a:
                b = nums[i]
        return False


sol = Solution()
print(sol.increasingTriplet([5, 1, 1,1 , 1, 1, 1, 1, 1, 1, 1, 1, 2, 3]))
