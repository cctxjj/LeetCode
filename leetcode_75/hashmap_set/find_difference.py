class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        result = [[], []]
        for element in nums1:
            if element not in nums2 and element not in result[0]:
                result[0].append(element)
        for element in nums2:
            if element not in nums1 and element not in result[1]:
                result[1].append(element)

        return result
