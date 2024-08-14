class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        height, max_alt = gain[0], gain[0]

        for element in gain[1:]:
            height += element
            max_alt = max(max_alt, height)
        return max(max_alt, 0)
