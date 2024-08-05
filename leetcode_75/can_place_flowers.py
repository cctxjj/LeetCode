# checking early in line 29 is lowkey op, didn't think of that myself...

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        if len(flowerbed) == 0:
            return False
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return True
            return False

        count = 0

        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            count += 1

        for index, pod in enumerate(flowerbed[1:len(flowerbed) - 1]):
            if pod == 0 and flowerbed[index] != 1 and flowerbed[index + 2] != 1:
                count += 1
                flowerbed[index + 1] = 1
                if count >= n:
                    return True

        if flowerbed[-1] == 0 and flowerbed[-2] != 1:
            count += 1
            flowerbed[-1] = 1

        return count >= n


sol = Solution()
print(sol.canPlaceFlowers([0, 0, 1, 0, 0], 3))
