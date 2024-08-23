class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_cpy = []
        for element in nums:
            if element not in nums_cpy:
                nums_cpy.append(element)
            else:
                nums_cpy.remove(element)
        return nums_cpy[0]
