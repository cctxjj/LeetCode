class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        els = []
        for element in set(arr):
            if arr.count(element) in els:
                return False
            els.append(arr.count(element))
        return True

sol = Solution()
print(sol.uniqueOccurrences([1, 1, 2]))