class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pointer_1 = 0
        for pointer_2 in range(0, len(nums)):
            if nums[pointer_2] != 0:
                nums[pointer_1], nums[pointer_2] = nums[pointer_2], nums[pointer_1]
                pointer_1 += 1

