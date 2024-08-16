class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        left = 0
        right = sum(nums[1:])
        while index < len(nums):
            if left == right:
                return index
            if index + 1 < len(nums)-1:
                right -= nums[index+1]
            left += nums[index]
            index += 1
        return -1
