import math


class Solution(object):

    def __init__(self):
        self.prefix = []
        self.suffix = []

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        self.prefix.append(1)
        for i in range(1, len(nums)):
            self.prefix.append(self.prefix[i - 1] * nums[i - 1])

        print(self.prefix)

        self.suffix = [1] * len(nums)
        self.suffix[-2] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            self.suffix[i] = self.suffix[i + 1] * nums[i+1]
        print(self.suffix)

        for i in range(0, len(nums)):
            result.append(self.prefix[i] * self.suffix[i])
        return result


sol = Solution()
print(sol.productExceptSelf([1, 2, 3, 4]))
