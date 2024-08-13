class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if nums.count(0) == len(nums):
            return k

        max_ones = 0
        zeros = 0
        ones = 0

        start = 0
        end = 0

        while end < len(nums):

            if nums[end] == 1:
                ones += 1
            else:
                zeros += 1

            if zeros > k:
                while zeros > k:
                    if nums[start] == 1:
                        ones -= 1
                    else:
                        zeros -= 1
                    start += 1

            max_ones = max(max_ones, ones + zeros)
            end += 1
        return max_ones


