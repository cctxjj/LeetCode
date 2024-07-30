class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pairs = {}
        # keys: possible nums to be found in further loop through array;
        # vals: index with corresponding num in the nums list
        for index, element in enumerate(nums):
            if element in pairs:
                return pairs[element], index
            else:
                pairs[target - element] = index
        return False
