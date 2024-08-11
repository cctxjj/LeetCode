class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if len(height) == 2:
            return min(height[0], height[1])

        max_water = 0

        pointer_1 = 0
        pointer_2 = len(height) - 1

        while pointer_1 < pointer_2:
            area = min(height[pointer_1], height[pointer_2])*abs(pointer_2 - pointer_1)
            max_water = max(max_water, area)
            if height[pointer_1] < height[pointer_2]:
                pointer_1 += 1
            else:
                pointer_2 -= 1
        return max_water


sol = Solution()
print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
