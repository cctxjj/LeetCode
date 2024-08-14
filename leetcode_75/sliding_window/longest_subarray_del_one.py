class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s, e = 0, 0
        zeroes = 0
        max_subarray = 0

        while e < len(nums):
            if nums[e] == 0:
                zeroes += 1
            while zeroes > 1:
                if nums[s] == 0:
                    zeroes -= 1
                s += 1
            max_subarray = max(max_subarray, e - (s - 1) - 1)

            e += 1

        return max_subarray



