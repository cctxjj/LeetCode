class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        potions.sort()
        result = []
        for index in range(len(spells)):
            index_potions = int(round(len(potions)))
            result.append(0)
            cont = True
            while cont:
              # binary search
                pass
        return result


sol = Solution()
print(sol.successfulPairs([3, 1, 2], [1, 2, 3, 4, 5], 7))

# redo