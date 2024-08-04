'''
1 = 1
2 = 2
3 = 3 (1, 1, 1); (1, 2) --> 2x;
4 = 5 (1, 1, 1, 1); (1, 1, 2) --> 3x; (2, 2)
5 = 8 (1, 1, 1, 1, 1); (1, 1, 1, 2) --> 4x, (1, 2, 2) --> 3x
6 =   (1, 1, 1, 1, 1, 1); (1, 1, 1, 1, 2) --> 5x, (1, 1, 2, 2) --> n!/k1!*k2!...kx!
'''
import math


class Solution(object):
    def climbStairs(self,
                    n):
        """
        :type n: int
        :rtype: int
        """
        options = []

        for i in range(0, n):
            options.append(1)

        count = 1

        pop_count = 0
        for i in range(0, math.floor(n / 2)):
            options.pop(-1 - pop_count)
            options.pop(-1 - pop_count)
            options.append(2)
            pop_count += 1
            print(options)
            count += self.__get_combs__(options)

        return count

    def __get_combs__(self,
                      l):
        n = len(l)
        k1 = l.count(1)
        k2 = l.count(2)
        return int(math.factorial(n) / (math.factorial(k1) * math.factorial(k2)))



