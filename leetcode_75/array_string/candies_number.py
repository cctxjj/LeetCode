class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result = []
        top_candies = max(candies)
        for number in candies:
            result.append(number + extraCandies >= top_candies)
        return result


sol = Solution()
print(sol.kidsWithCandies([2, 3, 5, 1, 3], 3))
