class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        cur_ind = 0
        count_zeros = nums.count(0)
        for num in nums:
            if num != 0:
                nums[cur_ind] = num
                cur_ind += 1
        while nums.count(0) < count_zeros:
            nums[cur_ind] = 0
            cur_ind += 1
        return nums